#!/bin/bash

for i in $(cat $1)
do
url="${2/FUZZ/$i}"
tempfile=$(mktemp)
code=$(curl -s $url --write-out '%{http_code}' -o $tempfile)
echo "$code          $url"
rm -rf $tempfile
done
