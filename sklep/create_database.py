from sklep.sql_tools import execute_query
from sklep.model import User_, Product, ItemInCart, Cart

models = [
    User_, Product, Cart, ItemInCart
]

for model in models:
    try:
        execute_query(model.create_table())
    except Exception as e:
        print(e)


