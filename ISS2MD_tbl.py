from ISS2MarketData import MOEX_const, MOEX_value
from config import load_data
from ASTSreq import ASTSreq

Fields = {}
print('Generate Table ISS2MarketData ....', end='')
with open('ISS2MarketData.html', "w") as a_file:
    a_file.write('<html lang="ru"><head><meta charset="utf-8"></head><body>\n')
    a_file.write( \
        '<table border="1"><tr>' \
            '<th colspan=2 colstyle="text-align: center;">MarketData value<p>(Java)</th>' \
            '<th colspan=%d style="text-align: center;">Конфигурация:</th></tr>' \
        '<tr><th style="text-align: center;">Название</th>' \
            '<th style="text-align: center;">Opt.</th>'  % len(load_data['config']) \
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
print(' Done!')

for f in Fields:
    print('%20s:\t%5s\t%5s' % (f,
                               str(f in list(map(lambda x: x[0], ASTSreq['36']['Equities']['SECURITIES']['output']))),
                               str(f in ASTSreq['36']['Currency'])))
'''
print('Generate Table ISSmapASTS ....', end='')
with open('ISSmapASTS.html', "w") as a_file:
    a_file.write('<html lang="ru"><head><meta charset="utf-8"></head><body>\n')
    a_file.write( \
        '<table border="1"><tr>' \
            '<th colspan=2 colstyle="text-align: center;">MarketData value<p>(Java)</th>' \
            '<th colspan=%d style="text-align: center;">Конфигурация:</th></tr>' \
        '<tr><th style="text-align: center;">Название</th>' \
            '<th style="text-align: center;">Opt.</th>'  % len(load_data['config']) \
    )
    for cfg_name in load_data['config']:
        a_file.write('<th style="text-align: center;">%s</th>' % cfg_name)
    a_file.write('</tr>\n')

    for bl in ['MarketData', 'BondMarketData', 'IndexMarketData']:
        a_file.write('<tr><td colspan=%d colstyle="text-align: left;">Структура <b><i>%s</i></b></td></tr>\n' % (len(load_data['config']) + 2, bl))
'''