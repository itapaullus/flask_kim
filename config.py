CSRF_ENABLED = True
SECRET_KEY = '1jUiNoVKUX4VS!psWQ&P*pvY2rU!ejdDMKxg2G93P2$^2rg'
OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ewwpaullus_kim:pRat92Cas11@pg2.sweb.ru/ewwpaullus_kim'
