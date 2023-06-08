import random


print("Welcome to the fantasy name generator\n")

first_names = ("Al","Johnrek","Merlphy","Elmlee","Mephistophflores",
               "Vikgraham","Mesmoke","Fornwest","Hacrusher","Badcrawford",
               "Petersoniniar","Gwydellis")

last_names = ("Aumcia","Aumrvey","Firephens","Fangryan","Williamsang",
              "Kellydrinker", "Drottmartin", "Hernananic", "Satanlopez",
                "Ronic", "Dianic", "Gophire")

chosen_first_name = ""
chosen_last_name = ""


while True:
    chosen_first_name = random.choice(first_names)

    chosen_last_name = random.choice(last_names)

    print("\n")
    print("{} {}".format(chosen_first_name, chosen_last_name))
    print("\n")

    try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")

    if try_again.lower() == "n":
        break

input("\nPress Enter to exit.")


