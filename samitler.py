"""
Bir Packets adinda folder(Paket) yaradin. Icinde samitler adinda bir file (modul) olsun.
Onunda icinde samitleri_al adinda bir funksiya olsun.
Nece calisacaq ?:
Bu folderden colde yerlesen main.py faylimizda bu methodu cagirmali ve icine bir deyer (cumle) gondermeliyik.
Numune cagrilma:
'Salam necesen ... '
netice:
{'s', 'l', 'm', 'n', 'c'} >> heresinden bir dene olsa kifayetdir
"""



def samitleri_al(cumle):
    netice=set()
    samitler=["b","c","d","f","g","h","j","q","k","l","m","n","p","r","s","t","v","y","z","x","w"]
    for herf in cumle:
        if herf.lower() in samitler:
            netice.add(herf.lower())
    print(sorted(netice))