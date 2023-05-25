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

msg_count = 1000

start_time = time.time()

for i in range(msg_count):
    data = {'timestamp': time.time(), 'value': ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=random.randint(10, 50)))}
    p.produce('iot-data', json.dumps(data), callback=delivery_report)
    p.poll(0)

p.flush()

total_time = time.time() - start_time
print(f"Sent {msg_count} in {total_time} seconds")
