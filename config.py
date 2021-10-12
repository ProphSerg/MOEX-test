load_data = {
    'config': {
        'bonds': {
            'engine': 'stock',
            'market': ['ndm', 'bonds'],
            'ISS': ['MarketData', 'BondMarketData'],
            'ASTS': {
                'market': 'Equities',
                'tables': ['SECURITIES'],
            }
        },
        'indexes': {
            'engine': 'stock',
            'market': ['index'],
            'ISS': ['MarketData', 'IndexMarketData'],
            'ASTS': {
                'market': 'Equities',
                'tables': ['SECURITIES', 'INDEXES'],
            }
        },
        'currencies': {
            'engine': 'currency',
            'market': ['selt'],
            'ISS': ['MarketData'],
            'ASTS': {
                'market': 'Currency',
                'tables': ['SECURITIES'],
            }
        },
        'shares': {
            'engine': 'stock',
            'market': ['shares', 'foreignshares'],
            'ISS': ['MarketData'],
            'ASTS': {
                'market': 'Equities',
                'tables': ['SECURITIES'],
            }
        },
        'futures': {
            'engine': 'futures',
            'market': ['forts'],
            'ISS': ['MarketData'],
            'ASTS': {
                'market': 'Equities',
                'tables': ['SECURITIES'],
            }
        },
    },
    'url': {
        'data': 'https://iss.moex.com/iss/engines/<engine>/markets/<market>/securities.json',
        'metadata': 'https://iss.moex.com/iss/engines/<engine>/markets/<market>/securities/columns.json',
    },
}
