class Rotamer:
    def __init__(self, residue, index):
        self.residue = residue
        self.index = index

class Residue:
    def __init__(self, index, rotamers):
        self.rotamers = rotamers
        self.index = index
