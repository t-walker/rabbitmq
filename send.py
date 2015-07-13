import pika
import os
import threading

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')

threads = []
for i in range(50000):
    t = threading.Thread(channel.basic_publish(exchange='', routing_key='hello', body=str(i)))
    t.start()

connection.close()
