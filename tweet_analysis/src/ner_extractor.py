import spacy

# Load spaCy's pre-trained model for NER
nlp = spacy.load("en_core_web_sm")

def extract_location(tweet):
    """Extract location from the tweet using Named Entity Recognition (NER)."""
    doc = nlp(tweet)
    locations = [ent.text for ent in doc.ents if ent.label_ == "GPE"]  # GPE: Geopolitical Entity
    return locations

# Test location extraction
if __name__ == "__main__":
    test_tweet = "The garbage collection in New York is terrible."
    locations = extract_location(test_tweet)
    print("Extracted Locations:", locations)
