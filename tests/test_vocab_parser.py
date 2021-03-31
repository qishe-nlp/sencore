from sencore import VocabParser

def test_vocab_parser():
  lang = "en"
  sentence = "Apple is looking at buying U.K. startup for $1 billion."

  p = VocabParser(lang)
  vocabs = p.digest(sentence)
  print(vocabs)
  
  assert isinstance(vocabs, list) == True

