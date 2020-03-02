class SCModel:
    """
    Container for vocabs, phrases, sentence patterns
    """

    def __init__(self, obj):
        self.obj = obj


    def display(self, options={}):
        print(self.obj)
