import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def clean_pdf_text(text):
    '''
    Clean and tokenize the text extracted from a pdf file
    :param text: Text extracted from pdf in string
    :return: Tokenized and cleaned text in a list
    '''
    # 1. Remove punctuation
    text_no_punct = text.translate(str.maketrans('', '',string.punctuation))

    # 2. Remove numbers
    text_no_num = ''.join(x for x in text_no_punct if not x.isdigit())

    # 3. Tokenize
    tokens = word_tokenize(text_no_num)
    tokens = [w.lower() for w in tokens]

    # 4. Remove stopwords
    # 4.1. NLTK
    try:
        stop_words = stopwords.words('english')
    except:
        import nltk
        nltk.download('punkt')
        stop_words = stopwords.words('english')

    # 4.2. CUSTOM
    # Add a stopwords.txt file to remove other words
    try:
        exclude_words = []
        f = open('stopwords.txt', 'r')
        for line in f.readlines():
            exclude_words.append(line.strip().lower())
    except:
        exclude_words = []

    # 4.3. Filter the tokenized text with stopwords
    keywords = [w.lower().capitalize() for w in tokens if not w in stop_words and not w in exclude_words]

    # 5. Remove small words under 2 characters
    keywords = [x for x in keywords if len(x) > 2]

    # 6. Un-tokenize
    keyword_string = ''
    for words in keywords:
        keyword_string += "".join(words)+" "

    return keyword_string
