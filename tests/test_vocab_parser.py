from sencore import VocabParser
import json

lang = "en"
sentences = []
senfile = "test_source/{}_test.json".format(lang)
with open(senfile, encoding="utf8") as f:
  sentences = json.loads(f.read())

def test_vocab_parser():
  p = VocabParser(lang, poses=["VERB"])
  for s in sentences:
    print(s)
    vocabs = p.digest(s)
    print(vocabs)
    assert isinstance(vocabs, list) == True

