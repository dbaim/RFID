from pathlib import Path
import psycopg2


con = psycopg2.connect(
    database="railway",
    user="postgres",
    password="-dc5EgDg15dbb4Egg+*fD*EbEE6cGC6G",
    host = "monorail.proxy.rlwy.net",
    port="58167"
)

cursor_obj = con.cursor()
cursor_obj.execute("""
CREATE TABLE rfid (
    dob  TIMESTAMP,
    uid VARCHAR(16),
    type VARCHAR (50)
);
                   """)


cursor_obj.execute("""
INSERT INTO rfid(dob, uid, type) VALUES
    ('1999-01-08 4:05:06', '3D 75 8N 34', 'M300');
            """)


# def create_table():
#     with eng.connect() as conn:
#         conn.execute(text("""                        
# CREATE TABLE rfid_uhf (
#     dob  TIMESTAMP,
#     uid VARCHAR(16),
#     type VARCHAR (50)
# );
#         """))


    # def insert_table():
    #     with eng.connect() as conn:
    #         conn.execute(text("""                        
    # INSERT INTO rfid(dob, uid, type) VALUES
    # ('1999-01-08 4:05:06', '3D 75 8N 34', 'M300');
    #         """))


# def read_table():
#     with eng.connect() as conn:
#         dis = conn.execute(text("""                        
# SELECT * FROM rfid
#         """)).mappings()
#         for k in dis:
#             print(k)


# create_table()
# insert_table()
# read_table()




