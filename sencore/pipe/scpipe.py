class SCPipe:
    """
    Abstract class for VocabPipe, PhrasePipe, SentencePatternPipe
    """

    def __init__(self, lang="en"):
        """
        Initialize the language and model package to use
        """
        self.lang = lang

    def digest(self, sentence):
        """
        Process sentence into vocabs, phrases and sentence patterns 
        The children class should handle details
        """
        return sentence
