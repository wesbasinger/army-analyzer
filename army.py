class Army:

    def __init__(self, name, points):

        self.name = name
        self.points = points

        self.units = []

    def add_unit(self, unit):

        self.units.append(unit)

    def get_total_model_count(self):

        result = 0

        for unit in self.units:

            for model in unit.models:

                result += 1

        return result

    def get_total_wounds(self):

        result = 0

        for unit in self.units:

            for model in unit.models:

                result += model.wounds

        return result

