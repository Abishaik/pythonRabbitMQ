# Requirements
import pika,sys,os

# Error handling : try/except
try:

    # to get message with routing key 
    print('[*] Enter the message to send..... To exit press CTRL+C')

    # while loop for repeating the same process until keyboard intruption
    while(True):

        # connecting rabbit mq
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

        #input routing key and message splitted by space 
        # eg "1 sample_message_for_server1"
        data = input().split(' ')
        severity = data[0]
        message = data[1]
        channel.basic_publish( exchange='direct_logs', routing_key=severity, body=message)

        # to view the sent data
        print(" [x] Sent %r:%r" % (severity, message))


except KeyboardInterrupt:
    print('Interrupted')
    connection.close()
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)



# working @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@