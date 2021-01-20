from sencore.parser import Parser
import spacy
#from spacy import displacy
from phrase_recognizer import NounPhraseRecognizer, PrepPhraseRecognizer, VerbKnowledgeRecognizer

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
    np_recognizer = NounPhraseRecognizer(self._nlp)
    self._nlp.add_pipe(np_recognizer)
    pp_recognizer = PrepPhraseRecognizer(self._nlp)
    self._nlp.add_pipe(pp_recognizer)
    vk_recognizer = VerbKnowledgeRecognizer(self._nlp)
    self._nlp.add_pipe(vk_recognizer)

  def digest(self, sentence):
    doc = self._nlp(sentence)
    
    noun_phrases = [np.text for np in doc._.noun_phrases]
    prep_phrases = [pp.text for pp in doc._.prep_phrases]
    verbs = [{"text": v.text, "tag": v.tag_, "form": spacy.explain(v.tag_), "lemma": v.lemma_} for v in doc._.verbs]
    passive_phrases = [pp.text for pp in doc._.passive_phrases]
    verb_phrases = doc._.verb_phrases

    return {
      "noun_phrases": noun_phrases,
      "prep_phrases": prep_phrases,
      "verbs": verbs,
      "passive_phrases": passive_phrases,
      "verb_phrases": verb_phrases
    }

