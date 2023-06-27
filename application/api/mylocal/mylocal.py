from flask import Blueprint, Response
from application.api.mylocal.gig.Ent import Ent
from application.api.mylocal.gig.GIGTable import GIGTable
import json

bp = Blueprint('mylocal', __name__)

@bp.route('/')
def index():
    """Index."""
    data = 'mylocal_service Running.!'
    return data

@bp.route('/entities/<string:entity_ids_str>')
def entity(entity_ids_str):
    """
    - Parameters:
        - entity_ids_str (str): A string containing entity IDs separated by semicolons.
    - Returns: JSON response containing entity information for each entity ID.
    """
    print('/entities/ entity_ids: ', entity_ids_str)
    entity_ids = entity_ids_str.split(';')

    entity_map = {}
    for entity_id in entity_ids:
        entity_map[entity_id] = json.loads(Ent.from_id(entity_id).to_json())
        
    return Response(json.dumps(entity_map), mimetype='application/json')


@bp.route('/census/<string:table_name>/<string:entity_id>')
def census(table_name,entity_id):
    """
    - Parameters:
        - table_name (str): A string representing the table name.
        - entity_id (str): A string representing the entity ID.
    - Returns: JSON response containing census information for the specified entity ID.
    """
    print('/census/ table_name: ', table_name, 'entity_id: ', entity_id)
    try:
        table_name_arr = table_name.split('.')
        measurement = table_name_arr[0]
        ent_type_group = table_name_arr[1]
        time_group = table_name_arr[2]
    except:
        return Response(json.dumps('Invalid table name'), mimetype='application/json', status=400)
    
    gig_table = GIGTable(measurement, ent_type_group, time_group)
    entity = Ent.from_id(entity_id)
    census = entity.gig(gig_table)
    
    return Response(census.to_json() ,mimetype='application/json')

@bp.route('/entity/coordinates/<string:region_id>')
def geo(region_id):
    """
    - Parameters:
        - region_id (str): A string representing the region ID.
    - Returns: JSON response containing geo information for the specified region ID.
    """
    print('/entity/coordinates/ region_id: ', region_id)
    return Response(json.dumps(Ent.geo(region_id)), mimetype='application/json')


@bp.route('/regions/<string:latlng_str>')
def latlng_to_region(latlng_str):
    """
    - Parameters:
        - latlng_str (str): latitude,longitude
    - Returns: JSON response containing region IDs for the specified coordinates.
    """
    print('/regions/ latlng_str: ', latlng_str)
    return Response(json.dumps(Ent.latlng_to_region(latlng_str)), mimetype='application/json')
