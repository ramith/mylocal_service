from flask import Blueprint, Response
import json
from utils.Log import Log
from application.api.mylocal.controllers.entity_controller import EntityController
from application.api.mylocal.controllers.table_controller import TableController
from concurrent.futures import ThreadPoolExecutor

bp = Blueprint('mylocal', __name__)
log = Log('mylocal')


@bp.route('/')
def index():
    """Index."""
    return f"""mylocal_service Running.!
     <a href="https://app.swaggerhub.com/apis-docs/LAKINDUOSHADHA98_1/mylocal-service_backend_for_mylocal/1.0.0">
     API Documentation</a>"""

@bp.route('/entities/<string:entity_ids_str>', methods=['GET'])
def entity(entity_ids_str):
    """
    - Parameters:
        - entity_ids_str (str): A string containing entity IDs separated by semicolons.
    - Returns: JSON response containing entity information for each entity ID.
    """    
    log.info(f'/entities/ entity_ids: {entity_ids_str}')

    try: 
        entity_map = EntityController.get_entities(entity_ids_str)
        return Response(json.dumps(entity_map), mimetype='application/json')
    except:
        log.warning(f'/entities/ entity_ids: {entity_ids_str} - Invalid entity ID')
        return Response(json.dumps({'error': 'Invalid entity ID'}), mimetype='application/json', status=400)


@bp.route('/census/<string:table_name>/<string:entity_id>', methods=['GET'])
def census(table_name,entity_id):
    """
    - Parameters:
        - table_name (str): A string representing the table name.
        - entity_id (str): A string representing the entity ID.
    - Returns: JSON response containing census information for the specified entity ID.
    """
    log.info(f'/census/ table_name: {table_name}, entity_id: {entity_id}')

    try:
        census = TableController(table_name).get_table_row(entity_id)
        return Response(json.dumps(census) ,mimetype='application/json')
    except:
        log.warning(f'/census/ table_name: {table_name}, entity_id: {entity_id} - Invalid table name or entity ID')
        return Response(json.dumps({'error': 'Invalid table name or entity ID'}), mimetype='application/json', status=400)

@bp.route('/entity/coordinates/<string:entity_id>', methods=['GET'])
def geo(entity_id):
    """
    - Parameters:
        - region_id (str): A string representing the region ID.
    - Returns: JSON response containing geo information for the specified region ID.
    """    
    log.info(f'/entity/coordinates/ entity_id: {entity_id}')

    try:
        coordinates = EntityController.get_coordinates(entity_id)
        return Response(json.dumps(coordinates), mimetype='application/json')
    except:
        log.warning(f'/entity/coordinates/ entity_id: {entity_id} - Invalid entity ID')
        return Response(json.dumps({'error': 'Invalid entity ID'}), mimetype='application/json', status=400)

@bp.route('/regions/<string:latlng_str>', methods=['GET'])
def regions(latlng_str):
    """
    - Parameters:
        - latlng_str (str): latitude,longitude
    - Returns: JSON response containing region IDs for the specified coordinates.
    """
    log.info(f'/regions/ latlng_str: {latlng_str}')

    try:
        regions = EntityController.get_entity_ids_by_coordinates(latlng_str)
        return Response(json.dumps(regions), mimetype='application/json')
    except:
        log.warning(f'/regions/ latlng_str: {latlng_str} - Invalid coordinates')
        return Response(json.dumps({'error': 'Invalid coordinates'}), mimetype='application/json', status=400)
    

def _warmup():
    """Warmup function."""
    print('Warming up mylocal service...')
    
    # Execute EntityController.get_entities outside of parallel execution
    EntityController.get_entities('LK;LK-1127015;LK-11;LK-1;LK-1127;EC-01;EC-01C;LG-11031;MOH-11031')
    
    with ThreadPoolExecutor() as executor:
        futures = []
        
        # List of table names to be processed in parallel
        table_names = [
            'population-gender.regions.2012',
            'population-age_group.regions.2012',
            'population-marital_status.regions.2012',
            'population-ethnicity.regions.2012',
            'population-religion.regions.2012',
            'social-household-lighting.regions.2012',
            'social-household-cooking_fuel.regions.2012',
            'social-household-source_of_drinking_water.regions.2012',
            'social-household-solid_waste_disposal.regions.2012',
            'social-household-toilet_facilities.regions.2012',
            'social-household-roof_type.regions.2012',
            'social-household-floor_type.regions.2012',
            'social-household-wall_type.regions.2012',
            'social-household-structure.regions.2012',
            'social-household-living_quarters.regions.2012',
            'social-household-type_of_unit.regions.2012',
            'social-household-occupation_status.regions.2012',
            'social-household-year_of_construction.regions.2012',
            'social-household-number_of_rooms.regions.2012',
            'social-household-number_of_persons.regions.2012',
            'social-household-relationship_to_head.regions.2012',
            'social-household-number-of-households.regions.2012',
            'social-household-ownership-status.regions.2012'
        ]
        
        # Submit TableController tasks to the executor
        for table_name in table_names:
            futures.append(executor.submit(TableController(table_name).get_table_row, 'LK-1127015'))
        
        # Wait for all TableController futures to complete
        for future in futures:
            try:
                future.result()
            except Exception as e:
                log.debug(f"Exception occurred: {e}")

    # Execute EntityController.get_entity_ids_by_coordinates outside of parallel execution
    EntityController.get_entity_ids_by_coordinates('6.9157,79.8636')
    
    log.debug("Warming up entity coordinates in parallel...")
    
    # Run EntityController.get_coordinates in parallel
    with ThreadPoolExecutor() as executor:
        futures = []
        for entity_id in EntityController.get_entity_ids():
            futures.append(executor.submit(EntityController.get_coordinates, entity_id))
        
        # Wait for all EntityController.get_coordinates futures to complete
        for future in futures:
            try:
                future.result()
            except Exception as e:
                log.debug(f"Exception occurred: {e}")

    print('mylocal service warmup complete.!')
