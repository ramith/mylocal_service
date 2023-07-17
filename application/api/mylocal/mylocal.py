from flask import Blueprint, Response
import json
from application.api.mylocal.controllers.entity_controller import EntityController
from application.api.mylocal.controllers.table_controller import TableController
bp = Blueprint('mylocal', __name__)

@bp.route('/')
def index():
    """Index."""
    data = 'mylocal_service Running.!'
    return data

@bp.route('/entities/<string:entity_ids_str>', methods=['GET'])
def entity(entity_ids_str):
    """
    - Parameters:
        - entity_ids_str (str): A string containing entity IDs separated by semicolons.
    - Returns: JSON response containing entity information for each entity ID.
    """
    print('/entities/ entity_ids: ', entity_ids_str)

    entity_map = EntityController.get_entities(entity_ids_str)
    return Response(json.dumps(entity_map), mimetype='application/json')


@bp.route('/census/<string:table_name>/<string:entity_id>', methods=['GET'])
def census(table_name,entity_id):
    """
    - Parameters:
        - table_name (str): A string representing the table name.
        - entity_id (str): A string representing the entity ID.
    - Returns: JSON response containing census information for the specified entity ID.
    """
    print('/census/ table_name: ', table_name, 'entity_id: ', entity_id)

    census = TableController(table_name).get_table_row(entity_id)
    return Response(json.dumps(census) ,mimetype='application/json')

@bp.route('/entity/coordinates/<string:entity_id>', methods=['GET'])
def geo(entity_id):
    """
    - Parameters:
        - region_id (str): A string representing the region ID.
    - Returns: JSON response containing geo information for the specified region ID.
    """
    print('/entity/coordinates/ entity_id: ', entity_id)
    coordinates = EntityController.get_coordinates(entity_id)

    return Response(json.dumps(coordinates), mimetype='application/json') 

@bp.route('/regions/<string:latlng_str>', methods=['GET'])
def regions(latlng_str):
    """
    - Parameters:
        - latlng_str (str): latitude,longitude
    - Returns: JSON response containing region IDs for the specified coordinates.
    """
    print('/regions/ latlng_str: ', latlng_str)
    regions = EntityController.get_entity_ids_by_coordinates(latlng_str)

    return Response(json.dumps(regions), mimetype='application/json')

def _warmup():
    """Warmup function."""
    print('Warming up mylocal service...')
    
    EntityController.get_entities('LK-1127015;LK-11;LK-1;LK-1127;EC-01;EC-01C;LG-11031;MOH-11031')
    TableController('population-gender.regions.2012').get_table_row('LK-1127015')
    TableController('population-age_group.regions.2012').get_table_row('LK-1127015')
    TableController('population-marital_status.regions.2012').get_table_row('LK-1127015')
    TableController('population-ethnicity.regions.2012').get_table_row('LK-1127015')
    TableController('population-religion.regions.2012').get_table_row('LK-1127015')
    TableController('social-household-lighting.regions.2012').get_table_row('LK-1127015')
    TableController('social-household-cooking_fuel.regions.2012').get_table_row('LK-1127015')
    TableController('social-household-source_of_drinking_water.regions.2012').get_table_row('LK-1127015')
    TableController('social-household-solid_waste_disposal.regions.2012').get_table_row('LK-1127015')
    TableController('social-household-toilet_facilities.regions.2012').get_table_row('LK-1127015')
    TableController('social-household-roof_type.regions.2012').get_table_row('LK-1127015')
    TableController('social-household-floor_type.regions.2012').get_table_row('LK-1127015')
    TableController('social-household-wall_type.regions.2012').get_table_row('LK-1127015')
    TableController('social-household-structure.regions.2012').get_table_row('LK-1127015')
    TableController('social-household-living_quarters.regions.2012').get_table_row('LK-1127015')
    TableController('social-household-type_of_unit.regions.2012').get_table_row('LK-1127015')
    TableController('social-household-occupation_status.regions.2012').get_table_row('LK-1127015')
    TableController('social-household-year_of_construction.regions.2012').get_table_row('LK-1127015')
    TableController('social-household-number_of_rooms.regions.2012').get_table_row('LK-1127015')
    TableController('social-household-number_of_persons.regions.2012').get_table_row('LK-1127015')
    TableController('social-household-relationship_to_head.regions.2012').get_table_row('LK-1127015')
    TableController('social-household-number-of-households.regions.2012').get_table_row('LK-1127015')
    TableController('social-household-ownership-status.regions.2012').get_table_row('LK-1127015')
    EntityController.get_entity_ids_by_coordinates('6.9157,79.8636')

    for entity_id in EntityController.get_entity_ids():
        try:
            EntityController.get_coordinates(entity_id)
        except:
            pass

    print('mylocal service warmup complete.!')
