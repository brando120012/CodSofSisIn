from preloaded import MORSE_CODE

def decode_morse(morse_code):
    # 1) Strip leading/trailing whitespace
    morse_code = morse_code.strip()
    # 2) Split into words on 3 spaces
    words = morse_code.split('   ')
    decoded_words = []
    
    for word in words:
        # 3) Split word into individual character codes on single space
        chars = [c for c in word.split(' ') if c]
        # 4) Decode each code using the MORSE_CODE dict
        decoded = ''.join(MORSE_CODE[c] for c in chars)
        decoded_words.append(decoded)
    
    # 5) Reassemble decoded words with a space
    return ' '.join(decoded_words)
