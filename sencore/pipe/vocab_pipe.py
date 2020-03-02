from sencore.pipe.scpipe import SCPipe
from sencore.model.vocab_model import VocabModel
from sencore.pipe.configuration import pkgindices, dictindices
from importlib import import_module

import spacy
from spacy.tokens import Token

Token.set_extension("dictionary", default=False)

class VocabPipe(SCPipe):

    def __init__(self, lang, pkgs=pkgindices, dictapis=dictindices):
        """
        Set the language, load the model, set dictionary
        """
        super().__init__(lang)
        self.nlp = spacy.load(pkgs[lang]) 
        module_name, cls_name = dictapis[lang] 
        module = import_module(module_name)
        self.dictapi = getattr(module, cls_name)

    def digest(self, sentence):
        """
        Process sentence into vocabs setting in VocabModel
        """
        vocabs = self.nlp(sentence)
        for w in vocabs:
            w._.dictionary = self.dictapi.word(w.text, w.pos_)
        return VocabModel(vocabs)
