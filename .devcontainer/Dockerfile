# A basic Dockerfile to demonstrate our tmux configuration
FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Prompt avoidance
ENV DEBIAN_FRONTEND=noninteractive

# Install tmux
RUN apt-get update -y && apt-get install -y \
tmux \
&& rm -rf /var/lib/apt/lists/*