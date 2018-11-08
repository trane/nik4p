import os
import psycopg2
from psycopg2.extensions import parse_dsn

dsn = os.environ['DATABASE_URI']
connect_dict = parse_dsn(dsn)
con = psycopg2.connect(**connect_dic)
cur = con.cursor()
cur.execute("select * from users limit 1")
cur.fetchone()
