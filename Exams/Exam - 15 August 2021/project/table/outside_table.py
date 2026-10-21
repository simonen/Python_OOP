from project.table.table import Table


class OutsideTable(Table):
    _TABLE_NUMBERS = range(51, 101)

    @property
    def table_number(self):
        return self._table_number

    @table_number.setter
    def table_number(self, value: int):
        if value not in self._TABLE_NUMBERS:
            raise ValueError("Outside table's number must be between 51 and 100 inclusive!")

        self._table_number = value