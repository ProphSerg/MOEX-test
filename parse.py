import json
import re
import os
import os.path
from parseValue import parseValue

MOEX_const = {}
MOEX_value = {}
patt = re.compile(r'(MOEX.+?)\s*=\s*"(\w+?)"')
for s in open('/Users/proph/IdeaProjects/SBERINVESTOR/java_marketdata-loader/src/main/java/com/sberbank/si20/marketdata/loader/impl/constants/MoexTag.java'):
    r = patt.search(s)
    if r: MOEX_const[r[1]] = r[2]
MOEX_const.update({
    'TRADING_AVAILABLE_STATUS': 'TRADING_AVAILABLE',
    'TRADING_NOT_AVAILABLE_STATUS': 'TRADING_NOT_AVAILABLE',
    'DEFAULT_INDEXES_LOT_SIZE': -1,
    'DEFAULT_INDEXES_PRICE_STEP': -1.0,
    'RUB': 'RUB',
})

pStruct = re.compile(r'struct (\w*?MarketData\w*?)')
pBlock = re.compile(r'(optional|required).+?(\w+);')
isFind = False
for s in open('/Users/proph/IdeaProjects/SBERINVESTOR/java_commons/marketdata-tools/src/main/thrift/marketdata.thrift'):
    if isFind:
        if s.find('}') >= 0:
            isFind = False
        else:
            r = pBlock.search(s)
            if r:
                if not val_name in MOEX_value: MOEX_value[val_name] = {}
                MOEX_value[val_name].update({r[2]: {'options': r[1]}})
    else:
        r = pStruct.search(s)
        if r:
            val_name = r[1]
            isFind = True

pStruct = re.compile(r'return new (\w*?MarketData\w*?)')
pBlock = re.compile(r'\.set(\w+?)\((.+?)\)$')
for root, dirs, files in os.walk('/Users/proph/IdeaProjects/SBERINVESTOR/java_marketdata-loader/src/main/java/com/sberbank/si20/marketdata/loader/impl/moex/readers/impl/mappers/markets'):
    files.append('../MarketDataBondMarketDataMapper.java')
    for file in files:
        r = re.search(r'MarketData(\w+?)Mapper', file)
        if r: cfg_name = r[1].lower() if r[1] != 'BondMarketData' else 'bonds'

        isFind = False
        for s in open(os.path.join(root, file)):
            s = s.strip().rstrip(' ;')
            if isFind:
                if s.find('}') >= 0:
                    isFind = False
                else:
                    r = pBlock.search(s)
                    if r:
                        val = r[1].replace(r[1][0], r[1][0].lower(), 1)
                        if not cfg_name in MOEX_value[val_name][val]: MOEX_value[val_name][val][cfg_name] = {}
                        MOEX_value[val_name][val][cfg_name].update(parseValue(r[2]))
            else:
                r = pStruct.search(s)
                if r:
                    val_name = r[1]
                    isFind = True


with open('ISS2MarketData.py', 'w') as f_map:
    f_map.write('MOEX_const = ')
    json.dump(MOEX_const, f_map, ensure_ascii=False, indent=4)
    f_map.write('\n\nMOEX_value = ')
    json.dump(MOEX_value, f_map, ensure_ascii=False, indent=4)