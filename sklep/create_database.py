from sklep.sql_tools import execute_query
from model import User

execute_query(User.create_table())

