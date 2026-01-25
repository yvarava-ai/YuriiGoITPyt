pets = ["dog", "fish", "cat"]

match pets:
    case ["dog", "cat", _]:
        # Випадок, коли є і собака, і кіт
        print("There's a dog and a cat.")
    case ["dog", "fish", _]:
        # Випадок
        print("There's a dog and a fish.")
    case _:
        # Випадок для інших комбінацій
        print("No dogs.")
