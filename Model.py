from peewee import Model, MySQLDatabase, CharField, AutoField
from configparser import ConfigParser

config = ConfigParser()
config.read('db.ini')
db = MySQLDatabase(config['DataBase']['name'], user=config['DataBase']['user'], password=config['DataBase']['pass'], host=config['DataBase']['host'], port=config.getint('DataBase','port'))

class Shirt(Model):
    id = AutoField(primary_key=True)
    color = CharField()
    design = CharField()

    class Meta:
        database = db