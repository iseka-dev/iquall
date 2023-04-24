# Horacio Andres Chiarella
# 24/04/23

"""
Situación a analizar: Se desea escribir una carta utilizando
letras recortadas de un artículo de una revista. El primer paso es
verificar que en dicho artículo existan todas las letras necesarias
para lograr redactar la carta.
"""


def letter_freq(message: str) -> dict:
    """
    Funcion para determinar la frecuencia de cada letra en un string.
    Solo cuenta caracteres alfabeticos, y los cuenta una unica vez
    asi sean minusculas o mayusculas.
    """
    letter_frequency = {}
    for letter in message.lower():
        if letter.isalpha():
            if letter in letter_frequency:
                letter_frequency[letter] += 1
            else:
                letter_frequency[letter] = 1
    return letter_frequency


def compare_freq(message_freq: dict, journal_freq: dict) -> dict:
    """
    # Funcion que compara dos diccionarios cuyas claves son
    # caracteres alfabeticos y son la cantidad de apariciones
    # de cada uno.
    # Devuelve un diccionario con la diferencia entre cada
    # caracter (solo cuando la cantidad del primero es mayor
    # a la cantidad del segundo).
    """
    missing_letters = {}
    for key in message_freq:
        try:
            if message_freq[key] > journal_freq[key]:
                n_letters_missing = (
                    message_freq[key] - journal_freq[key]
                )
                missing_letters[key] = n_letters_missing
        except KeyError as e:
            missing_letters[key] = message_freq[key]
            print(f"\nKey not found in journal: {e}")
    return missing_letters


if __name__ == "__main__":
    # En primer lugar es necesario determinar el mensaje a enviar
    with open("message.txt", "r") as file:
        message = file.read()
    print("\nMessage to be written:\n", message)

    # Luego es necesario fijar la revista de la cual se tomaran las letras
    with open("journal.txt", "r") as file:
        journal = file.read()
    print("\nJournal with the letters to be used:\n", journal)

    # El primer paso es contar la frecuencia de cada letra en el mensaje.
    letters_in_message = letter_freq(message)
    print("\nLetters frequency in message:\n", letters_in_message)

    # Luego contamos la frecuencia de cada letra en la revistsa
    letters_in_journal = letter_freq(journal)
    print("\nLetters frequency in journal:\n", letters_in_journal)

    # Por ultimo comparamos la frecuencia de cada diccionario
    missing_letters = compare_freq(letters_in_message, letters_in_journal)

    if len(missing_letters) > 0:
        print(
            "\nNo se puede escribir el mensaje ya que faltan los "
            "siguientes caracteres:"
        )
        print("\nCaracteres faltantes: \n", missing_letters)
    else:
        print(
            "\n\nUsted puede escribir el mensaje con los caracteres"
            " de la revista"
        )
