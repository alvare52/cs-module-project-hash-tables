print("\n--- START ---")

# " : ; , . - + = / \ | [ ] { } ( ) * ^ &
ignoredWords = {"\"": 0,
                ":": 0, 
                ";": 0, 
                ",": 0,
                 ".": 0, 
                 "-": 0,
                 "+": 0,
                 "=": 0,
                 "/": 0,
                 "\\": 0,
                 "|": 0,
                 "[": 0,
                 "]": 0,
                 "{": 0,
                 "}": 0,
                 "(": 0,
                 ")": 0,
                 "*": 0,
                 "^": 0,
                 "&": 0}

# takes in a string and returns a dict that has each word as a key and values are the times that words shows
def word_count(s):
    
    # Your code here
    words = {}
    key = ""
    i = 0
    # first try printing out every word 
    for char in s.lower():
    
        i += 1
        # print(f"i = {i}")

        # Space means end of word? Add word to words (with count) and then reset key
        if char == " " or i == len(s):
            if i == len(s) and char not in ignoredWords:
                print(f"last, i = {i}, char is {char}")
                key += char.lower()

            if key not in words:
                words[key] = 1
            else:
                words[key] += 1
            key = ""
        # inside a word, add the next letter and not an ignored word
        else:
            if char not in ignoredWords:
                key += char.lower()

    return words


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count("Hello the+re world"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))

txt = "Hello  there world!"
x = txt.split()
print(x)