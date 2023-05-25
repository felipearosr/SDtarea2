import uuid
from confluent_kafka import Consumer, KafkaError

c = Consumer({
    'bootstrap.servers': 'kafka:9092',
    'group.id': str(uuid.uuid4()),
    'auto.offset.reset': 'earliest'
})

categories = ['Temperatura', 'Humedad', 'Presion', 'Viento', 'Radiacion']
c.subscribe(categories)

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print(f"Consumer error: {msg.error()}")
        continue

    print(f"Received message: {msg.value().decode('utf-8')}")

c.close()