
from confluent_kafka import Producer

p = Producer({'bootstrap.servers': '35.197.152.28:9092'})

p.produce('mytopic', "data".encode('utf-8'))

p.flush()