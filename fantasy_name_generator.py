import random


def generate_name():
    first_names = ("Rossshu","Al","Johnrek","Merlphy","Elmlee","Mephistophflores",
                   "Vikgraham","Mesmoke","Fornwest","Hacrusher","Badcrawford",
                   "Petersoniniar","Gwydellis","Harmmez", "Hatianaka"
                   "Wolda","Fraffolk","Berthelm","Cyne","Cuthbehrt","Wolda","Reda",
                   "Aethrin","Amus","Arsin","Sumuru","Nazuuma","Biumadea")

    last_names = ("Aumcia","Aumrvey","Firephens","Fangryan","Williamsang",
                  "Kellydrinker", "Drottmartin", "Hernananic", "Satanlopez",
                  "Ronic", "Dianic", "Gophire", "De Hollandcourt", "Fireckson"
                  "Tahyrst","Cheawood", "Demoor", "Adham", "Bratun", "Caford", "Famor", 
                  "Wahyrst", "Moford","Adbrycg","Choogate","Brewood","Wawold")

    chosen_first_name = random.choice(first_names)
    chosen_last_name = random.choice(last_names)

    return "{} {}".format(chosen_first_name, chosen_last_name)

def main():
    print("Welcome to the fantasy name generator\n")

    while True:
        print("\n")
        print(generate_name())
        print("\n")

        try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")

        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit.")


if __name__ == "__main__":
    main()



