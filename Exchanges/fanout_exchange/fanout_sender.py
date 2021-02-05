# Requirements
import pika
import sys

# Connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

# Let's Send sample message in hard code , also send by giving input in message
message = ' Sample message 1 '
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(" [x] Sent %r" % message)

# closing connection
connection.close()

# Working @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@