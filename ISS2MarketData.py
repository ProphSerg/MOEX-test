MOEX_const = {
    "MOEX_EXCHANGE_NAME": "MOEX",
    "MOEX_AUTH_COOKIE_NAME": "MicexPassportCert",
    "MOEX_RESPONSE_ONLINE_MARKER_GRANTED": "granted",
    "MOEX_MARKETDATA_NODE": "marketdata",
    "MOEX_SECURITIES_NODE": "securities",
    "MOEX_MARKETDATA_SYSTEM_TIME": "SYSTIME",
    "MOEX_MARKETDATA_TIME": "TIME",
    "MOEX_MARKETDATA_TRADING_STATUS": "TRADINGSTATUS",
    "MOEX_MARKETDATA_BOARD_ID": "BOARDID",
    "MOEX_MARKETDATA_SEC_ID": "SECID",
    "MOEX_MARKETDATA_BID": "BID",
    "MOEX_MARKETDATA_HIGH_BID": "HIGHBID",
    "MOEX_MARKETDATA_OFFER": "OFFER",
    "MOEX_MARKETDATA_LOW_OFFER": "LOWOFFER",
    "MOEX_MARKETDATA_LAST": "LAST",
    "MOEX_MARKETDATA_SPREAD": "SPREAD",
    "MOEX_MARKETDATA_YIELD": "YIELD",
    "MOEX_MARKETDATA_YIELD_LAST_COUPON": "YIELDLASTCOUPON",
    "MOEX_MARKETDATA_YIELD_TO_OFFER": "YIELDTOOFFER",
    "MOEX_MARKETDATA_L_CLOSE_PRICE": "LCLOSEPRICE",
    "MOEX_MARKETDATA_OPEN_VALUE": "OPENVALUE",
    "MOEX_MARKETDATA_LAST_CHANGE_PRC": "LASTCHANGEPRC",
    "MOEX_MARKETDATA_MONTH_CHANGE_PRC": "MONTHCHANGEPRC",
    "MOEX_MARKETDATA_YEAR_CHANGE_PRC": "YEARCHANGEPRC",
    "MOEX_MARKETDATA_HIGH": "HIGH",
    "MOEX_MARKETDATA_LOW": "LOW",
    "MOEX_MARKETDATA_CURRENT_VALUE": "CURRENTVALUE",
    "MOEX_MARKETDATA_LAST_VALUE": "LASTVALUE",
    "MOEX_MARKETDATA_OPEN": "OPEN",
    "MOEX_MARKETDATA_VAL_TODAY": "VALTODAY",
    "MOEX_MARKETDATA_VAL_TODAY_RUR": "VALTODAY_RUR",
    "MOEX_MARKETDATA_VOL_TODAY": "VOLTODAY",
    "MOEX_SECURITIES_STEP_PRICE": "STEPPRICE",
    "MOEX_SECURITIES_MIN_STEP": "MINSTEP",
    "MOEX_SECURITIES_PREV_PRICE": "PREVPRICE",
    "MOEX_SECURITIES_PREV_LEGAL_CLOSE_PRICE": "PREVLEGALCLOSEPRICE",
    "MOEX_SECURITIES_CURRENCY_ID": "CURRENCYID",
    "MOEX_SECURITIES_LOT_SIZE": "LOTSIZE",
    "MOEX_SECURITIES_FACE_UNIT": "FACEUNIT",
    "MOEX_SECURITIES_FACE_VALUE": "FACEVALUE",
    "MOEX_SECURITIES_ACCRUED_INT": "ACCRUEDINT",
    "MOEX_SECURITIES_ANNUAL_HIGH": "ANNUALHIGH",
    "MOEX_SECURITIES_ANNUAL_LOW": "ANNUALLOW",
    "MOEX_SECURITIES_SETTLE_DATE": "SETTLEDATE",
    "TRADING_AVAILABLE_STATUS": "TRADING_AVAILABLE",
    "TRADING_NOT_AVAILABLE_STATUS": "TRADING_NOT_AVAILABLE",
    "DEFAULT_INDEXES_LOT_SIZE": -1,
    "DEFAULT_INDEXES_PRICE_STEP": -1.0,
    "RUB": "RUB"
}

