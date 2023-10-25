from pathlib import Path
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import text, create_engine


def get_engine():
    url = f"postgresql://postgres:62A+6aBa+5c-eDA+3FD3dd4-*A+1c1ad@roundhouse.proxy.rlwy.net:20013/railway"
    engine = create_engine(url, pool_size=50, echo=False)
    return engine


eng = get_engine()


Session = sessionmaker(bind=eng)
session = Session()


def create_table():
    with eng.connect() as conn:
        conn.execute(text("""                        
CREATE TABLE rfid (
    dob  TIMESTAMP,
    uid VARCHAR(16),
    type VARCHAR (50)
);
        """))


def insert_table():
    with eng.connect() as conn:
        conn.execute(text("""                        
INSERT INTO rfid(dob, uid, type) VALUES
('1999-01-08 4:05:06', '3D 75 8N 34', 'M300');
        """))


def read_table():
    with eng.connect() as conn:
        dis = conn.execute(text("""                        
SELECT * FROM rfid
        """)).mappings()
        for k in dis:
            print(k)


create_table()
#insert_table()
#read_table()




