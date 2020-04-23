from kafka import KafkaConsumer

# continuous loop
var = 1

while var == 1:

    # initialize consumer to given topic and broker
    consumer = KafkaConsumer('test',
                             bootstrap_servers='localhost:9092')

    # verify connection
    print('Connected')
    print(consumer.bootstrap_connected())

    # loop and print messages
    for msg in consumer:
        print('...received')
        print(msg)
