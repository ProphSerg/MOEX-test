from ISS2MarketData import MOEX_const, MOEX_value
from config import load_data
from ASTSreq import ASTSreq
import json

Fields = {}
print('Generate Table ISS2MarketData ....', end='')
with open('ISS2MarketData.html', "w") as a_file:
    a_file.write('<html lang="ru"><head><meta charset="utf-8"></head><body>\n')
    a_file.write('<table border="1"><tr>'
                 '<th colspan=2 colstyle="text-align: center;">MarketData value<p>(Java)</th>'
                 '<th colspan=%d style="text-align: center;">Конфигурация:</th></tr>'
                 '<tr><th style="text-align: center;">Название</th>'
                 '<th style="text-align: center;">Opt.</th>' % len(load_data['config'])
    )
    for cfg_name in load_data['config']:
        a_file.write('<th style="text-align: center;">%s</th>' % cfg_name)
    a_file.write('</tr>\n')

    for bl in ['MarketData', 'BondMarketData', 'IndexMarketData']:
        a_file.write('<tr><td colspan=%d colstyle="text-align: left;">Структура <b><i>%s</i></b></td></tr>\n' % (len(load_data['config']) + 2, bl))
        for Mv, Mvv in MOEX_value[bl].items():
            a_file.write('<tr><td>%s</td><td style="text-align: center;">%s</td>' % (Mv, 'O' if Mvv['options'] == 'optional' else 'R'))

            for cfg_name in load_data['config']:
                a_file.write('<td>')
                if cfg_name in Mvv:
                    Mvc = Mvv[cfg_name]
                    if 'const' in Mvc:
                        if Mvc['const'].isdigit():
                            a_file.write('Константа: <i>%s</i>' % Mvc['const'])
                        else:
                            c = MOEX_const[Mvc['const']]
                            a_file.write('Константа<p><b>%s</b> = <i>%s</i>' %
                                         (Mvc['const'], f'"{c}"' if isinstance(c,str) else str(c)))
                    elif 'block' in Mvc:
                        a_file.write('Блок ISS: <i>%s</i><p>Поле: <i>%s</i>' %
                                     (Mvc['block'], ', '.join( list( map(lambda x: MOEX_const[x], Mvc['field']) ) ) )
                                      )
                        Fields.update(dict.fromkeys(list( map(lambda x: MOEX_const[x], Mvc['field']) ) ))
                    elif 'NONE' in Mvc:
                        a_file.write('???')
                    if 'comment' in Mvc:
                        if 'link' in Mvc:
                            a_file.write('<p>Ссылка на: <i>%s</i>' % Mvc['link'])
                        if 'map' in Mvc:
                            a_file.write('<p><b>Use map</b>')
                        if 'contains' in Mvc:
                            a_file.write('<p><b>Use contains</b>')
                        a_file.write('<p>Как: <i>%s</i>' % Mvc['comment'])

                a_file.write('</td>')

            a_file.write('</tr>\n')
    a_file.write('</table></body></html>\n')
print(' Done!')

with open('columns.json', "r") as a_file:
    columns = json.load(a_file)

print('Generate Table ISSmapASTS ....', end='')
ver = '36'
with open('ISSmapASTS.html', "w") as a_file:
    a_file.write('<html lang="ru"><head><meta charset="utf-8"></head><body>\n')
    fMAP = {}
    for cfg_name in load_data['config']:
        cfg = load_data['config'][cfg_name]
        val = 'Equities' if cfg_name != 'currencies' else 'Currency'
        if not val in fMAP: fMAP[val] = {}

        for md in cfg['ISS']:
            for f in MOEX_value[md]:
                if cfg_name in MOEX_value[md][f] and 'block' in MOEX_value[md][f][cfg_name]:
                    for i in MOEX_value[md][f][cfg_name]['field']:
                        fMAP[val]['%s.%s' % (MOEX_value[md][f][cfg_name]['block'], MOEX_const[i])] = set()

    for mk in fMAP:
        a_file.write('Рынок: %s<br>\n'
            '<table border="1"><tr>'
            '<th colspan=2 colstyle="text-align: center;">ISS</th>'
            '<th colspan=2 colstyle="text-align: center;">ASTS</th></tr>\n'
            '<tr><th style="text-align: center;">Поле</th><th colstyle="text-align: center;">Описание</th>'
            '<th style="text-align: center;">Поле</th><th colstyle="text-align: center;">Описание</th></tr>\n' % mk
        )

        for f in sorted(fMAP[mk]):
            b = f.split('.')[0]
            t = f.split('.')[1]

            for tb in ['SECURITIES', 'INDEXES']:
                for s in ASTSreq[ver][mk][tb]['output']:
                    if t == s[0]: fMAP[mk][f].update(['%s|%s|%s|%s' % (tb, t, s[1], s[4])])

            if len(fMAP[mk][f]) > 0:
                a_file.write('<tr>'
                    '<td rowspan=%d>%s</td><td rowspan=%d>%s<br>%s</td>%s\n'
                    % (len(fMAP[mk][f]), f, len(fMAP[mk][f]), columns[b][t]['info']['short_title'], columns[b][t]['info']['title'],
                       '<tr>'.join(list(map(lambda x: '<td>%s.%s</td><td>%s<br>%s</td></tr>' % (x.split('|')[0], x.split('|')[1], x.split('|')[2], x.split('|')[3]), fMAP[mk][f]))))
                )
            else:
                a_file.write('<tr><td><span style="color: rgb(255,0,0);"><b>%s</b></span></td>'
                             '<td><span style="color: rgb(255,0,0);"><b>%s<br>%s</b></span></td><td></td><td></td>\n' % (f, columns[b][t]['info']['short_title'], columns[b][t]['info']['title']))
        a_file.write('</table><p>\n')

    a_file.write('</body></html>\n')
