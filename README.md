[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/facebook/react/blob/master/LICENSE) 
[![npm version](https://img.shields.io/npm/v/react.svg?style=flat)](https://www.npmjs.com/package/react) 
[![CircleCI Status](https://circleci.com/gh/facebook/react.svg?style=shield&circle-token=:circle-token)](https://circleci.com/gh/facebook/react) 
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://reactjs.org/docs/how-to-contribute.html#your-first-pull-request)

![phyton](https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRKhb5t3rIXW4GW_ZJAoiwUtV9TMIGB_7lZLg&usqp=CAU)
![java](https://image.flaticon.com/icons/png/128/919/919854.png)

![Spring](https://hack24x7.com/img/icons/development/Spring.png)
![spring-cloud](https://avatars-03.gitter.im/group/iv/4/575c3e6cc2f0db084a1d5892)
![maven](https://www.runoob.com/wp-content/uploads/2018/09/maven-logo-128.png)
![docker](https://dunstontc.gallerycdn.vsassets.io/extensions/dunstontc/vscode-docker-syntax/0.1.5/1527792532694/Microsoft.VisualStudio.Services.Icons.Default)
![kafka](https://cdn.eventil.com/uploads/group/avatar/1182/medium_highres_465871372.jpeg)

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
