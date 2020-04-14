
import string
from collections import Counter
import matplotlib.pyplot as plt

#This is cleaning process where we remove unwanted char from text.
def Cleaning_Process(text):
    #maketrans_function

    #para1 = list of char that need to be replaced
    #para2 = list of char that with which char need to replace
    #para3 = list of char that need to be delete

    #para1 = "abc"
    #para2 = "xyz"
    #then abc is replaced with xyz



    Last_Text = text.translate(str.maketrans("","",string.punctuation))
    return Last_Text

def Tokenization_Process(text):
    ls = []
    ls = text.split()
    return ls

def Remove_Stop_Word(tokenized_text_ls):
    stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
                  "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
                  "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
                  "these",
                  "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
                  "do",
                  "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
                  "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
                  "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under",
                  "again",
                  "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both",
                  "each",
                  "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so",
                  "than",
                  "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

    final_ls = []

    for wrd in tokenized_text_ls:
        if wrd not in stop_words:
            final_ls.append(wrd)

    return final_ls

def emotion_finding(final_words):


    # 1) Check if the word in the final word list is also present in emotion.txt
    #  - open the emotion file
    #  - Loop through each line and clear it
    #  - Extract the word and emotion using split

    # 2) If word is present -> Add the emotion to emotion_list
    # 3) Finally count each emotion in the emotion list

    emotion_list = []
    with open("emotion.txt","r") as file:
        for line in file:
            clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
            word, emotion = clear_line.split(':')

            if word in final_words:
                emotion_list.append(emotion)


    return emotion_list


def plotting_emotion(dict):

    fig, ax1 = plt.subplots()
    ax1.bar(dict.keys(), dict.values())
    fig.autofmt_xdate()
    plt.savefig('graph.png')
    plt.show()


text = open('DataFile.txt',encoding='utf-8').read()
text = text.lower()
print (text)

text = Cleaning_Process(text)
print(text)

tokenized_text_ls = Tokenization_Process(text)
print(tokenized_text_ls)

final_ls = Remove_Stop_Word(tokenized_text_ls)
print(final_ls)

emotion_list = emotion_finding(final_ls)
print(emotion_list)

print(emotion_list)
w = Counter(emotion_list)
plotting_emotion(w)