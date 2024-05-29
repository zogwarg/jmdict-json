#!/usr/bin/env bash
echo Getting remote files:
curl http://ftp.edrdg.org/pub/Nihongo/JMdict.gz -o JMdict.xml.gz -L
curl -O http://ftp.edrdg.org/pub/Nihongo/JMnedict.xml.gz -L
curl -O https://www.edrdg.org/kanjidic/kanjidic2.xml.gz -L

echo Decompressing:
gzip -d JMdict.xml.gz
gzip -d JMnedict.xml.gz
gzip -d kanjidic2.xml.gz


echo Backup:
[[ -f jmdict.json ]] && cp jmdict.json jmdict.json.bk
[[ -f jmnedict.json ]] && cp jmnedict.json jmnedict.json.bk
[[ -f kanjidict.json ]] && cp kanjidict.json kanjidict.json.bk

echo Converting to JSON:
python3 convert-jmdict.py
python3 convert-jmnedict.py
python3 convert-kanjidict.py

cat kanjidict.json | jq '
  pick(
    .character
    | .literal,
      (
        .misc?
        | .freq,
          .jlpt,
          .grade
      ),
      .dic_number?.dic_ref,
      (
        .reading_meaning?
        | .rmgroup?.reading,
          .nanori
      )
  )
  | ( .character.dic_number?.dic_ref | arrays) |= map(select(.["@dr_type"] == "heisig6"))
  | ( .character.reading_meaning?.rmgroup?.reading | arrays) |= map(select(.["@r_type"] | . == "ja_on" or . == "ja_kun"))
  | select(.character.dic_number?.dic_ref[0])
  | .character.reading_meaning |= (
    (
      .rmgroup.reading
      | group_by(.["@r_type"])
      | map({(.[0]["@r_type"]): [ .[]["#text"]] }) | add  ) + {nanori}
    )
  | .character.heisig = (.character.dic_number.dic_ref[0]["#text"] | tonumber) | del(.character.dic_number)
' -c | jq -sc 'sort_by(.character.heisig) | .[]' > kanjidict-heisig.json

echo Clean Backup:
rm jmdict.json.bk jmnedict.json.bk kanjidict.json.bk
