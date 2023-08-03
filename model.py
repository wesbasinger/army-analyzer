class Model:

    def __init__(self, name, movement, toughness, save, wounds, leadership, oc):

        self.name = name
        self.movement = movement
        self.toughness = toughness
        self.save = save
        self.wounds = wounds
        self.leadership = leadership
        self.oc = oc

        self.weapons = []