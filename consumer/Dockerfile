FROM bde2020/spark-master:3.3.0-hadoop3.3

COPY consumer_spark.py /consumer/consumer_spark.py

WORKDIR /consumer

CMD ["../spark/bin/spark-submit", "--master", "local[*]", "--packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0", "consumer_spark.py"]
