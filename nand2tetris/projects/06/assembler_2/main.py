from terminaltables import AsciiTable

from structuring import *
from symbols import *
import tables


table = AsciiTable(assembly_table);
print(table.table);

table_2 = AsciiTable(symbols_table);
print(table_2.table);
