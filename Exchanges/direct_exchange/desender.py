import pika,sys,os

try:
    print('[*] Enter the message to send..... To exit press CTRL+C')
    while(True):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

        data = input().split(' ')
        severity = data[0]
        message = data[1]
        channel.basic_publish( exchange='direct_logs', routing_key=severity, body=message)
        print(" [x] Sent %r:%r" % (severity, message))
except KeyboardInterrupt:
    print('Interrupted')
    connection.close()
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
