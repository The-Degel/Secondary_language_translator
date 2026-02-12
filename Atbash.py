class AtbashCipher:
    def __init__(self, text):
        self.translation_dict = self.atbash_table()
        self.text = text

    @staticmethod
    def atbash_table() -> dict:
        """ Returns the respective reversed letter of each letter input. """

        main_abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        reversed_abc = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

        atbash_dict = {}

        # Makes a dictionary of every letter.
        for letter in range(26):
            atbash_dict[reversed_abc[letter]] = main_abc[letter]

        return atbash_dict

    def atbash_translate(self) -> str:
        """
        The function translates secondary alphabet from the videos of Unaltered_User.
        :return: The decypher of the secondary alphabet.
        """

        full_string = ""

        # Appends the letters into the string.
        for char in self.text:
            if char not in self.atbash_table():
                full_string += " "

            else:
                full_string += self.atbash_table().get(char)

        return full_string