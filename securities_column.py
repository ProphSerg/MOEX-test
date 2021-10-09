import requests
import collections
import json
import os.path
from config import load_data

class myJSONEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, set):
            return list(z)
        else:
            super().default(self, z)

url={}
columns = {}

if os.path.isfile('columns.json'):
    print('Load ....')
    with open('columns.json', "r") as a_file:
        columns = json.load(a_file)
else:
    for cfg_name, cfg in load_data['config'].items():
        for market in cfg['market']:
            url['data'] = load_data['url']['data'].replace('<engine>', cfg['engine']).replace('<market>', market)
            url['metadata'] = (load_data['url']['metadata'].replace('<engine>', cfg['engine'])).replace('<market>', market)

            req = requests.get(url['data'])
            mreq = requests.get(url['metadata'])
            jreq = req.json()
            jmreq = mreq.json()

            if not 'securities' in columns:
                columns['securities'] = {}
                columns['marketdata'] = {}

            for bl in ('securities', 'marketdata'):
                if len(jreq[bl]['metadata']) != len(jmreq[bl]['data']):
                    print('Config: %s. Block: %s. Length column data (%d) NOT equals Length metadata (%d)' % (cfg_name, bl, len(jreq[bl]['metadat']), len(jmreq[bl]['data'])))

                for md in jmreq[bl]['data']:
                    mdd = dict(zip(jmreq[bl]['columns'], md))
                    k = mdd['name']
                    if not k in jreq[bl]['metadata']:
                        print('Config: %s. Block: %s. Key <%s> not found in data!' % (cfg_name, bl, k))
                        continue
                    v = jreq[bl]['metadata'][k]
                    if not k in columns[bl]:
                        columns[bl][k] = v
                        columns[bl][k]['info'] = mdd
                    if not 'LOADIN' in columns[bl][k]:
                        columns[bl][k]['LOADIN'] = set([cfg_name])
                    else:
                        columns[bl][k]['LOADIN'].add(cfg_name)

    print('Save ....')
    columns = json.loads(json.dumps(columns, cls=myJSONEncoder))
    with open('columns.json', "w") as a_file:
        json.dump(columns, a_file)
    with open('columns_f.json', "w") as a_file:
        json.dump(columns, a_file, indent=4, ensure_ascii=False)

print('Generate Table securitie_coloumns....')
with open('securitie_coloumns.html', "w") as a_file:
    a_file.write('<html lang="ru"><body>\n')
    a_file.write( \
        '<table border="1"><tr>' \
            '<th colspan=3 style="text-align: center;">Поля загружаемые из ISS</th>' \
            '<th colspan=%d style="text-align: center;">Загружаются в конфигурации:</th></tr>' \
        '<tr><th style="text-align: center;">Название</th>' \
            '<th style="text-align: center;">Описание</th>' \
            '<th style="text-align: center;">Тип</th>' % len(load_data['config']) \
    )
    for cfg_name in load_data['config']:
        a_file.write('<th style="text-align: center;">%s</th>' % cfg_name)
    a_file.write('</tr>\n')

    for bl in ('securities', 'marketdata'):
        a_file.write('<tr><td colspan=8 style="text-align: left;">Блок <b><i>%s</i></b></td></tr>\n' % bl)
        for k, v in columns[bl].items():
            a_file.write('<tr><td>%s</td><td>%s</td><td>%s</td>' % (v['info']['name'], v['info']['title'], v['info']['type']))
            for cfg_name in load_data['config']:
                a_file.write('<td style="text-align: center;">%s</td>' % ('+' if cfg_name in v['LOADIN'] else ' '))
            a_file.write('</tr>\n')

    a_file.write('</table></body></html>\n')

print('Done!')
