from transformers import pipeline
from preprocessing import clean_tweet
from ner_extractor import extract_location  # Import the extract_location function

# Load pre-trained emotion classification model
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def predict_emotion(tweet):
    """Predict the emotion of a tweet after cleaning and extract location if negative."""
    cleaned_tweet = clean_tweet(tweet)  # Clean the tweet
    emotion_result = classifier(cleaned_tweet)
    emotion = emotion_result[0]['label']
    confidence = emotion_result[0]['score']
    
    # Extract location if the tweet is negative
    locations = []
    if emotion == 'NEGATIVE':
        locations = extract_location(tweet)
    
    return emotion, confidence, locations

# Test the classifier with location extraction
if __name__ == "__main__":
    # Accept input tweet from the user
    input_tweet = input("Please enter a tweet: ")
    
    emotion, confidence, locations = predict_emotion(input_tweet)
    print(f"\nTweet: {input_tweet}")
    print(f"Emotion: {emotion} (Confidence: {confidence:.2f})")
    if locations:
        print(f"Extracted Locations: {locations}")
    else:
        print("No locations extracted.")
    print("-" * 50)
