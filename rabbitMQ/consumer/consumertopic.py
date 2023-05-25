import pika
import time

categories = ['Temperatura', 'Humedad', 'Presion', 'Viento', 'Radiacion']

def process_msg(ch, method, properties, body):
    print(f"Received message: {body}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    while True:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', credentials=pika.PlainCredentials('newuser', 'newpassword')))
            channel = connection.channel()

            for category in categories:
                channel.queue_declare(queue=category)
                channel.basic_qos(prefetch_count=1)
                channel.basic_consume(queue=category, on_message_callback=process_msg)

            channel.start_consuming()
        except pika.exceptions.AMQPConnectionError:
            print("RabbitMQ is not ready. Waiting...")
            time.sleep(5)

if __name__ == "__main__":
    main()