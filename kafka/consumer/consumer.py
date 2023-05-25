from confluent_kafka import Consumer, KafkaError
import uuid

c = Consumer({
    'bootstrap.servers': 'kafka:9092',
    'group.id': str(uuid.uuid4()),  # genera un UUID único
    'auto.offset.reset': 'earliest'
})

c.subscribe(['iot-data'])

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print(f"Consumer error: {msg.error()}")
        continue

    #print(f"Received message: {msg.value().decode('utf-8')}")

c.close()


