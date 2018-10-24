#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "113114562-HUW606EeFCAPQnSdSrERbnTDU9HZdrQU4faqHUTB"
access_token_secret = "d5qpfjnBows7PazTZt3z0FD1ltHrbl7pv3yEWsD557Mqk"
consumer_key = "Yq2RabQNxOekM4uYF7GllNgvl"
consumer_secret = "xZVD0IhxEegSDXmY68zhld858gbJW9syOoFLx8rrkoD66RhVe7"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

	#This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords
    stream.filter(track=['Lloyds', 'HSBC', 'Barclays', 'Halifax', 'Santander', 'Monzo', 'Revolut', 'Atom', 'Metro Bank'])


