# Ceasarova sifra

def caesarova_sifra(text, posun):
    abeceda = "abcdefghijklmnopqrstuvwxyz"
    zasifrovana_abeceda = abeceda[posun:] + abeceda[:posun]
    mapa = str.maketrans(abeceda + abeceda.upper(), zasifrovana_abeceda + zasifrovana_abeceda.upper())
    return text.translate(mapa)

text = "Hello, World!"
posun = 3
zasifrovany_text = caesarova_sifra(text, posun)
print("Zašifrovaný text:", zasifrovany_text)



