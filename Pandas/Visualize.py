import matplotlib.pyplot as plt
from Shakespeere import words, categorizing_words,full_text, df, words_count, apostroph_words, count_true, count_false, count_romeo_julietta, ttr
import numpy as np

def words_visualization():

    names = np.array(['Words', 'Aps Words', 'Existing Words', 'Non-existing Words'])
    values = np.array([words_count, apostroph_words, count_true, count_false])
    colors = np.array(['red', 'blue', 'green', 'yellow'])

    plt.subplot(2, 1, 1)
    plt.bar(names, values, color=colors)
    plt.title("Used Words")
    plt.ylabel("Total Words")
    plt.xlabel("Kind of Words")

    plt.subplot(2,1,2)
    plt.pie(np.array([count_true, count_false]), labels=np.array(['Existing Words', 'Non-existing Words']), colors=np.array(['blue', 'green']), autopct='%1.1f%%')

    plt.suptitle("Words Analysis")
    plt.show()

def romeo_julietta_count_visualization():
    romeo_count, juliet_count = count_romeo_julietta(df)
    total_words = romeo_count + juliet_count
    plt.bar(np.array(['Total count', 'Romeo count', 'Juliet count']), np.array([total_words, romeo_count, juliet_count]), color=np.array(['red','blue', 'pink']))
    plt.title("Romeo and Juliet Count")
    plt.xlabel('Names')
    plt.ylabel('Values')
    plt.show()

def ttr_visualization():
    ttr_percent, total_words, unique_words = ttr(full_text)

    plt.bar(np.array(['Total words', 'Unique words', "TTR (%)"]), np.array([total_words, len(unique_words), ttr_percent]), color=np.array(['red','blue', 'green']))
    plt.title("TTR (%)")
    plt.xlabel("Words")
    plt.ylabel("Values")
    plt.show()

def categorized_words_visualization():

    categories_count_dict = categorizing_words(words)

    plt.subplot(2, 1, 1)
    plt.bar(np.array([key for key in categories_count_dict.keys()]), np.array([value for value in categories_count_dict.values()]))
    plt.title("Words By Category in Segment")
    plt.xlabel("Categories")
    plt.ylabel("Count")

    plt.subplot(2, 1, 2)
    plt.pie(np.array([value for value in categories_count_dict.values()]), labels=np.array([key for key in categories_count_dict.keys()]))

    plt.suptitle("WORD ANALYSIS")
    plt.show()


# words_visualization()
# romeo_julietta_count_visualization()
# ttr_visualization()
categorized_words_visualization()

