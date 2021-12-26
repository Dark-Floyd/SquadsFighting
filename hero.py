class Hero:
    def __init__(self, name, status, nature, power):
        self.name = name
        self.status = status
        self.nature = nature
        self.power = power

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def get_nature(self):
        return self.nature

    def set_nature(self, nature):
        self.nature = nature

    def get_power(self):
        return self.power

    def set_power(self, power):
        self.power = power

    def printname(self):
        print(self.name, self.status, self.nature, self.power)
