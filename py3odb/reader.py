"""
A context manager that allows iteration of single execution statements.

>>> with Reader("/path/to/data.odb", "SELECT DISTINCT varno FROM <odb>") as db_reader:
>>>     for row in db_reader:
>>>         print(row)

"""
import py3odb


class Reader:  # pylint: disable=too-few-public-methods
    """Class for reading the results of a single SQL query."""
    def __init__(self, filename, sql_command):
        self._filename = filename
        self._sql_command = sql_command
        self._connection = None
        self._cursor = None
        self._description = None

    def __enter__(self):
        self._connection = py3odb.connect(self._filename)
        self._cursor = self._connection.cursor()
        self._cursor.execute(self._sql_command)
        self._description = self._cursor.description
        return self

    def __exit__(self, *args):
        self._connection.close()

    def __iter__(self):
        return self

    def __next__(self):
        row = self._cursor.fetchone()
        if row is None:
            raise StopIteration
        return row

    @property
    def description(self):
        """Returns the cursor description if available, otherwise None."""
        return self._description
