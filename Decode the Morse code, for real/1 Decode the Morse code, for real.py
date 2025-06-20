# assume MORSE_CODE is preloaded

def decodeBitsAdvanced(bits: str) -> str:
    # 1) trim idle
    bits = bits.strip('0')
    if not bits:
        return ''
    # 2) run‐length encode
    runs = []
    last, cnt = bits[0], 1
    for b in bits[1:]:
        if b == last:
            cnt += 1
        else:
            runs.append((last, cnt))
            last, cnt = b, 1
    runs.append((last, cnt))

    # 3) separate lengths
    ones  = [l for b, l in runs if b == '1']
    zeros = [l for b, l in runs if b == '0']

    # 4) k-means (k=2) on ones → dot/dash centers
    def km2(data):
        c1, c2 = min(data), max(data)
        for _ in range(5):
            g1, g2 = [], []
            for x in data:
                if abs(x-c1) <= abs(x-c2):
                    g1.append(x)
                else:
                    g2.append(x)
            if g1:
                c1 = sum(g1)/len(g1)
            if g2:
                c2 = sum(g2)/len(g2)
        return sorted((c1, c2))
    if ones:
        if len(ones) > 1:
            c_dot, c_dash = km2(ones)
        else:
            c_dot = c_dash = ones[0]
    else:
        c_dot = c_dash = 0

    # 5) k-means (k=3) on zeros → gap centers
    if zeros:
        def km3(data):
            pts = sorted(set(data))
            if len(pts) >= 3:
                c = [pts[0], pts[len(pts)//2], pts[-1]]
            else:
                m = sum(pts)/len(pts)
                c = [pts[0], m, pts[-1]]
            for _ in range(6):
                groups = {0:[],1:[],2:[]}
                for x in data:
                    j = min(range(3), key=lambda j: abs(x-c[j]))
                    groups[j].append(x)
                for j in range(3):
                    if groups[j]:
                        c[j] = sum(groups[j])/len(groups[j])
            return sorted(c)
        cz0, cz1, cz2 = km3(zeros)
    else:
        cz0 = cz1 = cz2 = 0

    # 6) thresholds
    td  = (c_dot  + c_dash) / 2
    t01 = (cz0    + cz1)   / 2
    t12 = (cz1    + cz2)   / 2

    # 7) build Morse literal
    out = []
    for bit, length in runs:
        if bit == '1':
            out.append('.' if length <= td else '-')
        else:
            if length <= t01:
                # intra‐char gap: ignore
                pass
            elif length <= t12:
                out.append(' ')   # between chars
            else:
                out.append('   ') # between words

    morse = ''.join(out).strip()
    # collapse any >3 spaces down to 3
    while '    ' in morse:
        morse = morse.replace('    ', '   ')
    return morse

def decodeMorse(morseCode: str) -> str:
    mc = morseCode.strip()
    if not mc:
        return ''
    words = mc.split('   ')
    decoded = []
    for w in words:
        letters = w.split(' ')
        decoded.append(''.join(MORSE_CODE.get(ch, '') for ch in letters))
    return ' '.join(decoded)


# quick self‐test
if __name__ == "__main__":
    assert decodeMorse(decodeBitsAdvanced('1')) == 'E'
    assert decodeMorse(decodeBitsAdvanced('101')) == 'I'
    raw = (
      "0000000011011010011100000110000001111110100111110011111100000000000"
      "1110111111110111110111110000001011000111111000001111100111011000001"
      "00000"
    )
    assert decodeMorse(decodeBitsAdvanced(raw)) == 'HEY JUDE'
    print("All tests pass!")
