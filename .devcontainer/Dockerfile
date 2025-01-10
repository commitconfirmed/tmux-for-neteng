# A basic Dockerfile to demonstrate our tmux configuration
FROM ubuntu:latest

# Prompt avoidance
ENV DEBIAN_FRONTEND=noninteractive

USER root
WORKDIR /root

# Some standard Ubuntu packages for troubleshooting and a SSH server
RUN apt-get update -y && apt-get install -y \
tmux \
vim \
&& rm -rf /var/lib/apt/lists/*

# Copy configurations & setup
COPY example-bashrc.txt /root/example-bashrc.txt
COPY .tmux.conf /root/.tmux.conf
COPY generate-bashrc.py /root/generate-bashrc.py
COPY hosts.csv /root/hosts.csv
RUN mkdir log
RUN cat /root/example-bashrc.txt >> /root/.bashrc

ENTRYPOINT ["/bin/bash"]