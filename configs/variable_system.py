KEY_RSA = 'duanfpro'

U = 'username'
P = 'password'

TOKEN = {
    'private_key':'anphMNcZkh',
    'public_key':'fnEcdMHkm',
    'type':'Bearer ',
    'hash':'HS256',
    'tls_access_token':60*60,
    'tls_refresh_token':60*60*3
}

GROUP_URL = {
    'url_auth',
    'url_post',
}

THROTTLING = {
        'rate': '1',
        'split': '/',
        'per_time': '3s',
        'method': [
            'GET'
        ],
}

DATABASE_TB = {
    'HERO_TB': 'hero'
}

DETAIL_HERO = {
    'id': 'Code',
    'name': 'Name',
    'power': 'Power'
}