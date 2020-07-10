# suppose you have a bunch of data, and you want to transform it, you know what it should transform to

# substitute one letter for another
# Goal: Write an encode() function to scramble a string it's given

# need to change one character into another
# map from one character to another

# use that to change an entire string into another

encode_table = {"A": "M",
"B": "N",
"C": "B",
"D": "V",
"E": "C",
"F": "X",
"G": "Z",
"H": "L",
"I": "K",
"J": "J",
"K": "H",
"L": "G",
"M": "F",
"N": "D",
"O": "S",
"P": "A",
"Q": "P",
"R": "O",
"S": "I",
"T": "U",
"U": "Y",
"V": "T",
"W": "R",
"X": "E",
"Y": "W",
"Z": "Q"}

decode_table = {}

# decode_table = {v:k for k, v in encode_table.items()}
def build_decode(encoding_table):
    for key, value in encode_table.items():
        decode_table[value] = key

def decode(s):
    decoded_string = ""
    for character in s:
        if character not in decode_table:
            decoded_string += character
        else:
            # for each character, look up its mapping
            unscrambled_character = decode_table[character]
            #build our return string
            decoded_string += unscrambled_character
    return decoded_string

def encode(s):
    encoded_string = ""

    # iterate over the given string
    s = s.upper()
    for character in s:
        if character not in encode_table:
            encoded_string += character
        else:
            # for each character, look up its mapping
            scrambled_character = encode_table[character]
            # build our return string
            encoded_string += scrambled_character
    return encoded_string

print("\n---START---\n")
encoded = encode("Hail Caesar, we who are about to die salute thee")
print(f"encoded = {encoded}")
build_decode(encode_table)
decoded = decode(encoded)
print(f"decoded = {decoded}")
print("\n---END---\n")