STOP_WORDS = ['i', 'u', 'na', 'je', 'se', 'su', 's', 'za', 'o', 'a', 'pa', 'te', 'li', 'da', 'ali', 'bi', 'bio', 'bila', 'što', 'ga', 'mu', 'joj', 'ih']
def ucitaj_tekst(filepath):
    try:
    #ovdje ide logika za čitanje datoteke
        with open (filepath,'r',encoding='utf-8') as file:
         sadrzaj = file.read()
        return sadrzaj
    except FileNotFoundError:
        print(f'greška: Datoteka na putanji {filepath} ne postoji.')
        return None #vraća prazan skup podataka, ako ne nađe datoteku

#funkcija koja pročišćava tekst
def ocisti_tekst(tekst):
    #ovdje ide logika za pročišćavanje teksta
    tekst = tekst.lower()
    interpunkcija={',','.',':',';','!','?','"',"'",'(',')',}
    for znak in interpunkcija:
        tekst = tekst.replace(znak, '')
    lista_rijeci = tekst.split()
    return lista_rijeci

#funkcija za brojanje frekvecnciju rjeci u tekstu
def broji_frekvenciju(lista_rijeci):
    #1. kreirati prazan rječnik koji će čuvati rezultate 
    rjecnik_frekvencija = {}
    #2. proći kroz svaku riječ u primljenoj listi
    for rijec in lista_rijeci:
        if rijec in rjecnik_frekvencija:
            rjecnik_frekvencija[rijec] += 1
        else:
            rjecnik_frekvencija[rijec] = 1
    return rjecnik_frekvencija
#Čišćenje teksta od veznika i sličih "nebitnih" riječi
def ukloni_stop_words(rjecnik_frekvencija, stop_words_lista):
    ocisceni_rjecnik = {}
    for rijec, frekvencija in rjecnik_frekvencija.items():
        if rijec not in STOP_WORDS:
            ocisceni_rjecnik[rijec] = frekvencija
    return ocisceni_rjecnik

def ocisti_stop_words (lista_rjeci):
    for rijec in lista_rjeci:
        if rijec in STOP_WORDS:
            lista_rjeci.remove(rijec)
    return lista_rjeci

#sortiranje 
def sortiraj_i_ispisi(rjecnik_frekvencija):
    sortiraj_i_ispisi = sorted(rjecnik_frekvencija.items(), key=lambda item: item[1], reverse=True)
    return sortiraj_i_ispisi

#glavni dio programa
if __name__ == '__main__':
    filepath = 'tekst.txt'
    print(f'učitavam tekst iz datoteke :{filepath}')

    ucitani_tekst = ucitaj_tekst(filepath)

    if ucitani_tekst:
        print('\ntekst uspješno učitan. slijedi ispis sadržaja:')
        print('-' * 40)
        print(ucitani_tekst)
        print('-' * 40)
    else:
        print('program se prekida jer tekst nije učitan.')
    
    procisceni_tekst = ocisti_tekst(ucitani_tekst)
    if procisceni_tekst:
        print ('procisceni tekst je:')
        print('-' * 40)
        print(procisceni_tekst)
        print('-' * 40)
        print(ucitani_tekst.__len__())

        cist_tekst = ocisti_stop_words(procisceni_tekst)

        #novi dio - pozivamo novu funkciju
        print("brojanje frekvencije riječi u tekstu:")
        frekvencije = broji_frekvenciju(cist_tekst)
        print("Brojanje završeno.")
        # ispisujemo rezultate da vidimo da li je sve ok
        print('\n--- Rječnik frekvencija  ---')
        print(frekvencije)
        print('---------------------------')
        #sortiranje
        broj_rijeci = sortiraj_i_ispisi(frekvencije)
    
    else: 
        print ('program se prekida jer tekst nije prociscen.')

    if broj_rijeci:
        
        print("-" * 50)
        print(broj_rijeci)
        print("-" * 50)
    else:
        print("neka greška se dogodila.")
    
