#!/usr/bin/env python3
#conding:utf-8

from sqlalchemy import create_engine, Table, MetaData, desc
from sqlalchemy.sql import select, and_, or_, not_, text


MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PWD = 'wefwef'
MYSQL_DBN = 'hergerg'

DRIVE_PRE = 'mysql+mysqldb'
#DRIVE_PRE = 'mysql+mysqlconnector'

engine = create_engine('%s://%s:%s@%s:%s/%s' % (
            DRIVE_PRE, MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_PORT, MYSQL_DBN
        ),
        encoding='utf8', connect_args={'charset':'utf8'}, echo=0,
    )

conn = engine.connect()
metadata=MetaData()


tlod = Table('your_table_name', metadata, autoload=True, autoload_with=engine)


def flush_old():
    s = select([tlod]).where( and_( tlod.c.device_id == None, tlod.c.id >= sid ) ).limit(200)
    result = conn.execute(s)

    upd = tlod.update().values(device_id=devid).where(tlod.c.id == i.id)
    conn.execute(upd)

    s = select([tlod.c.user_id]).where(tlod.c.device_id == devid)
    result = conn.execute(s)


def offset():
    offs = 0
    STE = 200

    st = datetime.datetime(2016, 6,1)
    et = datetime.datetime(2016, 6,2)
    while 1:
        s = select([sbl]).where( and_(sbl.c.time_created >= st, sbl.c.time_created < et))  \
            .limit(STE).offset(offs)
        #s = select([spd]).order_by(desc(spd.c.id)).limit(1)
        rows = conn.execute(s)
        if rows.rowcount == 0:
            break
        offs += STE

        for _ in rows:
            print(_)


def nbtext():
    sql = text('''select * from your_table_name where name = :x ''')
    rows = conn.execute(sql, x='6wef')
    print(rows.rowcount)
    for row in rows:
        print(row)



def show_tables():
    metadata.reflect(engine)
    print(metadata.tables.keys())





if __name__ == '__main__':
    nbtext()


