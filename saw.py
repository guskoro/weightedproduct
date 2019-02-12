class Laptop:
    def __init__(self, merk):
        self._merk       = merk
        self._attributes = []
        self._total      = None

    @property
    def merk(self):
        return self._merk

    @merk.setter
    def setMerk(self, merk):
        self._merk = merk

    @property
    def attributes(self):
        return self._attributes

    @attributes.setter
    def setAttributes(self, attributes):
        self._attributes = attributes

    def addAtribute(self, attribute):
        self.attributes.append(attribute)

    @property
    def total(self):
        return self._total

    def setTotal(self, total):
        self._total = total

class Attribute:
    def __init__(self, name, bobot, maxmin, value):
        self._name      = name
        self._bobot     = bobot
        self._value     = value
        self._maxmin    = maxmin
        self._max_val   = 0
        self._min_val   = 0
        self._value_normalization = None
        self._rank_value          = None

    @property
    def name(self):
        return self._name

    def setName(self, name):
        self._name = name

    @property
    def bobot(self):
        return self._bobot

    def setBobot(self, bobot):
        self._bobot = bobot

    @property
    def maxmin(self):
        return self._maxmin

    def setMaxmin(self, maxmin):
        self._maxmin = maxmin

    @property
    def max_val(self):
        return self._max_val

    def setMax_val(self, max_val):
        self._max_val = max_val

    @property
    def min_val(self):
        return self._min_val

    def setMin_val(self, min_val):
        self._min_val = min_val

    @property
    def value(self):
        return self._value

    def setValue(self, value):
        self._value = value

    @property
    def value_normalization(self):
        return self._value_normalization

    def setValue_normalization(self, value_normalization):
        self._value_normalization = value_normalization

    @property
    def rank_value(self):
        return self._rank_value

    def setRank_value(self, rank_value):
        self._rank_value = rank_value


def main():
    print("Program SAW Beny Gugus Dita\n")
    laptops = []
    laptops = inputData(laptops)

    showData(laptops)
    setMinMax(laptops)
    normalisasi(laptops)
    showNormalization(laptops)
    ranking(laptops)
    showRanking(laptops)
    total(laptops)
    showTotal(laptops)
    hasil(laptops)

def normalisasi(laptops):
    for i in range(len(laptops)):
        for j in range(len(laptops[i].attributes)):
            if laptops[i].attributes[j].maxmin == 0:
                laptops[i].attributes[j].setValue_normalization(round(laptops[i].attributes[j].min_val / laptops[i].attributes[j].value, 2))
            if laptops[i].attributes[j].maxmin == 1:
                laptops[i].attributes[j].setValue_normalization(round(laptops[i].attributes[j].value / laptops[i].attributes[j].max_val, 2))

def ranking(laptops):
    for i in range(len(laptops)):
        for j in range(len(laptops[i].attributes)):
            laptops[i].attributes[j].setRank_value(round(laptops[i].attributes[j].bobot * laptops[i].attributes[j].value_normalization, 2))

def total(laptops):
    for i in range(len(laptops)):
        temptotal = 0
        for j in range(len(laptops[i].attributes)):
            temptotal = temptotal + laptops[i].attributes[j].rank_value
        laptops[i].setTotal(temptotal)

def hasil(laptops):
    result = 0
    result_itr = None
    for i in range(len(laptops)):
        if laptops[i].total > result:
            result = laptops[i].total
            result_itr = i
    print("\nMerk yang disarankan adalah ", end='')
    print(laptops[result_itr].merk)

def setMinMax(laptops):
    min_attr = [999999, 999999, 999999, 999999, 999999, 999999]
    max_attr = [0, 0, 0, 0, 0, 0]
    for i in range(len(laptops)):
        for j in range(len(laptops[i].attributes)):
            if laptops[i].attributes[j].value < min_attr[j]:
                min_attr[j] = laptops[i].attributes[j].value
            if laptops[i].attributes[j].value > max_attr[j]:
                max_attr[j] = laptops[i].attributes[j].value

    for i in range(len(laptops)):
        for j in range(len(laptops[i].attributes)):
            laptops[i].attributes[j].setMin_val(min_attr[j])
            laptops[i].attributes[j].setMax_val(max_attr[j])

    print("\nMinimum   |", end='')
    for i in range(len(min_attr)):
        print(" ", min_attr[i], " |", end='')
    print()
    print("Maximum   |", end='')
    for i in range(len(max_attr)):
        print(" ", max_attr[i], " |", end='')
    print("\n")


def showData(laptops):
    for k in range(len(laptops)):
        print(laptops[k].merk, " | " ,laptops[k].attributes[0].value, " | ",laptops[k].attributes[1].value, " | ",laptops[k].attributes[2].value, " | ",laptops[k].attributes[3].value, " | ",laptops[k].attributes[4].value, " | ",laptops[k].attributes[5].value, " |")

