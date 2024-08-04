from sklep.sql_tools import execute_query


class DatabaseEntity:
    columns = {}
    apostrof_types = [
        'varchar', 'text', 'timestamp', 'date'
    ]

    @classmethod
    def _get_columns_name(cls):
        return cls.columns.keys()

    def get_values_for_create(self):
        values = [str(self.get_sql_value(column_name)) for column_name in self._get_columns_name()]
        return values

    def get_sql_value(self, column_name):
        value = getattr(self, column_name)
        type = self.columns[column_name].split("(")[0]
        if type in self.apostrof_types:
            return f"'{value}'"
        return value

    def save(self):
        if self.id is None:
            self._create()
        else:
            self._update()

    def _update(self):
        pass

    def _create(self):
        query = f"""INSERT INTO {self._get_table_name()}({",".join(self._get_columns_name())}) VALUES
                ({','.join(self.get_values_for_create())})
                returning id;
                """
        id = execute_query(query)
        self.id = id[0][0]

    def _update(self):
        data = [f"{column_name}={self.get_sql_value(column_name)}" for column_name in self._get_columns_name()]

        query = f"""
            UPDATE user_ SET
            {','.join(data)}
            WHERE id={self.id}
        """
        execute_query(
            query
        )

    @classmethod
    def _get_table_name(cls):
        return cls.__name__.lower()

    @classmethod
    def all(cls):
        query = f"SELECT * FROM {cls._get_table_name()}"
        rows = execute_query(query)
        objects = []
        for row in rows:
            objects.append(cls(*row))
        return objects

    @classmethod
    def get(cls, id):
        query = f"SELECT * FROM {cls._get_table_name()} WHERE id={id}"
        row = execute_query(query)[0]
        object = cls(*row)
        return object

    @classmethod
    def create_table(cls):
        data = [f"{column_name} {type}" for column_name, type in cls.columns.items()]
        query = f"""
            create table {cls._get_table_name()}(
                id serial primary key, 
                {','.join(data)}
            );
            """
        return query


class User_(DatabaseEntity):
    columns = {
        'first_name': 'varchar(120)',
        'last_name': 'varchar(120)',
        'username': 'varchar(120)',
        'password': 'varchar(120)'
    }

    def __init__(self, id=None, first_name=None,
                 last_name=None, username=None, password=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password


class Product(DatabaseEntity):
    columns = {
        "name": 'varchar(50)',
        'price': 'float'
    }

    def __init__(self, id=None, name=None, price=None):
        self.id = id
        self.name = name
        self.price = price


class Cart(DatabaseEntity):
    columns = {
        'user_id': 'INTEGER'
    }

    def __int__(self, id=None, user=None):
        self.id = id
        self.user = user
        self.user_id = None
        if self.user is not None:
            self.user_id = self.user.id




class ItemInCart(DatabaseEntity):
    columns = {
        'cart_id': 'INTEGER',
        'product_id': 'INTEGER'
    }
    def __int__(self, id=None, cart=None, product=None):
        self.id = id
        self.cart = cart
        self.cart_id = None
        if self.cart is not None:
            self.cart_id = self.cart.id
        self.product = product
        self.product_id = None
        if self.product is not None:
            self.product_id = self.product.id


#

#
if __name__ == "__main__":
    # u = User_(first_name='Sławek', last_name='bogusławski', username='cooklee', password='qwerty')
    p = Product(name='cebula', price=5.34)
    p.save()
