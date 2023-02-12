FROM golang:alpine
# Maintainer label is deprecated.
LABEL maintainer="Richard L. Briley Jr."
COPY . /go/src/app
WORKDIR /go/src/app
EXPOSE 6111:6111
RUN go mod init
RUN go build -o helloworld
CMD [ "./helloworld" ]
