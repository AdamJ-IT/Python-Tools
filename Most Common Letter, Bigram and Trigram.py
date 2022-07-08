print("Please input text to be analysed")
text = input()

stripText = text.replace(" ","")

# Hard coded language frequencies


print("""-------------------------------------------------------------""")
print("Single Letter Frequencies")
print("""-------------------------------------------------------------""")
#This generates the dictionary of letter frequency of the users input 
userFreq1  = {}

for i in stripText:
    if i in userFreq1:
        userFreq1[i] +=1
    else:
        userFreq1[i]=1
        
w = {k: v for k, v in sorted(userFreq1.items(), reverse=True, key=lambda item: item[1])}
print(w)


print("""-------------------------------------------------------------""")
print("Bigram Frequencies")
print("""-------------------------------------------------------------""")
#search frequencies of pairs of letters

bigram_freq = {}
length = len(stripText)
for i in range(length-1):
    bigram = (stripText[i], stripText[i+1])
    if bigram not in bigram_freq:
        bigram_freq[bigram] = 0
    bigram_freq[bigram] += 1

x = {k: v for k, v in sorted(bigram_freq.items(), reverse=True, key=lambda item: item[1])}
print(x)


print("""-------------------------------------------------------------""")
print("Trigram Frequencies")
print("""-------------------------------------------------------------""")

#search frequencies of triples of letters 
trigram_freq ={}
length = len(stripText)
for i in range(length-2):
    trigram = (stripText[i], stripText[i+1], stripText[i+2])
    if trigram not in trigram_freq:
        trigram_freq[trigram] = 0
    trigram_freq[trigram] += 1

y = {k: v for k, v in sorted(trigram_freq.items(), reverse=True, key=lambda item: item[1])}
print(y)

