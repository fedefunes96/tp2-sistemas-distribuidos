import pika
import sys
import random
import time

class Receiver:
    def __init__(self):
        self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(host='rabbitmq')
            )

    def receive_from_topic(self, topic, callback):
        self.channel = self.connection.channel()

        self.channel.exchange_declare(exchange=topic, exchange_type='fanout')

        result = self.channel.queue_declare(queue='', durable=True)

        queue_name = result.method.queue

        self.channel.queue_bind(exchange=topic, queue=queue_name)

        self.channel.basic_qos(prefetch_count=1)

        self.channel.basic_consume(
            queue=queue_name, on_message_callback=self.data_read, auto_ack=True
        )    

        self.callback = callback

        self.channel.start_consuming()

    def data_read(self, ch, method, properties, body):        
        self.callback(method, properties.type, body.decode('utf-8'))

    def receive_distributed_work(self, queue, callback):
        self.channel = self.connection.channel()

        self.channel.queue_declare(queue=queue, durable=True)

        self.channel.basic_qos(prefetch_count=1)

        self.channel.basic_consume(
            queue=queue, on_message_callback=self.work_read
        )

        self.callback = callback

        self.channel.start_consuming()

    def ack_work_done(self, queue, method):
        self.channel.basic_ack(delivery_tag = method.delivery_tag)

    def work_read(self, ch, method, properties, body):
        self.callback(method, properties.type, body.decode('utf-8'))

    def close_topic(self, topic):
        self.channel.close()
    
    def close_work_queue(self, queue):
        self.channel.close()        

    def close(self):
        self.connection.close()

'''class Receiver:
    def __init__(self):
        self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(host='rabbitmq')
            )
        
        self.topics = {}
        self.topics_callbacks = {}
        self.work_queues = {}
        self.work_callbacks = {}

    def receive_from_topic(self, topic, callback):
        self.topics[topic] = self.connection.channel()

        self.topics[topic].exchange_declare(exchange=topic, exchange_type='fanout')

        result = self.topics[topic].queue_declare(queue='', durable=True)

        queue_name = result.method.queue

        self.topics[topic].queue_bind(exchange=topic, queue=queue_name)

        self.topics[topic].basic_qos(prefetch_count=1)

        self.topics[topic].basic_consume(
            queue=queue_name, on_message_callback=self.data_read, auto_ack=True
        )    

        self.topics_callbacks[topic] = callback

        self.topics[topic].start_consuming()

    def data_read(self, ch, method, properties, body):        
        self.topics_callbacks[method.exchange](properties.type, body.decode('utf-8'))

    def receive_distributed_work(self, queue, callback):
        self.work_queues[queue] = self.connection.channel()

        self.work_queues[queue].queue_declare(queue=queue, durable=True)

        self.work_queues[queue].basic_qos(prefetch_count=1)

        self.work_queues[queue].basic_consume(
            queue=queue, on_message_callback=self.work_read
        )

        self.work_callbacks[queue] = callback

        self.work_queues[queue].start_consuming()

    def ack_work_done(self, queue):
        self.work_queues[queue].basic_ack(delivery_tag = method.delivery_tag)

    def work_read(self, ch, method, properties, body):
        print(dir(ch))
        print(dir(properties))
        print(dir(method))
        self.work_callbacks[method.queue](properties.type, body.decode('utf-8'))

    def close_topic(self, topic):
        channel = self.topics.pop(topic)
        channel.close()
    
    def close_work_queue(self, queue):
        channel = self.work_queues.pop(queue)
        channel.close()        

    def close(self):
        self.connection.close()
'''