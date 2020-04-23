# Kafka compose
    Kafka - Messageria Cluster
    Zookeeper - Broks Manager

#### Parameters 
    Optional:
    KAFKA_CREATE_TOPICS - Create a test topic with 5 partitions and 2 replicas
    
    Mandatory
    KAFKA_ADVERTISED_HOST_NAME - Put the IP of your host, the IP on your main network adapter
    KAFKA_ZOOKEEPER_CONNECT - Tell Kafka to connect to the Zookeeper container at port 2181
    
#### Run

##### Build containers
    docker-compose -f docker-compose.yml up -d

#### Operating commands

##### Access into kafka service container
    docker exec -it kafka /bin/sh
##### Access to command directory at kafka service
    cd opt/kafka_2.12-2.4.1/bin
##### Command list topics in kafka service
    kafka-topics.sh --list --bootstrap-server localhost:9092
##### Command create producer console
    kafka-console-producer.sh --broker-list localhost:9092 --topic test
##### Command create consumer console
    kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning

>Examples : Spring-kafka, Python-kafka

###### For more information, please visit the Apache Kafka documentation at: [Documentation](https://kafka.apache.org/)