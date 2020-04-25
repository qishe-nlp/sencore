class Parser:
  """
  Abstract class for VocabParser, PhraseParser, SentencePatternParser
  """

  def __init__(self, lang="en"):
    """
    Initialize the language
    """
    self.lang = lang

  def digest(self, sentence):
    """
    Process sentence into vocabs, phrases and sentence patterns 
    The children class should handle details
    """
    raise Exception("You have to implement method {}!!!".format("digest"))
      
