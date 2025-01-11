from sencore import DeepLAPI

def test_deepl():
  lang = "es"
  t_api = DeepLAPI(lang)
  r = t_api.search("casar")
  print(r)

def test_deepl_with_ctx():
  lang = "es"
  t_api = DeepLAPI(lang)
  r = t_api.search("casar", "¿Tú estás segura de que te quieres casar?")
  print(r)
