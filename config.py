from dotenv import load_dotenv
import os

load_dotenv()

class Config(object):
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=os.getenv('DBUSERPROD')+ "@jseijas-dbsrv",
    dbpass=os.getenv('DBPASSPROD'),
    dbhost=os.getenv('DBHOSTPROD') + ".postgres.database.azure.com",
    dbname=os.getenv('DBNAMEPROD')
    
    )

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://{dbuser}:{dbpass}@{dbhost}:{dbport}/{dbname}'.format(
    dbuser=os.getenv('DBUSER'),
    dbpass=os.getenv('DBPASS'),
    dbhost=os.getenv('DBHOST'),
    dbname=os.getenv('DBNAME'),
    dbport=os.getenv('DBPORT')
    )
    DEBUG = True
    

class GithubCIConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    DEBUG = True