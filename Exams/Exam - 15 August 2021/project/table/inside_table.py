from project.table.table import Table


class InsideTable(Table):
    _TABLE_NUMBERS = range(1, 51)

    @property
    def table_number(self):
        return self._table_number

    @table_number.setter
    def table_number(self, value: int):
        if value not in self._TABLE_NUMBERS:
            raise ValueError("Inside table's number must be between 1 and 50 inclusive!")

        self._table_number = value