MOEX_value = {
    "BondMarketData": {
        "spread": {
            "options": "required",
            "bonds": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_SPREAD"
                ]
            }
        },
        "yieldPcnt": {
            "options": "required",
            "bonds": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_YIELD"
                ]
            }
        },
        "yieldToOfferPcnt": {
            "options": "optional",
            "bonds": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_YIELD_LAST_COUPON",
                    "MOEX_MARKETDATA_YIELD_TO_OFFER"
                ],
                "comment": "marketDataYieldOfferMapper.map(marketdata, row)"
            }
        },
        "bondFaceValue": {
            "options": "required",
            "bonds": {
                "block": "securities",
                "field": [
                    "MOEX_SECURITIES_CURRENCY_ID",
                    "MOEX_SECURITIES_FACE_UNIT",
                    "MOEX_SECURITIES_FACE_VALUE"
                ],
                "map": [
                    "SUR",
                    "RUB"
                ],
                "comment": "faceValueCalc"
            }
        },
        "accruedInterest": {
            "options": "required",
            "bonds": {
                "block": "securities",
                "field": [
                    "MOEX_SECURITIES_ACCRUED_INT"
                ]
            }
        }
    },
    "IndexMarketData": {
        "open": {
            "options": "required",
            "indexes": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_OPEN_VALUE"
                ]
            }
        },
        "lastChangePct": {
            "options": "required",
            "indexes": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_LAST_CHANGE_PRC"
                ]
            }
        },
        "monthChangePct": {
            "options": "required",
            "indexes": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_MONTH_CHANGE_PRC"
                ]
            }
        },
        "yearChangePct": {
            "options": "required",
            "indexes": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_YEAR_CHANGE_PRC"
                ]
            }
        },
        "annualHigh": {
            "options": "optional",
            "indexes": {
                "block": "securities",
                "field": [
                    "MOEX_SECURITIES_ANNUAL_HIGH"
                ]
            }
        },
        "annualLow": {
            "options": "optional",
            "indexes": {
                "block": "securities",
                "field": [
                    "MOEX_SECURITIES_ANNUAL_LOW"
                ]
            }
        }
    },
    "MarketData": {
        "highBid": {
            "options": "optional",
            "bonds": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_HIGH"
                ]
            },
            "futures": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_HIGH"
                ]
            },
            "indexes": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_HIGH"
                ]
            },
            "shares": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_HIGH"
                ]
            },
            "currencies": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_HIGH"
                ]
            }
        },
        "lowAsk": {
            "options": "optional",
            "bonds": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_LOW"
                ]
            },
            "futures": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_LOW"
                ]
            },
            "indexes": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_LOW"
                ]
            },
            "shares": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_LOW"
                ]
            },
            "currencies": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_LOW"
                ]
            }
        },
        "lastPrice": {
            "options": "optional",
            "bonds": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_LAST"
                ]
            },
            "futures": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_LAST"
                ]
            },
            "indexes": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_CURRENT_VALUE"
                ]
            },
            "shares": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_LAST"
                ]
            },
            "currencies": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_LAST"
                ]
            }
        },
        "closePrice": {
            "options": "optional",
            "bonds": {
                "block": "securities",
                "field": [
                    "MOEX_SECURITIES_PREV_PRICE"
                ]
            },
            "indexes": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_LAST_VALUE"
                ]
            },
            "shares": {
                "block": "securities",
                "field": [
                    "MOEX_SECURITIES_PREV_PRICE"
                ]
            },
            "currencies": {
                "block": "securities",
                "field": [
                    "MOEX_SECURITIES_PREV_PRICE"
                ]
            }
        },
        "currency": {
            "options": "required",
            "bonds": {
                "block": "securities",
                "field": [
                    "MOEX_SECURITIES_CURRENCY_ID"
                ],
                "map": [
                    "SUR",
                    "RUB"
                ],
                "comment": "marketDataCurrencyMapper.mapCurrencyId(securities, row)"
            },
            "futures": {
                "const": "RUB"
            },
            "indexes": {
                "block": "securities",
                "field": [
                    "MOEX_SECURITIES_CURRENCY_ID"
                ],
                "map": [
                    "SUR",
                    "RUB"
                ],
                "comment": "marketDataCurrencyMapper.mapCurrencyId(securities, row)"
            },
            "shares": {
                "block": "securities",
                "field": [
                    "MOEX_SECURITIES_CURRENCY_ID"
                ],
                "map": [
                    "SUR",
                    "RUB"
                ],
                "comment": "marketDataCurrencyMapper.mapCurrencyId(securities, row)"
            },
            "currencies": {
                "block": "securities",
                "field": [
                    "MOEX_SECURITIES_CURRENCY_ID"
                ],
                "map": [
                    "SUR",
                    "RUB"
                ],
                "comment": "marketDataCurrencyMapper.mapCurrencyId(securities, row)"
            }
        },
        "exchangeTime": {
            "options": "required",
            "bonds": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_SYSTEM_TIME",
                    "MOEX_MARKETDATA_TIME"
                ],
                "comment": "marketDataExchangeTimeMapper.map(marketdata, row)"
            },
            "futures": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_SYSTEM_TIME",
                    "MOEX_MARKETDATA_TIME"
                ],
                "comment": "marketDataExchangeTimeMapper.map(marketdata, row)"
            },
            "indexes": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_SYSTEM_TIME",
                    "MOEX_MARKETDATA_TIME"
                ],
                "comment": "marketDataExchangeTimeMapper.map(marketdata, row)"
            },
            "shares": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_SYSTEM_TIME",
                    "MOEX_MARKETDATA_TIME"
                ],
                "comment": "marketDataExchangeTimeMapper.map(marketdata, row)"
            },
            "currencies": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_SYSTEM_TIME",
                    "MOEX_MARKETDATA_TIME"
                ],
                "comment": "marketDataExchangeTimeMapper.map(marketdata, row)"
            }
        },
        "tradingStatus": {
            "options": "required",
            "bonds": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_TRADING_STATUS"
                ],
                "comment": "marketDataTradingStatusMapper.map(marketdata, row)",
                "contains": {
                    "OFLDIESAab": "",
                    "T": "TRADING_AVAILABLE",
                    "__else__": "TRADING_NOT_AVAILABLE"
                }
            },
            "futures": {
                "const": "TRADING_NOT_AVAILABLE_STATUS"
            },
            "indexes": {
                "const": "TRADING_NOT_AVAILABLE_STATUS"
            },
            "shares": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_TRADING_STATUS"
                ],
                "comment": "marketDataTradingStatusMapper.map(marketdata, row)",
                "contains": {
                    "OFLDIESAab": "",
                    "T": "TRADING_AVAILABLE",
                    "__else__": "TRADING_NOT_AVAILABLE"
                }
            },
            "currencies": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_TRADING_STATUS"
                ],
                "comment": "marketDataTradingStatusMapper.map(marketdata, row)",
                "contains": {
                    "OFLDIESAab": "",
                    "T": "TRADING_AVAILABLE",
                    "__else__": "TRADING_NOT_AVAILABLE"
                }
            }
        },
        "lotSize": {
            "options": "required",
            "bonds": {
                "block": "securities",
                "field": [
                    "MOEX_SECURITIES_LOT_SIZE"
                ]
            },
            "futures": {
                "const": "1"
            },
            "indexes": {
                "const": "DEFAULT_INDEXES_LOT_SIZE"
            },
            "shares": {
                "block": "securities",
                "field": [
                    "MOEX_SECURITIES_LOT_SIZE"
                ]
            },
            "currencies": {
                "block": "securities",
                "field": [
                    "MOEX_SECURITIES_LOT_SIZE"
                ]
            }
        },
        "priceStep": {
            "options": "required",
            "bonds": {
                "block": "securities",
                "field": [
                    "MOEX_SECURITIES_MIN_STEP"
                ]
            },
            "futures": {
                "block": "securities",
                "field": [
                    "MOEX_SECURITIES_STEP_PRICE"
                ]
            },
            "indexes": {
                "const": "DEFAULT_INDEXES_PRICE_STEP"
            },
            "shares": {
                "block": "securities",
                "field": [
                    "MOEX_SECURITIES_MIN_STEP"
                ]
            },
            "currencies": {
                "block": "securities",
                "field": [
                    "MOEX_SECURITIES_MIN_STEP"
                ]
            }
        },
        "bondData": {
            "options": "optional",
            "bonds": {
                "link": "BondMarketData",
                "comment": "marketDataBondMarketDataMapper.map(marketdata, securities, row)"
            }
        },
        "instrumentId": {
            "options": "optional",
            "bonds": {
                "NONE": "None",
                "comment": "instrumentDao.getId(marketDataKey)"
            },
            "futures": {
                "NONE": "None",
                "comment": "instrumentDao.getId(marketDataKey)"
            },
            "indexes": {
                "NONE": "None",
                "comment": "instrumentDao.getId(marketDataKey)"
            },
            "shares": {
                "NONE": "None",
                "comment": "instrumentDao.getId(marketDataKey)"
            },
            "currencies": {
                "NONE": "None",
                "comment": "instrumentDao.getId(marketDataKey)"
            }
        },
        "updateTime": {
            "options": "required",
            "bonds": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_SYSTEM_TIME",
                    "MOEX_MARKETDATA_TIME"
                ],
                "comment": "marketDataUpdateTimeMapper.map(marketdata, row)"
            },
            "futures": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_SYSTEM_TIME",
                    "MOEX_MARKETDATA_TIME"
                ],
                "comment": "marketDataUpdateTimeMapper.map(marketdata, row)"
            },
            "indexes": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_SYSTEM_TIME",
                    "MOEX_MARKETDATA_TIME"
                ],
                "comment": "marketDataUpdateTimeMapper.map(marketdata, row)"
            },
            "shares": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_SYSTEM_TIME",
                    "MOEX_MARKETDATA_TIME"
                ],
                "comment": "marketDataUpdateTimeMapper.map(marketdata, row)"
            },
            "currencies": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_SYSTEM_TIME",
                    "MOEX_MARKETDATA_TIME"
                ],
                "comment": "marketDataUpdateTimeMapper.map(marketdata, row)"
            }
        },
        "lastClosePrice": {
            "options": "optional",
            "bonds": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_L_CLOSE_PRICE"
                ]
            },
            "shares": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_L_CLOSE_PRICE"
                ]
            }
        },
        "indexData": {
            "options": "optional",
            "indexes": {
                "link": "IndexMarketData",
                "comment": "toIndexMarketData(marketdata, securities, row)"
            }
        },
        "open": {
            "options": "optional",
            "bonds": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_OPEN"
                ]
            },
            "futures": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_OPEN"
                ]
            },
            "shares": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_OPEN"
                ]
            },
            "currencies": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_OPEN"
                ]
            }
        },
        "offer": {
            "options": "optional",
            "bonds": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_OFFER"
                ]
            },
            "futures": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_OFFER"
                ]
            },
            "shares": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_OFFER"
                ]
            },
            "currencies": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_OFFER"
                ]
            }
        },
        "bid": {
            "options": "optional",
            "bonds": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_BID"
                ]
            },
            "futures": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_BID"
                ]
            },
            "shares": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_BID"
                ]
            },
            "currencies": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_BID"
                ]
            }
        },
        "valToDayRur": {
            "options": "optional",
            "bonds": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_VAL_TODAY_RUR"
                ]
            },
            "futures": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_VAL_TODAY"
                ]
            },
            "shares": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_VAL_TODAY_RUR"
                ]
            },
            "currencies": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_VAL_TODAY_RUR"
                ]
            }
        },
        "volToDay": {
            "options": "optional",
            "bonds": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_VOL_TODAY"
                ]
            },
            "futures": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_VOL_TODAY"
                ]
            },
            "shares": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_VOL_TODAY"
                ]
            },
            "currencies": {
                "block": "marketdata",
                "field": [
                    "MOEX_MARKETDATA_VOL_TODAY"
                ]
            }
        },
        "settleDate": {
            "options": "optional",
            "bonds": {
                "block": "securities",
                "field": [
                    "MOEX_SECURITIES_SETTLE_DATE"
                ],
                "comment": "marketDataSettleDateMapper.map(securities, row)"
            },
            "shares": {
                "block": "securities",
                "field": [
                    "MOEX_SECURITIES_SETTLE_DATE"
                ],
                "comment": "marketDataSettleDateMapper.map(securities, row)"
            },
            "currencies": {
                "block": "securities",
                "field": [
                    "MOEX_SECURITIES_SETTLE_DATE"
                ],
                "comment": "marketDataSettleDateMapper.map(securities, row)"
            }
        }
    }
}