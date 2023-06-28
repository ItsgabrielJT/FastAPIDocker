from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import metadata, engine

users = Table("users", metadata, 
    Column("id", Integer, primary_key=True), 
    Column("name", String(255)), 
    Column("email", String(200)),
    Column("password", String(200)),
    )

metadata.create_all(engine)