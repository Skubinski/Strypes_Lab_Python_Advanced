import pandas as pd
from nltk.corpus import words as vocab



eng_dict = set(word.lower() for word in vocab.words())
eng_dict.add('bewitched')
eng_dict.add('interchanged')
eng_dict.add('filched')
eng_dict.add('looked')
with open('shakespeare.txt') as file:
    full_text = file.read().split()
    words = [word.lower() for word in full_text if word not in "!.;,"]




df = pd.DataFrame({
    'text': words
})

filtered_words = df[df['text'].str.contains("'")]
filtered_words['corrected'] = filtered_words['text'].str.replace("'", "e")
filtered_words['exists'] = filtered_words['corrected'].isin(eng_dict)


words_count = df['text'].count()
apostroph_words = filtered_words['text'].count()
count_true = 0
count_false = 0

for value in filtered_words['exists']:
    if value == True:
        count_true += 1
    else:
        count_false += 1

print(f"Total words: {words_count}!")
print(f"Total apostrophic words: {apostroph_words}!")
print(f"Total real apostrophic words: {count_true}!")
print(f"Total unreal apostrophic words: {count_false}!")
print(f"Usage of apostrohic words: {(apostroph_words / words_count)*100:.2f}%!")
print(f"Usage of Real apostrohic words: {(count_true / apostroph_words)*100:.2f}%!")
print(f"Usage of Unreal apostrohic words: {(count_false / apostroph_words)*100:.2f}%!")

filtered_words.to_csv('corrected.csv', index=False)

ww = dict(zip(filtered_words['text'], zip(filtered_words['corrected'], filtered_words['exists'])))


new_shakespeere = []
for word in full_text:
    if word in ww.keys() and ww[word][1] == True:
        new_shakespeere.append(ww[word][0])
    else:
        new_shakespeere.append(word)

with open("shakespeare_corrected.txt", "w") as file:
    file.writelines(" ".join(new_shakespeere))








