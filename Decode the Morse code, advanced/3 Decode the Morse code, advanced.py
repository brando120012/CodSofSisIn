import re
M = {'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z','-----':'0','.----':'1','..---':'2','...--':'3','....-':'4','.....':'5','-....':'6','--...':'7','---..':'8','----.':'9',".-.-.-":".","--..--":",","..--..":"?","'.----.":"'", "-.-.--":"!","-..-.":"/","-.--.":"(", "-.--.-":")",".-...":"&","---...":":","-.-.-.":";","-...-":"=",".-.-.":"+", "-....-":"-","..--.-":"_",".-..-.":'"',"...-..-":"$",".--.-.":"@"}
I = {v: k for k, v in M.items()}
def decode_bits(bits):
    b = bits.strip('0')
    if not b: return ""
    groups = re.findall(r'(1+|0+)', b)
    unit = min(len(g) for g in groups)
    code = ""
    for g in groups:
        n = len(g)//unit
        if g[0]=='1': code += '.' if n==1 else '-' if n==3 else ''
        else:
            if n==3: code += ' '
            elif n==7: code += '   '
    return code
def decode_morse(morse):
    return " ".join("".join(M.get(s,"") for s in w.split()) for w in morse.strip().split("   "))
def text_to_morse(text):
    return "   ".join(" ".join(I[c.upper()] for c in word if c.upper() in I) for word in text.split())
def morse_to_bits(morse):
    return "0000000".join("000".join("0".join("111" if s=='-' else "1" for s in letter) for letter in word.split()) for word in morse.split("   "))
if __name__=='__main__':
    text = "HEY JUDE"
    morse = text_to_morse(text)
    bits  = morse_to_bits(morse)
    print(text)
    print(morse)
    print(bits)
    print(decode_morse(decode_bits(bits)))
