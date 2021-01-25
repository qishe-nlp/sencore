from sencore.parser import Parser
import spacy
#from spacy import displacy
from phrase_recognizer import NounPhraseRecognizer, PrepPhraseRecognizer, VerbKnowledgeRecognizer

def merge_ranges(ranges):
  ordered = sorted(ranges, key=lambda x: x[0])
  purified = []
  index = 0
  while index < len(ordered)-1:
    first, second = ordered[index], ordered[index+1]
    if first[1] > second[0]:
      purified.append((first[0], max(first[1], second[1]), first[2]))
      index = index + 2
    else:
      purified.append(first)
      index = index + 1
  if index == len(ordered)-1:
    purified.append(ordered[index])
  return purified

def extend_ranges(ranges, maxlen):
  ordered = merge_ranges(ranges)
  start = 0
  result = []
  for e in ordered:
    if start < e[0]:
      result.append((start, e[0], "plain"))
    result.append(e)
    start = e[1]
  if start < maxlen:
    result.append((start, maxlen, "plain"))
  return result

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

    noun_phrases_ranges = [(np.start, np.end, "noun_phrases") for np in doc._.noun_phrases]
    prep_phrases_ranges = [(pp.start, pp.end, "prep_phrases") for pp in doc._.prep_phrases]
    verbs_ranges = [(v.i, v.i+1, "verbs") for v in doc._.verbs]

    doc_mark = extend_ranges(noun_phrases_ranges+prep_phrases_ranges+verbs_ranges, len(doc))
    markers = [(doc[d[0]: d[1]].text, d[2]) for d in doc_mark]

    return {
      "noun_phrases": noun_phrases,
      "prep_phrases": prep_phrases,
      "verbs": verbs,
      "passive_phrases": passive_phrases,
      "verb_phrases": verb_phrases,
      "markers": markers
    }

