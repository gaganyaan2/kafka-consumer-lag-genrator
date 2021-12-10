apiVersion: apps/v1
kind: Deployment
metadata:
  name: kafka-producer
  env: prod
spec:
  selector:
    matchLabels:
      app: kafka-producer
  replicas: 1
  template:
    metadata:
      labels:
        app: kafka-producer
    spec:
      containers:
      - name: kafka-producer
        image: kafka-consumer-lag-generator:1.0
        imagePullPolicy: Always
        command: ["/bin/sh"]
        args: ["-c", "python -u /kafka/producer.py --server kafka:9092 --topic topic1 --messages 100 --sleep 0"]
        resources:
          requests:
            memory: "512Mi"
            cpu: "200m"
          limits:
            memory: "512Mi"
            cpu: "500m"