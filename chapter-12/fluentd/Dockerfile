# fluentd/Dockerfile
FROM fluent/fluentd:v1.9-1
USER root
RUN ["gem", "install", "fluent-plugin-elasticsearch", "-N", "--version", "4.0.9"]
USER fluent
