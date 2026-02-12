from Translator import Cipher
from Atbash import AtbashCipher
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import selenium.common.exceptions
from time import sleep as wait


def translator(cipher_text) -> str:
    """
    Translates the secondary language.
    :return: The encrypted text.
    """

    # Translates the text.
    cipher_instance = Cipher(cipher_text)
    encrypted_text = cipher_instance.translate()

    return encrypted_text


def atbash_translator(atbash_input) -> str:
    """
    Translates atbash ciphers.
    :param atbash_input: The atbash encoded string.
    :return: The deciphered string.
    """

    # Translates the text.
    atbash_instance = AtbashCipher(atbash_input)
    solved_atbash = atbash_instance.atbash_translate()

    return solved_atbash


def cipher_finder(driver, encrypted_text, key) -> str:
    """
    This function uses the cipher-identifier site to find the cipher used for the encrypted text.
    :param driver: The Chrome driver.
    :param encrypted_text: The string we got from the translator function.
    :param key: The key of the cipher (if exists)
    :return: The cipher used.
    """

    # Opens the website.
    driver.get("https://www.dcode.fr/cipher-identifier&v5")

    # Waits for the page to load.
    wait(1)

    # Finds the textbox and prints the encrypted text into it.
    driver.find_element(By.NAME, "ciphertext").send_keys(encrypted_text)

    # Enters the keyword if it exists.
    if key != "":
        driver.find_element(By.NAME, "clues").send_keys(key)

    # Presses the ANALYZE button.
    driver.find_element(By.XPATH, "//button[@data-post='ciphertext,clues']").click()

    # Wait for the results to load.
    wait(3)

    # Returns the probable cipher to use.
    best_cipher_choice = driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]").text

    return best_cipher_choice


def decrypter(driver, encrypted_text, key, cipher_choice) -> str:
    """
    This function uses the chosen site (from cipher_finder) to decrypt the message.
    :param driver: The Chrome driver.
    :param encrypted_text: The string we got from the translator function.
    :param key: The key of the cipher (if exists)
    :param cipher_choice: The used cipher.
    :return: The decrypted message.
    """

    # Access the new site.
    new_link = f'{"-".join(cipher_choice.split())}&v5'.lower()
    driver.get(f'https://dcode.fr/{new_link}')

    # Wait for the page to load.
    wait(1)

    # Clears the textbox.
    textbox = driver.find_element(By.NAME, "ciphertext")
    textbox.clear()

    # Finds the textbox and prints the encrypted text into it.
    driver.find_element(By.NAME, "ciphertext").send_keys(encrypted_text)

    # Enters the key if it exists, otherwise prints a message.
    try:
        driver.find_element(By.NAME, "key").send_keys(key)

    except selenium.common.exceptions.NoSuchElementException:
        pass

    # Press the decrypt button.
    driver.find_element(By.CSS_SELECTOR, "button[data-post='ciphertext,alphabet,hebraic_alphabet']").click()

    # Wait for the results to load.
    wait(2)

    # Returns the decrypted message.
    return driver.find_element(By.XPATH, "//div[@class='result']").text


def website(ciphered_string, key):
    """
    Sets the website driver and the functionality of the website itself.
    :param ciphered_string: The string we got from the translator function.
    :param key: The key of the cipher (if exists)
    """

    encrypted_text = translator(ciphered_string)

    # Runs the service (the Chrome "window").
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=service, options=options)

    # Finds the cipher used.
    cipher_choice = cipher_finder(driver, encrypted_text, key)

    # Returns the decrypted text.
    print(f'\n{decrypter(driver, encrypted_text, key, cipher_choice)}')


def main():
    """ The function activates the translation function. """

    ciphered_string = input("Enter your string please: ")
    key = input("\nEnter the key used for this decryption.\n"
                "If there is none, please press Enter: ")

    website(ciphered_string, key)

    # --- WRITE AN OPTION FOR ATBASH WITH THE SECONDARY LANGUAGE + ADD IT AS A 1ST OPTION --- #

    # --- USE THE CURRENT INPUTS AND ADD THE CIPHER IDENTIFIER AS A 2ND OPTION --- #

if __name__ == "__main__":
    main()

