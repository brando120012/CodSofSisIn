def rgb(r, g, b):
    # Clamp the values between 0 and 255 and convert each value
    # to its uppercase two-digit hexadecimal representation.
    return f"{max(0, min(255, r)):02X}{max(0, min(255, g)):02X}{max(0, min(255, b)):02X}"
