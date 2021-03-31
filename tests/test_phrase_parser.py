from sencore import PhraseParser


def test_phrase_parser():
  lang = "en"
  sentence = "Apple is looking at buying U.K. startup for $1 billion."
  p = PhraseParser(lang)
  phrases = p.digest(sentence)
  print(phrases)
  assert isinstance(phrases, dict) == True

