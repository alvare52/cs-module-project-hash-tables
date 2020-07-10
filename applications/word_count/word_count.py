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

    wordList = s.lower().split()
    print(wordList)
            
    # Your code here
    words = {}

    for word in wordList:
    
        key = ""
        # go through each character in the word
        for char in word:
            # ignore weird characters
            if char not in ignoredWords:
                key += char
        
        if key not in words:
            words[key] = 1
        else:
            words[key] += 1

    if "" in words:
        print("CURLYS FOUND")    
        del words[""]
    
    return words


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))