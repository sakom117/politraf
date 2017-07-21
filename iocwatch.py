#!/usr/bin/env python3
# -*- coding: utf-8

from infi.clickhouse_orm.database import Database
from infi.clickhouse_orm.models import Model
from infi.clickhouse_orm.fields import *
from infi.clickhouse_orm.engines import MergeTree
from pytz import timezone
import psutil, datetime
from pytz import timezone

class IOC_OTX(Model):

    event_date = DateField()
    timestamp = DateTimeField()
    indicator = StringField()
    name = StringField()
    references = StringField()
    
    engine = MergeTree('event_date', ('timestamp', 'indicator', 'name', 'references'))

class CONNStats(Model):

    event_date = DateField()
    timestamp = DateTimeField()
    protocol = StringField()
    src_addr = StringField()
    src_port = Float32Field()
    dst_addr = StringField()
    dst_port = Float32Field()
    qry_name = StringField()
    
    engine = MergeTree('event_date', ('timestamp', 'protocol', 'src_addr', 'src_port', 'dst_addr', 'dst_port', 'qry_name'))

db = Database('conn_stat')
#db.create_table(CONNStats)


#db = Database('comromised')
#db.create_table(IOC_OTX)

# 5 min time
tz = timezone('Europe/Moscow')
to_time = datetime.datetime.now(tz)
from_time = datetime.datetime.now(tz) - datetime.timedelta(minutes=5)
timestamp = (from_time - datetime.datetime(1970, 1, 1)) / datetime.timedelta(seconds=1)
timestamp2 = str(timestamp)
print (from_time)

class OTXWatch():

    def get_traf_last(self):
            print ("Starting fetch traffic stat ...")
            for row in db.select('SELECT timestamp, src_addr, src_port, dst_addr, dst_port, qry_name FROM conn_stat.connstats WHERE timestamp >= toDateTime('+timestamp+') ORDER BY timestamp LIMIT 10'):
                print (row.timestamp, row.src_addr, row.dst_addr)
            

#    def check_iocs(self):
#
#        today = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')
#
#        print ("Processing indicators ...")
#        for event in self.events:
#            try:
#                for indicator in event["indicators"]:
#
#                    try:
#                        
#                        if indicator["type"] in ('domain', 'hostname', 'IPv4', 'IPv6', 'CIDR'):
#                            indicator = indicator["indicator"]
#                            name = event["name"]
#                            references = event["references"][0]
#                            #print (indicator, name, references)
#                            timestamp = datetime.datetime.now()
#                            today = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')
#                            db.insert([IOC_OTX(event_date=today, timestamp=timestamp, indicator=indicator, name=name, references=references)])
#
#                    except Exception as e:
#                        pass
#
#            except Exception as e:
#                traceback.print_exc()

if __name__ == '__main__':

    # Retrieve the traffic events
    traf_receiver = OTXWatch()

    # Retrieve the events and store the IOCs
    # otx_receiver.get_iocs_last(int(args.l))
    traf_receiver.get_traf_last()

    # Write IOC files
#    traf_receiver.check_iocs()
