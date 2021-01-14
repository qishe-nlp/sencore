from sencore.parser import Parser
import spacy
from spacy import displacy

def detect_phrases(phrases, analysis):
  if len(analysis) == 0:
    return phrases
  else:
    c = analysis[0]  
    tree = [t for t in c.subtree]
    if len(tree) <= 3:
      phrases.append([" ".join([t.text for t in tree])]) 
    else:
      analysis += c.children
    del analysis[0]
    return detect_phrases(phrases, analysis)


class PhraseParser(Parser):

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

    #return [{"word": t.text, "dep": t.dep_, "pos": t.pos_, "tag": t.tag_} for t in doc]
      
    root = [e for e in doc if e.dep_=="ROOT"][0]
    #return [" ".join([t.text for t in c.subtree]) for c in root.children]
    phrases = []
    analysis = []
    analysis += root.children
    return detect_phrases(phrases, analysis)
    #return [{'word': e.text, 'dep': e.dep_} for e in doc]
    
