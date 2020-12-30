import pika,sys,os

try:
    print('[*] Enter the message to send..... To exit press CTRL+C')
    while(True):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
        
        routing_key = input("routing key :")
        message = input("message :")
        channel.basic_publish(exchange='topic_logs', routing_key=routing_key, body=message)
        print(" [x] Sent %r:%r" % (routing_key, message))
except KeyboardInterrupt:
    print('Interrupted')
    connection.close()
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
