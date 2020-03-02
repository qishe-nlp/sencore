from sencore.x2cdicts.vocab_semantic import VocabSemantic

class DictAPI:

    @classmethod
    def word(cls, w, pos):
        from googletrans import Translator
        api = Translator()
        origin = cls.get_origin(w, pos) 
        result = api.translate(w, src=cls.origin_lang, dest=cls.target_lang)
        target = cls.get_target(pos, result)
        return VocabSemantic(origin, target)


    @classmethod
    def get_origin(cls, w, pos):
        return {
            "lang": cls.origin_lang,
            "text": w,
            "pos": pos
        }

    @classmethod
    def get_target(cls, pos, result):
        target = {
            "lang": cls.target_lang,
            "explainations": [] 
        }
        target["explainations"].append({
            "pos": pos,
            "meaning": result.text,
            "examples": []
        })
        return target

