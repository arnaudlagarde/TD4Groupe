FROM jupyter/base-notebook

USER root

RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
    

USER ${NB_UID}

ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
ENV PATH=$PATH:$JAVA_HOME/bin

# Expose Jupyter Notebook port
EXPOSE 8888