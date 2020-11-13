# Usage

### Install from pip3
``` 
pip3 install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple --verbose sencore
```

### Install spacy lib
```
python -m spacy download en_core_web_sm
```

### Executable usage
Parse sentence into vocabs
```
parse_to_vocab --lang en --sentence "It is a great day"
```

### Package usage
```
from sencore import VocabParser 

def vocab(lang, sentence):
  sentences = {
      "en": "Apple is looking at buying U.K. startup for $1 billion.",
      "es": "En 1941, fue llamado a filas para incorporarse a la Armada.",
      "de": "Für Joachim Löw ist ein Nationalmannschafts-Comeback von Thomas Müller und Mats Hummels nicht mehr kategorisch ausgeschlossen.",
      "fr": "Nos jolis canards vont-ils détrôner les poules, coqueluches des jardiniers ?",
  }

  sen = sentence or sentences[lang]
  print(sen)
  vp = VocabParser(lang)
  vocabs = vp.digest(sen)
  print(vocabs)

```

# Development

### Clone project
```
git clone https://github.com/qishe-nlp/sencore.git
```

### Install [poetry](https://python-poetry.org/docs/)

### Install dependencies
```
poetry update
poetry run python -m spacy download en_core_web_md
```

### Execute
```
poetry run parse_to_vocab --help
```

### Build
* Change `version` in `pyproject.toml` and `x2cdict/__init__.py`
* Build python package by `poetry build`

### Publish
* Set pypi test environment variables in poetry, refer to [poetry doc](https://python-poetry.org/docs/repositories/)
* Publish to pypi test by `poetry publish -r test`


# TODO

### Test and Issue
* `tests/*`

### Github action to publish package
* pypi test repo
* pypi repo
