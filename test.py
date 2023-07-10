import unittest
from application.api.mylocal.models.entity import Entity
from application.api.mylocal.controllers.entity_controller import EntityController
from application.api.mylocal.controllers.table_controller import TableController

class MyLocalTestCase(unittest.TestCase):
    def test_entity_get_entity_by_id(self):
        entity = Entity('LK-1127015')
        result = entity.get_entity()
        expected_value = {'id': 'LK-1127015', 'name': 'Kurunduwatta', 'country_id': 'LK', 'province_id': 'LK-1', 'district_id': 'LK-11', 'dsd_id': 'LK-1127', 'gnd_id': 'LK-1127015', 'ed_id': 'EC-01', 'pd_id': 'EC-01C', 'lg_id': 'LG-11031', 'moh_id': 'MOH-11031', 'population': 9865, 'area': 3.62, 'gnd_num': None, 'subs': [], 'supers': ['EC-01C'], 'eqs': [], 'ints': [], 'centroid': [6.910336261080488, 79.86693203376326], 'centroid_altitude': 17}
        self.assertEqual(result, expected_value)

    def test_entity_controller_get_entity(self):
        result = EntityController.get_entity('LK-1127015')
        expected_value = {'id': 'LK-1127015', 'name': 'Kurunduwatta', 'country_id': 'LK', 'province_id': 'LK-1', 'district_id': 'LK-11', 'dsd_id': 'LK-1127', 'gnd_id': 'LK-1127015', 'ed_id': 'EC-01', 'pd_id': 'EC-01C', 'lg_id': 'LG-11031', 'moh_id': 'MOH-11031', 'population': 9865, 'area': 3.62, 'gnd_num': None, 'subs': [], 'supers': ['EC-01C'], 'eqs': [], 'ints': [], 'centroid': [6.910336261080488, 79.86693203376326], 'centroid_altitude': 17}
        self.assertEqual(result, expected_value)

    def test_entity_controller_get_entities(self):
        result = EntityController.get_entities('LK-1;LK-2;LK-3')
        expected_value = {'LK-1': {'id': 'LK-1', 'name': 'Western', 'country_id': 'LK', 'province_id': 'LK-1', 'area': 3709.0, 'population': 5850745, 'province_capital': 'Colombo', 'fips': 'CE36', 'subs': ['EC-01', 'EC-02', 'EC-03', 'LK-11', 'LK-12', 'LK-13'], 'supers': [], 'eqs': [], 'ints': [], 'centroid': [6.83475266513655, 80.06699098051703], 'centroid_altitude': 65}, 'LK-2': {'id': 'LK-2', 'name': 'Central', 'country_id': 'LK', 'province_id': 'LK-2', 'area': 5584.0, 'population': 2571557, 'province_capital': 'Kandy', 'fips': 'CE29', 'subs': ['EC-04', 'EC-05', 'EC-06', 'LK-21', 'LK-22', 'LK-23'], 'supers': [], 'eqs': [], 'ints': [], 'centroid': [7.3240253926618895, 80.71779633296414], 'centroid_altitude': 707}, 'LK-3': {'id': 'LK-3', 'name': 'Southern', 'country_id': 'LK', 'province_id': 'LK-3', 'area': 5559.0, 'population': 2477285, 'province_capital': 'Galle', 'fips': 'CE34', 'subs': ['EC-07', 'EC-08', 'EC-09', 'LK-31', 'LK-32', 'LK-33'], 'supers': [], 'eqs': [], 'ints': [], 'centroid': [6.2214499262787095, 80.7207042920801], 'centroid_altitude': 127}}
        self.assertEqual(result, expected_value)

    def test_table_controller_get_table_row(self):
        table_controller = TableController('education-educational-attainment.regions.2012')
        result = table_controller.get_table_row('LK-1127015')
        expected_value = {'LK-1127015': {'entity_id': 'LK-1127015', 'primary': 1025, 'secondary': 2081, 'gce_ordinary_level': 1473, 'gce_advanced_level': 3224, 'degree_and_above': 1534, 'no_schooling': 238, 'region_id': 0}}
        self.assertEqual(result, expected_value)

    def test_entity_controller_get_coordinates(self):
        result = EntityController.get_coordinates('LK-1127015')
        expected_value = {'coordinates': [[[[79.87138657373175, 6.921171695156659], [79.87397938938172, 6.918429502973021], [79.87515794194988, 6.9172542777514625], [79.87492223143624, 6.916862536010943], [79.87468652092262, 6.916862536010943], [79.87468652092262, 6.916079052529904], [79.87468652092262, 6.915687310789384], [79.87397938938172, 6.915687310789384], [79.87421509989535, 6.915295569048864], [79.87445081040899, 6.914903827308345], [79.87515794194988, 6.913336860346266], [79.87586507349079, 6.911769893384188], [79.87633649451804, 6.910986409903148], [79.87680791554531, 6.910986409903148], [79.87704362605895, 6.910986409903148], [79.87727933657258, 6.910986409903148], [79.8775150470862, 6.910986409903148], [79.8775150470862, 6.910202926422109], [79.8775150470862, 6.90941944294107], [79.8775150470862, 6.90902770120055], [79.8775150470862, 6.908244217719511], [79.87727933657258, 6.90902770120055], [79.87704362605895, 6.90902770120055], [79.87562936297715, 6.907852475978991], [79.87421509989535, 6.906677250757433], [79.87303654732719, 6.905110283795354], [79.87091515270448, 6.903151575092756], [79.86997231064996, 6.9023680916117165], [79.86902946859543, 6.901584608130677], [79.86690807397272, 6.900409382909118], [79.86620094243183, 6.900409382909118], [79.86549381089092, 6.899625899428079], [79.86407954780913, 6.89923415768756], [79.86195815318644, 6.898058932466], [79.86054389010464, 6.897275448984962], [79.86077960061827, 6.89845067420652], [79.86077960061827, 6.89884241594704], [79.860308179591, 6.89923415768756], [79.85983675856373, 6.900409382909118], [79.85960104805011, 6.901584608130677], [79.85936533753647, 6.902759833352236], [79.8588939165092, 6.903935058573795], [79.8588939165092, 6.904718542054834], [79.8588939165092, 6.905502025535873], [79.85912962702284, 6.906285509016913], [79.85912962702284, 6.906677250757433], [79.85818678496831, 6.908635959460031], [79.85700823240015, 6.910986409903148], [79.85630110085924, 6.912161635124708], [79.85630110085924, 6.912553376865227], [79.8560653903456, 6.912945118605746], [79.85653681137288, 6.912945118605746], [79.85724394291377, 6.913336860346266], [79.85936533753647, 6.914120343827306], [79.86195815318644, 6.915687310789384], [79.86431525832276, 6.9172542777514625], [79.8645509688364, 6.9172542777514625], [79.86478667935003, 6.917646019491983], [79.86502238986367, 6.917646019491983], [79.86502238986367, 6.918037761232502], [79.86478667935003, 6.919212986454061], [79.86643665294547, 6.9199964699351], [79.86832233705452, 6.921171695156659], [79.86902946859543, 6.921563436897179], [79.8687937580818, 6.921955178637698], [79.8687937580818, 6.922346920378218], [79.86855804756816, 6.922346920378218], [79.8687937580818, 6.9227386621187375], [79.86902946859543, 6.9227386621187375], [79.86973660013632, 6.923130403859258], [79.86997231064996, 6.9227386621187375], [79.87138657373175, 6.921171695156659]]]], 'type': 'MultiPolygon'}
        self.assertEqual(result, expected_value)

    def test_entity_get_id(self):
        entity = Entity(coordinates=[6.9157, 79.8636], type='gnd')
        result = entity.get_id()
        expected_value = "LK-1127015"
        self.assertEqual(result, expected_value)

    def test_entity_controller_get_entity_ids_by_coordinates(self):
        result = EntityController.get_entity_ids_by_coordinates('6.9157,79.8636')
        expected_value = {'province': 'LK-1', 'district': 'LK-11', 'dsd': 'LK-1127', 'gnd': 'LK-1127015'}
        self.assertEqual(result, expected_value)

if __name__ == '__main__':

    unittest.main()
