class Cipher:
    def __init__(self, text):
        self.translation_dict = self.cipher_table()
        self.text = text

    @staticmethod
    def cipher_table() -> dict:
        """ Returns a dictionary of the secondary alphabet. """

        main_abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        secondary_abc = "@#~\\^><,\"'$&._=;:|/)(][*?!"

        translation_dict = {}

        # Makes a dictionary of every letter.
        for i in range(26):
            translation_dict[secondary_abc[i]] = main_abc[i]

        return translation_dict

    def translate(self) -> str:
        """
        The function translates secondary alphabet from the videos of Unaltered_User.
        :return: The decypher of the secondary alphabet.
        """

        full_string = ""

        # Appends the letters into the string.
        for char in self.text:
            if char not in self.cipher_table():
                full_string += " "

            else:
                full_string += self.cipher_table().get(char)

        return full_string