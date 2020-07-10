def no_dups(s):

    # Your code here

    noDupsList = []
    words = {}
    new = s.split()

    # add to noDupsList and words dictionary
    for word in new:
        if word not in words:
            noDupsList.append(word)
            words[word] = 1
    
    # make into string
    result = ""
    for word in noDupsList:
        result += word + " "
    # remove last space
    result = result[:-1]

    print(f"result = {result}")
    return result


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))