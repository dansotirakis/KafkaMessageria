# Kafka compose
### Kafka - Messageria Cluster
### Zookeeper - Brok's Manager
#### Parameters 
#### Optional:
##### KAFKA_CREATE_TOPICS 
`Create a test topic with 5 partitions and 2 replicas`
#### Mandatory
##### KAFKA_ADVERTISED_HOST_NAME
`Put the IP of your host, the IP on your main network adapter`
##### KAFKA_ZOOKEEPER_CONNECT
`Tell Kafka to connect to the Zookeeper container at port 2181`
#### Run commands
##### Build containers
`docker-compose -f docker-compose.yml up`
##### Or
##### Build containers (save)
`docker-compose -f docker-compose.yml up -d`
#### Handling commands
##### Access into kafka service container
`docker exec -it kafka /bin/sh`
##### Access to command directory at kafka service
`cd opt/kafka_2.12-2.4.1`
##### Command create a topic in kafka service
`./bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic testtopic`
##### Command list topics in kafka service
`./bin/kafka-topics.sh --list --zookeeper zookeeper:2181`
##### Command create producer console
`bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test`
### Command create consumer console
`bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning`
