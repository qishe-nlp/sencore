from sencore import KGParser
import json

lang = "en"
sentences = []
senfile = "test_source/{}_test.json".format(lang)
with open(senfile, encoding="utf8") as f:
  sentences = json.loads(f.read())

def test_kg_parser():
  p = KGParser(lang)
  for s in sentences:
    kgs = p.digest(s)
    print(kgs)
    assert isinstance(kgs, dict) == True

