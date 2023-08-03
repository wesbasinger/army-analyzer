class Army:

    def __init__(self, name, points):

        self.name = name
        self.points = points

        self.units = []

    def add_unit(self, unit):

        self.units.append(unit)