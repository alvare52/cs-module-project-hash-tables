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
                 "[": 0,}

# takes in a string and returns a dict that has each word as a key and values are the times that words shows
def word_count(s):
    
    # Your code here
    words = {}
    key = ""
    # first try printing out every word 
    for char in s:
        if char == " ":
            print("SPACE")
        # end of word? add word to words with count and then reset key
        if char.lower() in ignoredWords:
            if key not in words:
                words[key] = 1
            else:
                words[key] += 1
                print(f"key added = {key}")
            
            key = ""
        
        # inside a word, add the next letter
        else:
            key += char.lower()
    return words


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count("Hello there world"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))