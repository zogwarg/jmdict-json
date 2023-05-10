#!/usr/bin/env bash
echo Getting remote files:
curl http://ftp.edrdg.org/pub/Nihongo/JMdict.gz -o JMdict.xml.gz -L
curl -O http://ftp.edrdg.org/pub/Nihongo/JMnedict.xml.gz -L

echo Decompressing:
gzip -d JMdict.xml.gz
gzip -d JMnedict.xml.gz



echo Converting to JSON:
cp jmdict.json jmdict.json.bk
cp jmnedict.json jmnedict.json.bk
python3 convert-jmdict.py
python3 convert-jmnedict.py
rm jmdict.json.bk jmnedict.json.bk
