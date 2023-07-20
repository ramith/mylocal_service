from ast import literal_eval
from application.api.mylocal.models.table import Table

class TableController:
    def __init__(self, table_name):
        self.table = Table(table_name)

    def get_table(table_name):
        return Table(table_name).get_table()
    
    def get_table_row(self, row_id):
        table = self.table.get_table()
        for row in table:
            if row['entity_id'] == row_id:
                return_row = {}
                for key, value in row.items():
                    try:
                        return_row[key] = literal_eval(value)
                    except:
                        return_row[key] = value
                return {row_id: return_row}
        return None
    