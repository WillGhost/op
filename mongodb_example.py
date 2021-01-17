#!/usr/bin/env python

from pymongo import MongoClient


mongodb_host = '192.168.56.48'
mongodb_user = 'root'
mongodb_pwd = '2c5cwefewfwf234239e414'

URI = 'mongodb://%s:%s@%s:27017/admin' %(mongodb_user, mongodb_pwd, mongodb_host)
client = MongoClient(URI)

#mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]
#https://docs.mongodb.com/manual/reference/connection-string/

db = client['db_name']

col_logs = db['collection_name']


analysis = col_logs.find()

cc = 0
for a in analysis:
    cc += 1
    print a
    if cc > 15:
        break

