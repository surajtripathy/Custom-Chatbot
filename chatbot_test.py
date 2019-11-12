import pandas as pd
from random import randint
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from childbot1 import check_id_storage_location
from childbot2 import check_id_time

count_della_started = 0

def get_faq():
    df_faq = pd.read_csv('faq.csv', names = ['questions','answers'])
    return_string = ""
    for i in range(int(df_faq.size/2)):
        return_string = return_string + df_faq['questions'].values[i] + "\n" + df_faq['answers'].values[i] + "\n"
    return return_string

def get_greetings():
    df_greetings = pd.read_csv('greetings.csv', names=['greetings'])
    return (df_greetings['greetings'].values[randint(0,5)])

cust_id_from_prompt = ""
def get_cust_id(temp_cust_id):
    global cust_id_from_prompt
    cust_id_from_prompt = temp_cust_id
    return "Please ask your query now"

def get_reply(inp_msg):
    global cust_id_from_prompt
    df = pd.read_csv('dataset.csv', names=['sentence', 'label'])
    
    sentences = df['sentence'].values
    y = df['label'].values

    vectorizer = CountVectorizer()
    vectorizer.fit(sentences)

    X_train = vectorizer.transform(sentences)

    classifier = LogisticRegression()
    classifier.fit(X_train, y)

    input_msg = inp_msg
    input_msg = [input_msg]
    input_msg_transform = vectorizer.transform(input_msg)
    cust_id = cust_id_from_prompt

    if (classifier.predict(input_msg_transform)[0] == 1):
        return(str(check_id_storage_location(cust_id)),1)
    elif(classifier.predict(input_msg_transform)[0] == 2):
        return(str(check_id_time(cust_id)),2)
