# Some helper functions.
# You should not need to edit this file.

import ujson
import fileinput

from pymongo import connection

from settings import settings


def read_json():
    for line in fileinput.input():
        yield ujson.loads(line)

def connect_db(dbname, remove_existing=False):
    con = connection.Connection(settings['mongo_host'],settings['mongo_port'])
    if remove_existing:
        con.drop_database(dbname)
    return con[dbname]


