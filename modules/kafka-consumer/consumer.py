from kafka import KafkaConsumer


TOPIC_NAME = 'locations'

consumer = KafkaConsumer(TOPIC_NAME)
for message in consumer:
    print (message)
