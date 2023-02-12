#!/bin/bash

exec 3<>/dev/tcp/localhost/"$1"

echo -e "GET /path/to/health/endpoint/ HTTP/1.1
host: localhost:$1
" >&3

timeout 1 cat <&3 | grep status | grep healthy || exit 1