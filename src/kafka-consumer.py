from kafka import KafkaConsumer

# continuous loop
var = 1

while var == 1:

    # initialize consumer to given topic and broker
    consumer = KafkaConsumer('test-topic',
                             group_id='consumer-1',
                             bootstrap_servers=['localhost:32768'])

    # verify connection
    print('Brooke is connected')
    print(consumer.bootstrap_connected())
    print(consumer.topics())

    # loop and print messages
    for message in consumer:
        print('...received')
        print(message.topics())
