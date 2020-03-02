from sencore.model.scmodel import SCModel

class VocabModel(SCModel):
    def __init__(self, obj):
        super().__init__(obj)

    def display(self, options={}):
        import spacy
        for w in self.obj:
            print("{}\t{}\t{}".format(w.text, w.tag_, spacy.explain(w.tag_)))

            for e in w._.dictionary.target["explainations"]:
                print(e["meaning"])
                for ex in e["examples"]:
                    print(ex)

    def simple_exp(self):
        import spacy
        exp = []
        for w in self.obj:
            r = {
                'pos': w.pos_,
                'tag': w.tag_,
                'text': w.text,
                'tag_more': spacy.explain(w.tag_),
                'meanings': [e["meaning"] for e in w._.dictionary.target["explainations"]]
            }
            exp.append(r)
        return exp
