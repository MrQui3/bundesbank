
import math


class bank:
    def __init__(self, m_anzahl, m, registrierung, anzahl_pro_tag, id):
        self.m_anzahl = m_anzahl
        self.m = m
        self.registrierung = registrierung
        self.anzahl_pro_tag = anzahl_pro_tag
        self.id = id
        self.verkauf_zeit = math.ceil(self.m_anzahl / self.anzahl_pro_tag)
        self.gesamt_wert = self.gesamt_wert_berechnen()
        self.prio = self.prio_berechnen()


    def gesamt_wert_berechnen(self):
        gesamt_wert = 0
        a = 0
        for i in range(len(self.m)):
            if self.m[i].besucht:
                continue
            gesamt_wert += self.m[i].wertigkeit
            a += 1

        self.m_anzahl = a
        return gesamt_wert

    def prio_berechnen(self):
        return self.gesamt_wert/self.registrierung

class coin:
    def __init__(self, wertigkeit, id):
        self.wertigkeit = wertigkeit
        self.id = id
        self.besucht = False


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
            coins = []
            for j in range(anzahl_m):
                coins.append(wertigkeiten[m[j]])
            b.append(bank(anzahl_m, coins, registrierung, anzahl_pro_tag, id=i))

    return m_anzahl, b_anzahl, d_anzahl, wertigkeiten, b



m_anzahl, b_anzahl, d_anzahl, wertigkeiten, banken = read_data_from_file('d_tough_choices.txt')

for i in range(b_anzahl):
    banken[i].m = sorted(banken[i].m, key=lambda c: c.wertigkeit, reverse=True)


def alle_beuschten_münzen_löschen(m):
    if len(m) == 0:
        return m
    if m[0].besucht:
        m.pop(0)
        alle_beuschten_münzen_löschen(m)
    return m

rest_registrierung_zeit = 0
registrierte_banken= []
registriertende_bank = None
gescannte_münzen = []

for i in range(d_anzahl):
    if rest_registrierung_zeit == 0:
        gescannte_münzen.append([])
        if len(banken) == 0:
            registriertende_bank = None
        else:
            banken = sorted(banken, key=lambda b: b.prio, reverse=True)
            registriertende_bank = banken[0]
            rest_registrierung_zeit = banken[0].registrierung
            registrierte_banken.append(banken[0])
            banken.pop(0)


    rest_registrierung_zeit -= 1
    for k in range(len(registrierte_banken)):
        if registriertende_bank == registrierte_banken[k]:
            continue
        for j in range(registrierte_banken[k].anzahl_pro_tag):
            m = alle_beuschten_münzen_löschen(registrierte_banken[k].m)
            if len(registrierte_banken[k].m) == 0:
                break

            if registrierte_banken[k].m_anzahl > 0:
                gescannte_münzen[k].append(registrierte_banken[k].m[0].id)
                registrierte_banken[k].m[0].besucht = True
                registrierte_banken[k].m.pop(0)
            else:
                break

a = 0
for i in range(len(registrierte_banken)):
    if len(gescannte_münzen[i]) == 0:
        a += 1



print(f"{len(registrierte_banken)-a}")
for i in range(len(registrierte_banken)):
    if len(gescannte_münzen[i]) == 0:
        continue
    print(f"{registrierte_banken[i].id} {len(gescannte_münzen[i])}")
    print(" ".join(map(str, gescannte_münzen[i])))


