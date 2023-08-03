class Unit:

    def __init__(self, name):

        self.name = name
        self.models = []

    def add_model(self, model):

        self.models.append(model)
