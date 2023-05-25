from confluent_kafka import Producer
import json
import time
import random

p = Producer({'bootstrap.servers': 'kafka:9092'})

categories = ['Temperatura', 'Humedad', 'Presion', 'Viento', 'Radiacion']

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

message_count = 1000
start_time = time.time()

for i in range(message_count):
    category = random.choice(categories)
    data = {'timestamp': time.time(), 'value': ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=random.randint(10, 50))), 'category': category}
    p.produce(category, json.dumps(data), callback=delivery_report)
    p.poll(0)
    time.sleep(random.randint(1, 3))

end_time = time.time()
print(f'Sent {message_count} messages in {end_time - start_time} seconds.')