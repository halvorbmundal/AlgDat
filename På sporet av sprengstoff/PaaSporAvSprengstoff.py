from sys import stdin


class Kubbe:
    vekt = None
    neste = None

    def __init__(self, vekt):
        self.vekt = vekt
        self.neste = None

def spor(kubbe):
    a = 0
    k = kubbe
    while k is not None:
        if k.vekt>a:
            a=k.vekt
        k = k.neste
    return a



# Oppretter lenket liste
forste = None
siste = None
for linje in stdin:  #stdin
    forrige_siste = siste
    siste = Kubbe(int(linje))
    if forste == None:
        forste = siste
    else:
        forrige_siste.neste = siste

# Kaller loesningsfunksjonen og skriver ut resultatet
print(spor(forste))
