from sencore.parser import Parser
import spacy

class VocabParser(Parser):

  pkgindices = {
    "en": "en_core_web_md",
    "es": "es_core_news_md",
    "de": "de_core_news_md",
    "fr": "fr_core_news_md",
  }

  def __init__(self, lang):
    super().__init__(lang) 
    self._nlp = spacy.load(self.__class__.pkgindices[lang])

  def digest(self, sentence):
    doc = self._nlp(sentence)
    return [{'word': e.text, 'pos': e.pos_} for e in doc]
    
