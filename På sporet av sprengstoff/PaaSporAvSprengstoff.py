from sys import stdin


class Kubbe:
    vekt = None
    neste = None

    def __init__(self, vekt):
        self.vekt = vekt
        self.neste = None


#foerste = Kubbe(54)
#kubbe2 = Kubbe(37)
#kubbe3 = Kubbe(100)
#kubbe4 = Kubbe(123)
#kubbe5 = Kubbe(1)
#kubbe6 = Kubbe(54)
#li=[54,37,1,1,123]
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
