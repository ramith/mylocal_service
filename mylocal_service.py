from waitress import serve
from application.factory import create_app
from config import API_HOST,API_PORT
from flask_cors import CORS
from flask_caching import Cache

app = create_app()
CORS(app)
cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
cache.init_app(app)

if __name__ == '__main__':
    print('Starting mylocal_service on ', API_HOST, ':', API_PORT)
    serve(app, 
          host= API_HOST,
          port = API_PORT,
          threads = 8)
    