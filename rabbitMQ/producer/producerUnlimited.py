import pika
import time
import json
import random
import string


def produce_msg(channel):
    while True:
        time.sleep(1)
        message = json.dumps({
            "timestamp": time.time(),
            "value": ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(10, 50)))
        })
        channel.basic_publish(exchange='', routing_key='iot_data', body=message)
        print(f'Message sent: {message}')


def main():
    while True:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', credentials=pika.PlainCredentials('newuser', 'newpassword')))
            channel = connection.channel()
            channel.queue_declare(queue='iot_data')

            produce_msg(channel)

            connection.close()
        except pika.exceptions.AMQPConnectionError:
            print("RabbitMQ is not ready. Waiting...")
            time.sleep(5)


if __name__ == "__main__":
    main()