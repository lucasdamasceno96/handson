FROM golang:1.24rc2-bullseye AS builder 
WORKDIR /app
COPY main.go .
RUN go mod init main && \
    CGO_ENABLED=0 go build

FROM scratch 
EXPOSE 8080
COPY --from=builder /app/main /go/main
CMD ["./main"]