def showNormalization(laptops):
    print("Hasil Normalisasi")
    for k in range(len(laptops)):
        print(laptops[k].merk, " | " ,laptops[k].attributes[0].value_normalization, "\t|\t",laptops[k].attributes[1].value_normalization, "\t|\t",laptops[k].attributes[2].value_normalization, "\t|\t",laptops[k].attributes[3].value_normalization, "\t|\t",laptops[k].attributes[4].value_normalization, "\t|\t",laptops[k].attributes[5].value_normalization, "\t|")

def showRanking(laptops):
    print("\nHasil Ranking")
    for k in range(len(laptops)):
        print(laptops[k].merk, " | " ,laptops[k].attributes[0].rank_value, "\t|\t",laptops[k].attributes[1].rank_value, "\t|\t",laptops[k].attributes[2].rank_value, "\t|\t",laptops[k].attributes[3].rank_value, "\t|\t",laptops[k].attributes[4].rank_value, "\t|\t",laptops[k].attributes[5].rank_value, "\t|")

def showTotal(laptops):
    print("\nHasil Total")
    for k in range(len(laptops)):
        print(laptops[k].merk, " | ",laptops[k].attributes[0].rank_value, "\t|\t",laptops[k].attributes[1].rank_value, "\t|\t",laptops[k].attributes[2].rank_value, "\t|\t",laptops[k].attributes[3].rank_value, "\t|\t",laptops[k].attributes[4].rank_value, "\t|\t",laptops[k].attributes[5].rank_value, "\t=\t", laptops[k].total, "\t|")

def inputData(laptops):

    a = input('Masukkan bobot Prosessor: ')
    b = input('Masukkan bobot VGA: ')
    c = input('Masukkan bobot Layar: ')
    d = input('Masukkan bobot RAM: ')
    e = input('Masukkan bobot Jenis HD: ')
    f = input('Masukkan bobot Harga: ')

    merk1 = Laptop("Asus 12A")
    merk1.addAtribute(Attribute("Speed Processor", float(a), 1, 5.0))
    merk1.addAtribute(Attribute("VGA", float(b), 0, 5.0))
    merk1.addAtribute(Attribute("Layar", float(c), 1, 7.0))
    merk1.addAtribute(Attribute("RAM", float(d), 1, 7.5))
    merk1.addAtribute(Attribute("Jenis HD", float(e), 1, 7.0))
    merk1.addAtribute(Attribute("Harga", float(f), 0, 4.0))
    laptops.append(merk1)

    merk2 = Laptop("Asus 12B")
    merk2.addAtribute(Attribute("Speed Processor", float(a), 1, 6.0))
    merk2.addAtribute(Attribute("VGA", float(b), 0, 8.0))
    merk2.addAtribute(Attribute("Layar", float(c), 1, 7.0))
    merk2.addAtribute(Attribute("RAM", float(d), 1, 8.2))
    merk2.addAtribute(Attribute("Jenis HD", float(e), 1, 7.0))
    merk2.addAtribute(Attribute("Harga", float(f), 0, 4.7))
    laptops.append(merk2)

    merk3 = Laptop("Asus 12C")
    merk3.addAtribute(Attribute("Speed Processor", float(a), 1, 7.0))
    merk3.addAtribute(Attribute("VGA", float(b), 0, 8.3))
    merk3.addAtribute(Attribute("Layar", float(c), 1, 8.7))
    merk3.addAtribute(Attribute("RAM", float(d), 1, 7.5))
    merk3.addAtribute(Attribute("Jenis HD", float(e), 1, 8.2))
    merk3.addAtribute(Attribute("Harga", float(f), 0, 6.5))
    laptops.append(merk3)

    merk4 = Laptop("Asus 12D")
    merk4.addAtribute(Attribute("Speed Processor", float(a), 1, 7.0))
    merk4.addAtribute(Attribute("VGA", float(b), 0, 6.2))
    merk4.addAtribute(Attribute("Layar", float(c), 1, 8.7))
    merk4.addAtribute(Attribute("RAM", float(d), 1, 7.5))
    merk4.addAtribute(Attribute("Jenis HD", float(e), 1, 7.0))
    merk4.addAtribute(Attribute("Harga", float(f), 0, 6.5))
    laptops.append(merk4)

    merk5 = Laptop("Asus 12E")
    merk5.addAtribute(Attribute("Speed Processor", float(a), 1, 6.5))
    merk5.addAtribute(Attribute("VGA", float(b), 0, 7.3))
    merk5.addAtribute(Attribute("Layar", float(c), 1, 7.5))
    merk5.addAtribute(Attribute("RAM", float(d), 1, 8.7))
    merk5.addAtribute(Attribute("Jenis HD", float(e), 1, 8.8))
    merk5.addAtribute(Attribute("Harga", float(f), 0, 8.5))
    laptops.append(merk5)

    return laptops

if __name__ == "__main__":
    main()