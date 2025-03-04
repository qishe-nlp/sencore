from sencore import KGParser
import json

def _get_source(lang):
  sentences = []
  senfile = "test_source/{}_test.json".format(lang)
  with open(senfile, encoding="utf8") as f:
    sentences = json.loads(f.read())
  return sentences

def _validate_kg_parser(lang):
  p = KGParser(lang)
  sentences = _get_source(lang)
  for s in sentences:
    kgs = p.digest(s)
    print(kgs)
    assert isinstance(kgs, dict) == True

def test_kg_parser():
  langs = ["en", "es"]
  for lang in langs:
    _validate_kg_parser(lang)
