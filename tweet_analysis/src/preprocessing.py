import re

def clean_tweet(tweet):
    """Preprocess and clean the tweet."""
    # Remove URLs
    tweet = re.sub(r"http\S+|www\S+|https\S+", '', tweet, flags=re.MULTILINE)
    # Remove mentions (@user)
    tweet = re.sub(r'@\w+', '', tweet)
    # Remove hashtags (#)
    tweet = re.sub(r'#', '', tweet)
    # Convert to lowercase
    tweet = tweet.lower().strip()
    return tweet

# Test the cleaning function
if __name__ == "__main__":
    test_tweet = "Check out the new park in NYC! #citylife https://example.com @friend"
    print(clean_tweet(test_tweet))
