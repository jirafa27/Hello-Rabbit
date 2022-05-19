import random
import time
import pika
i = 0
while True:

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World!'+str(i))
    print(" [x] Sent 'Hello World! "+str(i)+"'")
    connection.close()
    time.sleep(random.randint(0, 3))
    i+=1