from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import os
from google.oauth2 import service_account
#export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/My First Project-77c5622a5066.json"
credentials_path = os.path.dirname(os.path.realpath(__file__)) + os.sep + "My First Project-77c5622a5066.json"
credentials = service_account.Credentials.from_service_account_file(credentials_path)

from google.cloud import language

"""Analyze file with Google NLP
Returns:
    string -- Reaction/Sentiment of the text.
"""
def analyze_text(file_to_analyze):
    # Instantiates a client
    client = language.LanguageServiceClient(credentials=credentials)

    # The text to analyze
    with open(file_to_analyze, 'r') as f:
            # Instantiates a plain text document.
            content = f.read()

    document = types.Document(
        content=content,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    print('Text: {}'.format(content))
    print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

    reaction = get_reaction(sentiment.score, sentiment.magnitude)
    print(reaction)

"""Get the Reaction based off score and magnitude
score: float, value from -1(Negative) to 1 (Positive)
magnitude: float, value from 0 to +inf, indicating strength of score
Returns:
    string: reaction of text
"""
def get_reaction(score, magnitude):
    reaction = 'Neutral'
    if score >= 0.3:
        if magnitude >= 3:
            reaction = 'Clearly Positive'
        elif 1 <= magnitude < 3:
            reaction = 'Positive'
        else:
            reaction = 'Slightly Positive'

    elif score <= -0.3:
        if magnitude >= 3:
            reaction = 'Clearly Negative'
        elif 1 <= magnitude < 3:
            reaction = 'Negative'
        else:
            reaction = 'Slightly Negative'

    elif -.3 < score < .3:
        if magnitude >= 3:
            reaction = 'Mixed'
        else:
            reaction = 'Neutral'

    return reaction

if __name__ == "__main__":
    #file_to_analyze = 'tweetsV.txt'
    file_to_analyze = 'tweetsE.txt'

    analyze_text(file_to_analyze)
