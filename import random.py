import random

class Postava:
  def __init__(self, jmeno, rasa, zdravi, utok, obrana):
    self.jmeno = jmeno
    self.rasa = rasa
    self.zdravi = zdravi
    self.utok = utok
    self.obrana = obrana

  def utok_na(self, protivnik):
    # vypočítat náhodný počet útoků
    pocet_utoku = random.randint(1, 3)
    celkovy_utok = pocet_utoku * self.utok

    # odečíst obranu protivníka od celkového útoku
    skutecny_utok = celkovy_utok - protivnik.obrana

    # pokud by skutečný útok byl menší než nula, nastavit ho na nulu
    if skutecny_utok < 0:
      skutecny_utok = 0

    # odečíst skutečný útok od zdraví protivníka
    protivnik.zdravi -= skutecny_utok

    # vypsat informace o útoku
    print(f"{self.jmeno} útočí na {protivnik.jmeno}! Počet útoků: {pocet_utoku}, Celkový útok: {celkovy_utok}, Skutečný útok: {skutecny_utok}")
  
  def branit_se(self, protivnik):
    # vypočítat náhodný počet útoků
    pocet_utoku = random.randint(1, 2)
    celkovy_utok = pocet_utoku * protivnik.utok

    # odečíst obranu od celkového útoku
    skutecna_obrana = celkovy_utok - self.obrana

    # pokud by skutečná obrana byla menší než nula, nastavit ji na nulu
    if skutecna_obrana < 0:
      skutecna_obrana = 0

    # odečíst skutečnou obranu od zdraví postavy
    self.zdravi -= skutecna_obrana

    # vypsat informace o obraně
    print(f"{self.jmeno} se brání proti {protivnik.jmeno}! Počet útoků: {pocet_utoku}, Celkový útok: {celkovy_utok}, Skutečná obrana: {skutecna_obrana}")

# vytvořit postavy
postava1 = Postava("Gandalf", "kouzelník", 100,) 
