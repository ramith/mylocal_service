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
                for key, value in row.items():
                    try:
                        row[key] = int(value)
                    except ValueError:
                        try:
                            row[key] = float(value)
                        except ValueError:
                            pass
                return {row['entity_id']: row}
        return None