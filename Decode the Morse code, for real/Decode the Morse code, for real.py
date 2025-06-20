# Diccionario Morse (mapea de código Morse a letra)
MORSE_CODE = { 
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', 
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', 
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', 
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', 
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', 
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', 
    '...--': '3', '....-': '4', '.....': '5', '-....': '6', 
    '--...': '7', '---..': '8', '----.': '9'
}

# Creamos el diccionario inverso para pasar de letra a Morse
LETTER_TO_MORSE = {v: k for k, v in MORSE_CODE.items()}

def binary_to_text(binary_str: str) -> str:
    """
    Convierte una cadena binaria (sin espacios u opcionalmente con ellos)
    en un mensaje de texto utilizando la codificación ASCII de 8 bits.
    """
    # Eliminar espacios adicionales (si existen)
    binary_str = binary_str.replace(" ", "")
    text = ""
    # Procesar cada bloque de 8 bits
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8]
        if len(byte) < 8:
            # Si el último bloque no tiene 8 bits, se ignora
            break
        text += chr(int(byte, 2))
    return text

def text_to_morse(text: str) -> str:
    """
    Convierte un mensaje de texto en su correspondiente código Morse.
    Las letras se separan mediante un espacio y las palabras mediante 3 espacios.
    """
    # Convertir el mensaje a mayúsculas para coincidir con el diccionario
    text = text.upper()
    morse_words = []
    for word in text.split():
        morse_letters = []
        for letter in word:
            code = LETTER_TO_MORSE.get(letter, '')
            if code:
                morse_letters.append(code)
        morse_words.append(" ".join(morse_letters))
    return "   ".join(morse_words)

# Función de test simple para verificar la salida
def testAndPrint(got, expected):
    if got == expected:
        print("Test passed!")
    else:
        print(f"Got '{got}', expected '{expected}'")

if __name__ == "__main__":
    # Cadena binaria de ejemplo (cada grupo de 8 bits representa un carácter ASCII)
    binary_message = (
        "01001000"  # H (72)
        "01000101"  # E (69)
        "01011001"  # Y (89)
        "00100000"  # espacio (32)
        "01001010"  # J (74)
        "01010101"  # U (85)
        "01000100"  # D (68)
        "01000101"  # E (69)
    )
    
    # 1. Convertimos la cadena binaria a texto
    text_message = binary_to_text(binary_message)
    print("Texto:", text_message)
    
    # 2. Convertimos el mensaje de texto a código Morse
    morse_message = text_to_morse(text_message)
    print("Código Morse:", morse_message)
    
    # Test: Se espera "HEY JUDE" de la conversión de binario a texto
    testAndPrint(text_message, "HEY JUDE")