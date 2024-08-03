from psycopg2 import connect
from settings import database_settings
from sklep.sql_tools import execute_query


class User:

    def __init__(self, id=None, first_name=None,
                 last_name=None, username=None, password=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    def save(self):
        query = f"""
        INSERT INTO user_(first_name, last_name, username, password2) VALUES
        ('{self.first_name}', '{self.last_name}', '{self.username}', '{self.password}')
        returning id;
        """
        id = execute_query(query)
        self.id = id[0][0]
        print(self.id)

    @classmethod
    def get_user(cls, id):
        query = f"""
        select * from user_ where id={id};"""
        user_row = execute_query(query)[0]
        u = User(*user_row)
        return u

    @classmethod
    def get_users(cls):
        query = f"""
                select * from user_;"""
        user_rows = execute_query(query)
        users = []
        for row in user_rows:
            users.append(User(*row))
        return users



    @classmethod
    def create_table(cls):
        query = """
        create table user_(
            id serial primary key, 
            first_name  varchar(20),
            last_name  varchar(20),
            username  varchar(20),
            password2  varchar(20)
        );
        """
        return query

    def __str__(self):
        return f"{self.id} {self.first_name} {self.last_name} {self.username} {self.password}"
#
#

#
if __name__ == "__main__":
    users = User.get_users()
    for u in users:
        print(u)
