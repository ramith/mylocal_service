import os
from dotenv import load_dotenv

load_dotenv()
ENTS_BASE_URL = os.getenv('ENTS_BASE_URL')
CENSUS_BASE_URL = os.getenv('CENSUS_BASE_URL')


API_HOST = os.getenv('API_HOST')
API_PORT = os.getenv('API_PORT')
