from tweepy.streaming import StreamListener # use the library to create stream listener
from tweepy import OAuthHandler # in this case, application-user
from tweepy import Stream
import twitter_credentials

class twStreamer():
    """
    Twitter Streamer:
    Class for streaming and processing live tweets.
    """
    def __init__(self):
        pass # different here

    def stream_tweets(self, twFile, hashTag):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = stdoutListener(twFile)
        #auth = self.autr.authTwapp()
        auth = OAuthHandler(twitter_credentials.KEY, twitter_credentials.KEY_SECRET)
        auth.set_access_token(twitter_credentials.TOKEN, twitter_credentials.TOKEN_SECRET)
        strLive = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords:
        # Streams do not terminate unless the connection is closed, blocking the thread.
        # Tweepy offers a convenient is_async parameter on filter
        # so the stream will run on a new thread.
        strLive.filter(track=hashTag, is_async=True) # edit here

class stdoutListener(StreamListener):
    """
    Twitter stream listener:
    This is a basic listener that just prints received tweets to stdout.
    """
    # The default StreamListener can classify most common twitter messages
    # and routes them to appropriately named methods,
    # but these methods are only stubs.
    def __init__(self, twFile):
        self.twFile = twFile

    def on_data(self, data):
        try:
            print(data)
            with open(self.twFile, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True

    # an error handling method
    def on_error(self, status):
        if status == 420:
            # Returning False on_data method in case rate limit occurs.
            # The 401 Unauthorized error is an HTTP status code
            # that means the page you were trying to access cannot be loaded
            # until you first log in with a valid user ID and password.
            return False
        print(status)

if __name__ == '__main__':
    hashTag_list = ['vogue', 'elle']
    twFile_list = ["tweets_vogue_live.txt", "tweets_elle_live.txt"]
    twitter_streamer = twStreamer()
    for i in range(2):
        twitter_streamer.stream_tweets(twFile_list[i], hashTag_list[i])
# in the real life, we cannot stop the stream, 
# but I tried the following to control the size of the file
# option1: control by length
#        import sys
#        with open(twFile_list[i], 'r') as f:
#            if len(f.readlines()) > 100:
#                sys.exit(0)
# option2: control by time
# I did not find the point to control it
#       import time
#       start = time.time()
#       twitter_streamer.stream_tweets(twFile_list[i], hashTag_list[i])
#       end = time.time()

:stuck_out_tongue:
        
## In this project, I stop the project in 1 minutes in the IDE for now 
