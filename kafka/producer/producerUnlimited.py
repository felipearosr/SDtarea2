from confluent_kafka import Producer
import json
import time
import random

p = Producer({'bootstrap.servers': 'kafka:9092'})

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

while True:
    data = {'timestamp': time.time(), 'value': ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=random.randint(10, 50)))}
    p.produce('iot-data', json.dumps(data), callback=delivery_report)
    p.poll(0)
    time.sleep(random.randint(1, 3))
