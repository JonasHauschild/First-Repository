import string
#alphabet = {a:i for a,i in zip(string.ascii_letters[:26], range(26))}

#print(alphabet)


letters = 'yzyxaabcafgxiy'
letters = letters.split()
#for guessed_letters in letters:
 #   if "x" not in letters:
  #      letters.remove(guessed_letters)
print(letters)

#[i for i in range(10) if i%2 == 0]


resulte = []
for i in range(10):
    if i%2 == 0:
        resulte.append(i)

print(resulte)


elemse = ['a', 'b', 'c']
for e in elemse:
    print(e)
    elemse.remove(e)
print(elemse)

elems = ['a', 'b', 'c']
i = 0
while i < len(elems):
    e = elems[i]
    print(e)
    elems.remove(e)
    i += 1

mylist = [1,2,3,4,5]

result = []
for i in mylist:
    if i%2==0:
        result.append(i**2)
    else:
        result.append(i ** 3)

print(result)


sentences = [string.ascii_letters]
print(sentences
      )
stopwords = ['for', 'a', 'of', 'the', 'and']

results = []

for sentence in sentences:
    sentence_tokens = []
    for word in sentence.split(' '):
        if word not in stopwords:
            sentence_tokens.append(word)
        results.append(sentence_tokens)

print(results)

#[[word for word in sentence.split(' ') if word not in stopwords] for sentene in sentences]

