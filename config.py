load_data = {
    'config': {
        'bonds': {
            'engine': 'stock',
            'market': ['ndm', 'bonds'],
        },
        'indexes': {
            'engine': 'stock',
            'market': ['index'],
        },
        'currencies': {
            'engine': 'currency',
            'market': ['selt'],
        },
        'shares': {
            'engine': 'stock',
            'market': ['shares', 'foreignshares'],
        },
        'futures': {
            'engine': 'futures',
            'market': ['forts'],
        },
    },
    'url': {
        'data': 'https://iss.moex.com/iss/engines/<engine>/markets/<market>/securities.json',
        'metadata': 'https://iss.moex.com/iss/engines/<engine>/markets/<market>/securities/columns.json',
    },
}
