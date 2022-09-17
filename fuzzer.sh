#!/bin/bash


mkdir splitting_the_wordlist

mv $1 splitting_the_wordlist/

cd splitting_the_wordlist

split -n $3 $1

mv $1 ../

url=$2

fuzz()
{
for i in $(cat $1)
do
url_to_go="${url/FUZZ/$i}"
tempfile=$(mktemp)
code=$(curl -s $url_to_go --write-out '%{http_code}' -o $tempfile)
echo "$code          $url_to_go"
rm -rf $tempfile
done
}

for file in $(ls)
do
fuzz $file &
done
