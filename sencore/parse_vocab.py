from sencore.pipe.vocab_pipe import VocabPipe 
import sys

def play(lang="en", sentence=None):
    sentences = {
        "en": "Apple is looking at buying U.K. startup for $1 billion.",
        "es": "En 1941, fue llamado a filas para incorporarse a la Armada.",
        "de": "Für Joachim Löw ist ein Nationalmannschafts-Comeback von Thomas Müller und Mats Hummels nicht mehr kategorisch ausgeschlossen.",
        "fr": "Nos jolis canards vont-ils détrôner les poules, coqueluches des jardiniers ?",
    }

    sen = sentence or sentences[lang]
    print(sen)
    vp = VocabPipe(lang)
    vm = vp.digest(sen)
    print(vm.simple_exp())

def run():
    lang = sys.argv[1] if len(sys.argv) >= 2 else "en" 
    sentence = sys.argv[2] if len(sys.argv) >= 3 else None
    play(lang, sentence)
