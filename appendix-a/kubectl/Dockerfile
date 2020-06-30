FROM alpine:3.9.6

RUN apk add --no-cache --virtual=build-deps wget \
  && wget https://storage.googleapis.com/kubernetes-release/release/v1.18.2/bin/linux/amd64/kubectl \
  && mv kubectl /usr/local/bin/kubectl \
  && chmod +x /usr/local/bin/kubectl \
  && apk del build-deps

ENTRYPOINT ["/usr/local/bin/kubectl"]
CMD [""]
