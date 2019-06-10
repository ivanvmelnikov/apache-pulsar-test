import pulsar
import time

client = pulsar.Client('pulsar://localhost:6650')
producer = client.create_producer('my-topic')

counter = 0;
while True:
    producer.send(('hello-pulsar-%d' % counter).encode('utf-8'))
    counter += 1
    time.sleep(1)


client.close()
