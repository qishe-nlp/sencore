from spacy import displacy
from pathlib import Path

def print_doc(doc):
  for t in doc:
    print("{} {} {} {} {} {}".format(t.text, t.pos_, t.dep_, t.tag_, t.morph, t.lemma_))

def graph(doc, lang):
  svg = displacy.render(doc, style="dep", jupyter=False)
  file_name = '-'.join([w.text for w in doc if not w.is_punct]) + ".svg"
  output_path = Path(lang+ "_images/" + file_name)
  output_path.open("w", encoding="utf-8").write(svg)
