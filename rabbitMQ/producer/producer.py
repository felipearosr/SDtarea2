import pika
import time

def main():
    message_count = 0
    message_limit = 1000
    start_time = time.time() 

    while True:
        try:
            if message_count < message_limit:
                connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', credentials=pika.PlainCredentials('newuser', 'newpassword')))
                channel = connection.channel()
                channel.queue_declare(queue='iot_data')
                channel.basic_publish(exchange='', routing_key='iot_data', body='Your message')  # send a message
                print(f"Sent message: Your message")
                connection.close()

                message_count += 1  # increment the count

            else:
                break  # stop the loop when the limit is reached

        except pika.exceptions.AMQPConnectionError:
            print("RabbitMQ is not ready. Waiting...")
            time.sleep(5)

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time: {total_time} seconds")


if __name__ == "__main__":
    main()