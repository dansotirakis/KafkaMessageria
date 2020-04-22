#Kafka compose

###Kafka - Messageria Cluster
###Zookeeper - Brok's Manager

###Parameters 
###Optional:

###KAFKA_CREATE_TOPICS 
`Crie um tópico de teste com 5 partições e 2 réplicas`

###Mandatory

######KAFKA_ADVERTISED_HOST_NAME
`Coloque o IP do seu host, o IP no seu adaptador de rede principal`
######KAFKA_ZOOKEEPER_CONNECT
`Diga ao Kafka para conectar-se ao contêiner do Zookeeper na porta 2181`

###Run commands

###Build containers

`docker-compose -f docker-compose.yml up`

###Or

###Build containers (save)
`docker-compose -f docker-compose.yml up -d`

###Handling commands

###Access into kafka service container
`docker exec -it kafka /bin/sh`

###Access to command directory at kafka service
`cd opt/kafka_2.12-2.4.1`

###Command create a topic in kafka service
`./bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic testtopic`

###Command list topics in kafka service
`./bin/kafka-topics.sh --list --zookeeper zookeeper:2181`

###Command create producer console
`bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test`
###Command create consumer console
`bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning`
