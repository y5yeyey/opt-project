# -*- coding: utf-8 -*-

from db_client import *

test = {
    "HOST": "localhost",
    "DB": "talkingdata",
    "USER": "root",
    "PWD": ""
}

conn, cr = mysql_client(test)
with mysql_data(conn, cr):
    sql = "select * from events limit 10;"
    cr.execute(sql)
    for line in fetch_all(cr):
        print line