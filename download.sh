#!/usr/bin/env bash
echo Getting remote files:
curl http://ftp.edrdg.org/pub/Nihongo/JMdict.gz -o JMdict.xml.gz -L
curl -O http://ftp.edrdg.org/pub/Nihongo/JMnedict.xml.gz -L

echo Decompressing:
gzip -d JMdict.xml.gz
gzip -d JMnedict.xml.gz


echo Backup:
[[ -f jmdict.json ]] && cp jmdict.json jmdict.json.bk
[[ -f jmnedict.json ]] && cp jmnedict.json jmnedict.json.bk

echo Converting to JSON:
python3 convert-jmdict.py
python3 convert-jmnedict.py

echo Clean Backup:
rm jmdict.json.bk jmnedict.json.bk
