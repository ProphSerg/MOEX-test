import requests
import collections
import json
import os.path


def makehash():
    return collections.defaultdict(makehash)


engines = makehash()
markets = makehash()
boards = makehash()

TOOL = ('engines', 'markets', 'boards')

if all(os.path.isfile('%s.json' % (t)) for t in TOOL):
    for t in TOOL:
        print('Load %s ....' % (t))
        with open('%s.json' % (t), "r") as a_file:
            exec('%s = json.load(a_file)' % (t))
else:
    r_engines = requests.get('https://iss.moex.com/iss/engines.json')
    engines['metadata'] = r_engines.json()['engines']['metadata']
    engines['columns'] = r_engines.json()['engines']['columns']

    for engine in r_engines.json()['engines']['data']:
        e = {}
        for i, v in enumerate(engines['columns']):
            e[v] = engine[i]
        engines['engines'][e['id']] = e
        engines['engines'][e['id']]['markets'] = []

        r_markets = requests.get('https://iss.moex.com/iss/engines/%s/markets.json' % (engine[1]))
        if 'metadata' not in markets:
            markets['metadata'] = r_markets.json()['markets']['metadata']
            markets['columns'] = r_markets.json()['markets']['columns']

        for market in r_markets.json()['markets']['data']:
            e = {}
            for i, v in enumerate(markets['columns']):
                e[v] = market[i]
            markets['markets'][e['id']] = e
            markets['markets'][e['id']]['boards'] = []
            engines['engines'][engine[0]]['markets'].append(str(e['id']))

            r_boards = requests.get(
                'https://iss.moex.com/iss/engines/%s/markets/%s/boards.json' % (engine[1], market[1]))
            if 'metadata' not in boards:
                boards['metadata'] = r_boards.json()['boards']['metadata']
                boards['columns'] = r_boards.json()['boards']['columns']

            for board in r_boards.json()['boards']['data']:
                e = {}
                for i, v in enumerate(boards['columns']):
                    e[v] = board[i]
                boards['boards'][e['id']] = e
                markets['markets'][market[0]]['boards'].append(str(e['id']))

    #    print(resp.json()['markets'])

    for t in TOOL:
        print('Save %s ....' % (t))
        with open('%s.json' % (t), "w") as a_file:
            exec('%s = json.loads(json.dumps(%s))' % (t, t))
            exec('json.dump(%s, a_file)' % (t))

for t in TOOL:
    if not '_' in t:
        print('Count %s is %d' % (t, eval("len(%s['%s'])" % (t, t))))
        print(eval(t))

# for m, v in boards['boards'].items():
#     print('%15s(%d): ' %(v['boardid'], v['id']), end='')
#     print(v['markets'])

# for e, ms in e_m_bs['engines'].items():
#     print('%15s:' % (e))
#     for m, bs in ms['markets'].items():
#         print('%19s:' % (m))
#         for r in bs:
#             print('%23s - %s' % (r[2], r[3]))

print('Generate Table ....')
with open('engine_market_board.html', "w") as a_file:
    a_file.write('<html lang="ru"><body>\n')
    es = ''
    eng_other_tbl = \
        '<table border="1"><tr><th colspan=2 style="text-align: center;">Торговые системы</th><th colspan=2 style="text-align: center;">Рынки</th><th colspan=2 style="text-align: center;">Режимы торгов</th></tr>\n' \
        '<tr><th style="text-align: center;">Код</th><th style="text-align: center;">Название</th><th style="text-align: center;">Код</th><th style="text-align: center;">Название</th><th style="text-align: center;">Код</th><th style="text-align: center;">Название</th></tr>\n'

    mrk_other_tbl = \
        '<table border="1"><tr><th colspan=2 style="text-align: center;">Рынки</th><th colspan=2 style="text-align: center;">Режимы торгов</th></tr>\n' \
        '<tr><th style="text-align: center;">Код</th><th style="text-align: center;">Название</th><th style="text-align: center;">Код</th><th style="text-align: center;">Название</th></tr>\n'

    for ek, ev in engines['engines'].items():
        if not ev['name'] in ('futures', 'commodity', 'interventions', 'offboard', 'agro'):
            eng_single = True
            a_file.write('<p>%s (%s)<p>\n' % (ev['title'], ev['name']))
            a_file.write('<table border="1"><tr><th colspan=2 style="text-align: center;">Торговые системы</th></tr>\n')
            a_file.write('<tr><th style="text-align: center;">Код</th><th style="text-align: center;">Название</th></tr>\n')
            a_file.write('<tr><td>%s</td><td>%s</td></table>\n\n' % (ev['name'], ev['title']))
        else:
            eng_single = False

        er = 0
        ms = ''
        for em in ev['markets']:
            if ev['name'] in ('stock',):
                mrk_single = True
            else:
                mrk_single = False
            mr = 0
            bs = ''
            for mb in markets['markets'][em]['boards']:
                s = '<td>%s</td><td>%s</td>' % (boards['boards'][mb]['boardid'], boards['boards'][mb]['title'])
                bs += ('<tr>' if bs != '' else '') + s + '</tr>'
                mr += 1

            s = '<td rowspan=%d>%s</td><td rowspan=%d>%s</td>' % (mr, markets['markets'][em]['NAME'], mr, markets['markets'][em]['title'])
            ms += ('<tr>' if eng_single == True or ms != '' else '') + s + bs
            er += mr
            if mrk_single == True:
                if mr > 4:
                    a_file.write('<p>%s (%s)<p>\n'% (markets['markets'][em]['title'], markets['markets'][em]['NAME']))
                    a_file.write('<table border="1"><tr><th colspan=2 style="text-align: center;">Рынки</th><th colspan=2 style="text-align: center;">Режимы торгов</th></tr>\n')
                    a_file.write('<tr><th style="text-align: center;">Код</th><th style="text-align: center;">Название</th><th style="text-align: center;">Код</th><th style="text-align: center;">Название</th></tr>\n')
                    a_file.write('<tr>' + s + bs + '</table><p>\n')
                else:
                    mrk_other_tbl += '<tr>' + s + bs

        if mrk_single == True:
            a_file.write(mrk_other_tbl + '</table><p>\n')

        if eng_single == False:
            eng_other_tbl += '<tr><td rowspan=%d>%s</td><td rowspan=%d>%s</td>' % (er, ev['name'], er, ev['title']) + ms
        elif mrk_single == False:
            a_file.write('<table border="1"><tr>')
            if mrk_single == False: a_file.write('<th colspan=2 style="text-align: center;">Рынки</th>')
            a_file.write('<th colspan=2 style="text-align: center;">Режимы торгов</th></tr>\n<tr>')
            if mrk_single == False: a_file.write('<th style="text-align: center;">Код</th><th style="text-align: center;">Название</th>')
            a_file.write('<th style="text-align: center;">Код</th><th style="text-align: center;">Название</th></tr>\n')
            a_file.write(ms + '</table><p>\n')

    a_file.write(eng_other_tbl + '</table></body></html>\n')

print('Done!')
