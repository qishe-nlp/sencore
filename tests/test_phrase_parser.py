from sencore import PhraseParser, PhraseModelParser
import json

lang = "en"
sentences = []
senfile = "test_source/{}_test.json".format(lang)
with open(senfile, encoding="utf8") as f:
  sentences = json.loads(f.read())

def test_phrase_parser():
  p = PhraseParser(lang)
  for s in sentences:
    phrases = p.digest(s)
    print(phrases)
    assert isinstance(phrases, dict) == True

def test_phrase_model_parser():
  p = PhraseModelParser(lang)
  for s in sentences:
    print(s)
    phrases = p.digest(s)
    print(phrases)
    assert isinstance(phrases, list) == True

