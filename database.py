from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import urllib.parse


SQLALCHEMY_DATABASE_URL = "mysql+pymysql://<<user>>:<<password>>@localhost/<<db_name>>"
print('SQLALCHEMY_DATABASE_URL:11111 ', SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
