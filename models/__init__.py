#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv


"""
This condition act like a 'switch' that allow us to change
storage type directly by using environment variable
"""
if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
