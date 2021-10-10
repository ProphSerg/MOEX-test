import re
import json
import os

Interface = {}
'''
<a name="t0_22"></a>
    <h4>SECURITIES - Финансовые инструменты (обновляемая)</h4>
    <ul>
        Таблица содержит текущую биржевую информацию о финансовых инструментах, относящихся к различным режимам торгов.
        Каждая строка таблицы соответствует уникальной паре режим торгов - финансовый инструмент.<p>
        <table
'''
pTbl = re.compile(r'<a name="t.+?<h4>(\w+) - (.+?)</h4>.*?(<ul>.+?)\s*?(<table.*?>(.+?)</table>|Входных полей нет<br>).*?<table.*?>(.+?)</table>.*?</ul>', flags=re.MULTILINE)
#pRC = re.compile(r'<tr.*?>(<td.*?>(.+?)</td>)+?</tr>')
pRow = re.compile(r'<tr.*?>(.*?)</tr>')
pCol = re.compile(r'<td.*?>(.*?)</td>')

for root, dir, files in os.walk('.'):
    for file in files:
        r = re.search(r'(\w+?)(\d{2})_Broker_Russian.htm', file)
        if not r: continue
        Imrk = r[1]
        Iver = r[2]
        if not Iver in Interface: Interface[Iver] = {}
        if not Imrk in Interface[Iver]: Interface[Iver][Imrk] = {}
        with open(file, 'r') as a_file: s = a_file.read()
        s = re.sub(r'<a href=.+?>(.+?)</a>', r'\1', s.replace('\n', ' ').replace('<b>', '').replace('<a href=#refs>*</a>', ''))

        for r in pTbl.findall(s):
            rr = pRow.findall(r[5])
            if not 'output' in Interface: Interface['output'] = list(map(str.strip, pCol.findall(rr[0])))
            Interface[Iver][Imrk][r[0]] = {
                'output': list(map(lambda x: list(map(str.strip, pCol.findall(x))), rr[1:])),
                'title': r[1].strip(),
                'desc': r[2].strip()
            }

            if len(r[4]) > 0:
                rr = pRow.findall(r[4])
                if not 'input' in Interface: Interface['input'] = list(map(str.strip, pCol.findall(rr[0])))
                Interface[Iver][Imrk][r[0]].update({'input': list(map(lambda x: list(map(str.strip, pCol.findall(x))), rr[1:]))})

with open('ASTSreq.py', 'w') as f_map:
    f_map.write('ASTSreq = ')
    json.dump(Interface, f_map, ensure_ascii=False, indent=4)
