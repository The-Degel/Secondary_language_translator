def cypher_table() -> dict:
    """ Returns a dictionary of the secondary alphabet. """

    main_abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    secondary_abc = "@#~\\^><,\"'$&._=;:|/)(][*?!"

    translation_dict = {}

    # Makes a dictionary of every letter.
    for i in range(26):
        translation_dict[secondary_abc[i]] = main_abc[i]

    return translation_dict


def translate(secondary_abc_string: str) -> str:
    """
    The function translates secondary alphabet from the videos of Unaltered_User.
    :return: The decypher of the secondary alphabet.
    """

    full_string = ""

    # Appends the letters into the string.
    for char in secondary_abc_string:
        if char not in cypher_table():
            full_string += " "

        else:
            full_string += cypher_table().get(char)

    return full_string


def main():
    """ The function activates the translation function. """

    cyphered_string = input("Enter your string please: ")
    print(translate(cyphered_string))

if __name__ == "__main__":
    main()
