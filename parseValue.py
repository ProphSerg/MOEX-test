import re

def parseValue(arg):
    r = re.search(r'(securities|marketdata)\.get\w+?\((MOEX.+?),', arg)
    if r: return {'block': r[1], 'field': [r[2].strip()]}
    if re.match(r'marketDataTradingStatusMapper', arg):
        return {'block': 'marketdata',
                'field': ['MOEX_MARKETDATA_TRADING_STATUS'],
                'comment': arg,
                'contains': {'OFLDIESAab': '',
                             'T': 'TRADING_AVAILABLE',
                             '__else__': 'TRADING_NOT_AVAILABLE',
                             }
                }
    if re.match(r'(marketDataExchangeTimeMapper|marketDataUpdateTimeMapper)', arg):
        return {'block': 'marketdata',
                'field': ['MOEX_MARKETDATA_SYSTEM_TIME', 'MOEX_MARKETDATA_TIME'],
                'comment': arg,
                }
    if re.match(r'marketDataBondMarketDataMapper', arg):
        return {'link': 'BondMarketData',
                'comment': arg,
                }
    if re.match(r'toIndexMarketData', arg):
        return {'link': 'IndexMarketData',
                'comment': arg,
                }
    if re.match(r'marketDataSettleDateMapper', arg):
        return {'block': 'securities',
                'field': ['MOEX_SECURITIES_SETTLE_DATE'],
                'comment': arg,
                }
    if re.match(r'marketDataCurrencyMapper\.mapCurrencyId', arg):
        return {'block': 'securities',
                'field': ['MOEX_SECURITIES_CURRENCY_ID'],
                'map': ['SUR', 'RUB'],
                'comment': arg,
                }
    if re.match(r'marketDataYieldOfferMapper', arg):
        return {'block': 'marketdata',
                'field': ['MOEX_MARKETDATA_YIELD_LAST_COUPON', 'MOEX_MARKETDATA_YIELD_TO_OFFER'],
                'comment': arg,
                }
    if re.match(r'faceValueCalc', arg):
        return {'block': 'securities',
                'field': ['MOEX_SECURITIES_CURRENCY_ID', 'MOEX_SECURITIES_FACE_UNIT', 'MOEX_SECURITIES_FACE_VALUE'],
                'map': ['SUR', 'RUB'],
                'comment': arg,
                }
    if re.match(r'instrumentDao', arg):
        return {'NONE': 'None',
                'comment': arg,
                }
    if re.match(r'^([A-Z_]+|\d+)$', arg):
        return {'const': arg,
                }
    return {'NONE': 'None'}
