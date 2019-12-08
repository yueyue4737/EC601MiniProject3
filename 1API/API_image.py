# Imports the Twitter APIs library
from twython import Twython
# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

import os
from google.oauth2 import service_account
#export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/My First Project-079a6734c983.json"
credentials_path = os.path.dirname(os.path.realpath(__file__)) + os.sep + "My First Project-079a6734c983.json"
credentials = service_account.Credentials.from_service_account_file(credentials_path)

# languages that NL API supports
SUPPORTED_LANGUAGE = ['zh', 'zh-Hant', 'en', 'fr', 'de', 'it',
                      'ja', 'ko', 'pt', 'es',
                      ]
# Twitter APIs keys

APP_KEY = '5zcnqEcEhTaWdGEWyskQHC4XF'
APP_SECRET = 'jzOLLcqQHpDYLmiSKjiqQTXf6u3vM0RdNeOUDfTrHlx0wSgp8Y'
OAUTH_TOKEN = '1172881526079533056-5oaIJxSfewZOS6pFXVEEhNOWgyNG6L'
OAUTH_TOKEN_SECRET = 'WF8RNwmPefkonUd6HUwv4qJWN9XqjE0PRfM1d5erbmguN'

# Instantiates twitter APIs and google NL API client.
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
client = language.LanguageServiceClient(credentials=credentials)

# program main function begin
while True:
    keyword = input("Please enter a key word you want to search:\n")
    search_result = twitter.search(q=keyword, result_type='popular', include_entities=True)
    # The type of search_result is dict.
    # the first entity is 'statuses'
    statuses = search_result['statuses']  # The type of statuses is list.
    average_attitude = 0
    for status in statuses:  # The type of status is dict.
        tweet_text = status['text']  # The type of tweet_text is string
        tweet_lang = status['lang']  # The type of tweet_lang is string
        print(status['entities'])

        if tweet_lang in SUPPORTED_LANGUAGE:
            document = types.Document(
                content=tweet_text,
                language=tweet_lang,
                type=enums.Document.Type.PLAIN_TEXT,
            )

            # Detects the sentiment of the text
            sentiment = client.analyze_sentiment(document=document).document_sentiment
            average_attitude += sentiment.score * sentiment.magnitude

    average_attitude /= len(statuses)

    if average_attitude < -0.25:
        print("The average attitude on Twitter about " + keyword + " is negative.")
    elif average_attitude < 0.25:
        print("The average attitude on Twitter about " + keyword + " is neutral.")
    else:
        print("The average attitude on Twitter about " + keyword + " is positive.")