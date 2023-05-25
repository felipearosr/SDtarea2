import pika
import time
import json
import random
import string

categories = ['Temperatura', 'Humedad', 'Presion', 'Viento', 'Radiacion']

def produce_msg(channel, category):
    while True:
        time.sleep(1)
        message = json.dumps({
            "timestamp": time.time(),
            "value": ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(10, 50))),
            "category": category
        })
        channel.basic_publish(exchange='', routing_key=category, body=message)
        print(f'Message sent: {message}')

def main():
    while True:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', credentials=pika.PlainCredentials('newuser', 'newpassword')))
            channel = connection.channel()

            for category in categories:
                channel.queue_declare(queue=category)

            category = random.choice(categories)
            produce_msg(channel, category)

            connection.close()
        except pika.exceptions.AMQPConnectionError:
            print("RabbitMQ is not ready. Waiting...")
            time.sleep(5)

if __name__ == "__main__":
    main()