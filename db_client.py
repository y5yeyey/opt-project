# -*- coding: utf-8 -*-

import MySQLdb

def mysql_client(db_config):
    conn = MySQLdb.connect(
        host=db_config["HOST"],
        user=db_config["USER"],
        passwd=db_config["PWD"],
        db=db_config["DB"],
    )
    cr = conn.cursor()
    return conn, cr

class mysql_data(object):
    def __init__(self, conn, cr):
        self.conn = conn
        self.cr = cr
    def __enter__(self):
        return self.cr
    def __exit__(self, type, value, traceback):
        self.cr.close()
        del self.cr
        self.conn.close()

def fetch_all(cr):
    return [dict(zip(zip(*cr.description)[0], row)) for row in cr.fetchall()]

