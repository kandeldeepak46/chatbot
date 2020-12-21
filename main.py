# import libraries
from newspaper import Article
import random
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import numpy as np
import warnings

from get_source import get_text_from_url

warnings.filterwarnings("ignore")


def greeting_response(text):
    text = text.lower()
    bot_greetings = [
        "howdy",
        "hey",
        "what's going on",
        "what's good",
        "hello",
        "hey there",
    ]
    user_greetings = [
        "hi",
        "hello",
        "hola",
        "greetings",
        "wassup",
        "hey",
        "how are you",
        "Oh! Hi",
    ]

    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)


def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))

    x = list_var

    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp

    return list_index


# Generate the response
def bot_response(user_input):
    user_input = user_input.lower()  # Convert the users input to all lowercase letters

    sent_tokens = get_text_from_url()
    # Append the users response to the list of sentence tokens
    sent_tokens.append(user_input)
    bot_response = ""  # Create an empty response for the bot
    cm = CountVectorizer().fit_transform(sent_tokens)  # Create the count matrix

    # Get the similarity scores to the users input
    similarity_scores = cosine_similarity(cm[-1], cm)

    # Reduce the dimensionality of the similarity scores
    flatten = similarity_scores.flatten()
    index = index_sort(flatten)  # Sort the index from

    # Get all of the similarity scores except the first (the query itself)
    index = index[1:]

    # Set a flag letting us know if the text contains a similarity score greater than 0.0
    response_flag = 0

    # Loop the through the index list and get the 'n' number of sentences as the response
    j = 0
    for i in range(0, len(index)):
        if flatten[index[i]] > 0.0:
            bot_response = bot_response + " " + sent_tokens[index[i]]
            response_flag = 1
            j = j + 1
        if j > 2:
            break
    # if no sentence contains a similarity score greater than 0.0 then print 'I apologize, I don't understand'
    if response_flag == 0:
        bot_response = bot_response + " " + "I apologize, I don't understand."
        # Remove the users response from the sentence tokens
        sent_tokens.remove(user_input)

    return bot_response


def start_chat():

    # Start the chat
    print(
        "Doc Bot: I am DOCTOR BOT or Doc Bot for short. I will answer your queries about Chronic Kidney Disease. If you want to exit, type Bye!"
    )
    exit_list = ["exit", "see you later", "bye", "quit", "break"]
    while True:
        user_input = input()
        if user_input.lower() in exit_list:

            print("Doc Bot: Chat with you later !")
            break
        else:

            if greeting_response(user_input) != None:

                print("Doc Bot: " + greeting_response(user_input))
            else:

                print("Doc Bot: " + bot_response(user_input))


if __name__ == "__main__":
    start_chat()
