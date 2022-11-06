from Tier import Tier

class Hund(Tier):
    def laufen(self):
        print('laufen')

einTier = Tier()
einTier.laufen()

# von der Datei Tier.py die abstrakte Methode Tier an Hund vererbt wurden