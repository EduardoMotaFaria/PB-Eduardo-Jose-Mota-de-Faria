animais = ["Elefante", "Tigre", "Gato", "Cachorro", "Leão", "Panda", "Coelho", "Cobra", "Jacaré", "Zebra",
           "Águia", "Tubarão", "Urso", "Lobo", "Papagaio", "Arraia", "Coruja", "Cavalo", "Golfinho", "Galo"]

animais.sort()

[print(animal) for animal in animais]

with open("animais.csv", "w", encoding="utf-8") as arquivo:
    arquivo.write("\n".join(animais))
