import nltk
from newspaper import Article


def get_text_from_url(
    url="https://www.mayoclinic.org/diseases-conditions/chronic-kidney-disease/symptoms-causes/syc-20354521",
) -> list:

    if url is None:
        raise ValueError("You must enter the url for chatting with bot")

    # Get the article URL
    article = Article(url)
    article.download()  # Download the article
    article.parse()  # Parse the article
    article.nlp()  # Apply Natural Language Processing (NLP)
    corpus = article.text  # Store the article text into corpus

    # Tokenization
    text = corpus
    sentence_tokens = nltk.sent_tokenize(text)  # txt to a list of sentences

    return sentence_tokens
