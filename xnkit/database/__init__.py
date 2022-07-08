from xnkit.database.postgres.afk_sql import AFKSQL
from xnkit.database.postgres.dv_sql import DVSQL
from xnkit.database.postgres.filters_sql import FILTERSSQL
from xnkit.database.postgres.notes_sql import NOTESSQL
from xnkit.database.postgres.pmpermit_sql import PMPERMITSQL
from xnkit.database.postgres.welcome_sql import WELCOMESQL


class Database(AFKSQL, NOTESSQL, PMPERMITSQL, DVSQL, WELCOMESQL, FILTERSSQL):
    pass
