import numpy as np
import math
import codecs
import collections

file = open("C:/Users/user/Desktop/text.txt", "r", encoding='utf-8')
text = file.read()
text = text.lower()
punctuations = [".", ",", "!", "?", ";", ":", "-", "1", "2", "3", "4","5", "6", "7","8","9", "0","—","»","«", " ", "’","/n"]
for k in range(len(punctuations)):
    text = text.replace(punctuations[k], "")# get rid of punctuations



alphabet = np.array(['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я'])
frequency = np.zeros(len(alphabet)) # creating array of rarity for monogram
temporary = np.zeros(len(text))# array for recoded text


for i in range(len(alphabet)):# iterating per alphabet
    for j in range(len(text)): # iteration trought the whole text
        if text[j] == alphabet[i]:# checking for matching
            frequency[i] = frequency[i]+1 # if so plus to rarity
            temporary[j] = i # saving letter code

frequency = frequency/(len(text))

for i in range (len(alphabet)):
    print (alphabet [i]," : ", frequency [i]) 




bigrams_f = np.zeros([33,33])

for k in range (0, len(text) - 1, 1):
        t1 = int(temporary[k])
        t2 = int(temporary[k+1])
        bigrams_f[t1, t2] +=1
       
for i in range(len(alphabet)):
    for j in range(len(alphabet)):
        print(alphabet[i], alphabet[j], ':', bigrams_f[i, j]/(len(text)-1))

  
frequency = frequency[np.nonzero(frequency)]
H1 = -np.dot(frequency, np.log2(frequency)) 
print(H1)
bigrams_f=bigrams_f/(len(text)-1)
bigrams_f = bigrams_f[np.nonzero(bigrams_f)]
H2 = -np.dot(bigrams_f, np.log2(bigrams_f))/2 
print(H2)

bigrams_f1 = np.zeros([33,33])
for k in range (0, len(text) - 1, 2):
        t1 = int(temporary[k])
        t2 = int(temporary[k+1])
        bigrams_f1[t1, t2] +=1


for i in range(len(alphabet)):
    for j in range(len(alphabet)):
        print(alphabet[i], alphabet[j], ':', bigrams_f1[i, j]/(len(text)-1))

bigrams_f1=bigrams_f1/(len(text)-1)
bigrams_f1 = bigrams_f1[np.nonzero(bigrams_f1)]
H21 = -np.dot(bigrams_f1, np.log2(bigrams_f1))/2 
print(H21)