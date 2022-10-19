
def process(w):
    output =""
    for ch in w:
        if( ch.isalpha() ):
            output += ch
    return output.lower()
words = set()

string = "All's well that ends well. Bad news travel fast. Well begun is half done. Birds of a feather flock together."

for s in string.split():
    words.add(process(s))

print("사용된 단어의 개수=", len(words))
print(words)