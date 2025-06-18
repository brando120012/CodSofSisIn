import re
def decode_bits(b): b=b.strip("0"); return "" if not b else (lambda T: b.replace("1"*(3*T), "-").replace("1"*T, ".").replace("0"*(7*T), "   ").replace("0"*(3*T), " ").replace("0"*T, ""))(min(len(x) for x in re.findall("1+|0+", b)))
def decode_morse(m): return " ".join("".join(MORSE_CODE[c] for c in w.split()) for w in m.split("   "))

