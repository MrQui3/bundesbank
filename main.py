

class bank:
    def __init__(self, m_anzahl, m, registrierung, anzahl_pro_tag, id):
        self.m_anzahl = m_anzahl
        self.m_index = m
        self.registrierung = registrierung
        self.anzahl_pro_tag = anzahl_pro_tag
        self.id = id


class coin:
    def __init__(self, wertigkeit, id):
        self.wertigkeit = wertigkeit
        self.id = id


def read_data_from_file(file_name):
    with open(file_name, 'r') as file:
        m_anzahl, b_anzahl, d_anzahl = map(int, file.readline().split())
        wertigkeiten = list(map(int, file.readline().split()))
        for i in range(len(wertigkeiten)):
            wertigkeiten[i] = coin(wertigkeiten[i], i)
        b = []
        for i in range(b_anzahl):
            anzahl_m, registrierung, anzahl_pro_tag = map(int, file.readline().split())
            m = list(map(int, file.readline().split()))
            b.append(bank(anzahl_m, m, registrierung, anzahl_pro_tag, i))

    return m_anzahl, b_anzahl, d_anzahl, wertigkeiten, b


print(read_data_from_file("a_example.txt"))
a = read_data_from_file('a_example.txt')
print('a')