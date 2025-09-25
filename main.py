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


    return tekst 


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
    else: 
        print ('program se prekida jer tekst nije prociscen.')