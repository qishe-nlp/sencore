from sencore import PhraseParser, PhraseModelParser
import json

def _get_source(lang):
  sentences = []
  senfile = "test_source/{}_test.json".format(lang)
  with open(senfile, encoding="utf8") as f:
    sentences = json.loads(f.read())
  return sentences

def _validate_phrase_parser(lang):
  p = PhraseParser(lang)
  sentences = _get_source(lang)
  for s in sentences:
    phrases = p.digest(s)
    print(phrases)
    assert isinstance(phrases, dict) == True

def _validate_phrase_model_parser(lang):
  p = PhraseModelParser(lang)
  sentences = _get_source(lang)
  for s in sentences:
    print(s)
    phrases = p.digest(s)
    print(phrases)
    assert isinstance(phrases, list) == True


def test_phrase_parser():
  langs = ["en", "es"]
  for lang in langs:
    _validate_phrase_parser(lang)
    #_validate_phrase_model_parser(lang)
