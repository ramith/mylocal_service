from application.api.mylocal.models.entity import Entity
from application.api.mylocal.models.table import Table
from application.api.mylocal.controllers.entity_controller import EntityController
from application.api.mylocal.controllers.table_controller import TableController
# from application.api.mylocal.models.

if __name__ == '__main__':
    entity = Entity('LK-1127015')
    print(entity.get_entity())

    table = Table('economy-economic-activity.regions.2012')
    print(table.get_table())

    print(EntityController.get_entity('LK-1127015'))

    print(EntityController.get_entities('LK-1;LK-2;LK-3'))

    print(TableController('education-educational-attainment.regions.2012').get_table_row('LK-1127015'))

    print(EntityController.get_coordinates('LK-11'))

    entity = Entity(coordinates=[6.9157,79.8636], type='gnd') 
    print(entity.get_id())

    print(EntityController.get_entity_ids_by_coordinates('6.9157,79.8636', 'gnd'))
