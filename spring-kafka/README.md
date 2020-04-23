# Spring Kafka Application 

>Example: kafka-producer | kafka-consumer in SpringBoot

#### If you want to see in real time create these two before building consumers.
    docker exec -it kafka /bin/sh
    cd opt/kafka_2.12-2.4.1/bin
    
    kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic baeldung --from-beginning
    kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic greeting --from-beginning
  
#### Dependencies
    mvn clean package
#### Run
    java -jar target/app-0.0.1-SNAPSHOT.jar  