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