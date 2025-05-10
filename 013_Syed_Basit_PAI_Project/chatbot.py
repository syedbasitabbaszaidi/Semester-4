import re
import nltk
from nltk.chat.util import Chat,reflections
import joblib
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords , wordnet
import re
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from tensorflow.keras.models import load_model # type: ignore

model = load_model('news_model.h5')

# model = joblib.load('news_model.joblib')
vector = joblib.load('news_vectorizer.joblib')

pairs = [
    [r"(?i).*hello.*|.*hi.*|.*hey.*",
     ["Hello! I'm your Fake News Detection Assistant. Want me to check a news story?",
      "Hi there! I can help you verify news articles. How can I assist?",
      "Hey! Ready to detect fake news? Just ask me."]],
    
    [r"(?i).*what do you do.*|.*who are you.*|.*your purpose.*",
     ["I'm a bot that helps detect fake news using deep learning.",
      "I analyze news content to determine if it's real or fake.",
      "I'm trained to spot misinformation in news articles."]],
    
    [r"(?i).*how does it work.*|.*how do you detect.*|.*working.*",
     ["Just paste the news content here, and I'll classify it as real or fake.",
      "I use natural language processing and a trained model to analyze text.",
      "Once you give me a news article, I run it through a classifier to check authenticity."]],
    
    [r"(?i).*dataset.*|.*training data.*|.*how trained.*",
     ["I was trained on real and fake news articles collected from trusted datasets.",
      "My model learned from thousands of labeled news examples.",
      "The dataset includes political, health, and world news classified as real or fake."]],
    
    [r"(?i).*can i trust you.*|.*are you accurate.*|.*reliable.*",
     ["While I'm trained to be accurate, always cross-verify with credible sources.",
      "I provide helpful insights, but final judgment should come from trusted platforms.",
      "I do my best to detect fake news — treat my response as a helpful tool, not absolute proof."]],
    
    [r"(?i).*thanks.*|.*thank you.*|.*appreciate.*",
     ["You're welcome! Let me know if you have another article to verify.",
      "Anytime! Happy to help.",
      "Glad I could assist. Stay informed!"]],
    
    [r"(?i).*bye.*|.*goodbye.*|.*see you.*",
     ["Goodbye! Stay sharp and question everything!",
      "See you later! Don't fall for fake news.",
      "Take care! Keep fact-checking."]],
    
    [r"(?i).*(check|verify).*(news|article|story).*|.*(is this news|real or fake).*",
     ["Please enter the full news content, and I'll check it for you.",
  "Sure, paste the news article you'd like me to analyze.",
  "Go ahead and share the news content — I'll run it through the fake news model."]]
]

chatbot = Chat(pairs,reflections)

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def get_pos(pos):
    if pos.startswith('J'):
        return wordnet.ADJ
    if pos.startswith('N'):
        return wordnet.NOUN
    if pos.startswith('V'):
        return wordnet.VERB
    if pos.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]',' ',text)
    text = re.sub(r'\s+',' ',text).strip()
    words = word_tokenize(text)
    stp = [w for w in words if w not in stop_words]
    pos_tags = pos_tag(stp)
    lemma = [lemmatizer.lemmatize(w,get_pos(pos)) for w,pos in pos_tags]
    return ' '.join(lemma)

def classify_news(text):
    try:
        preprocessed_text = clean_text(text)
        vectorized_text = vector.transform([preprocessed_text]).toarray()
        prediction = model.predict(vectorized_text)
        print(prediction)
        if prediction[0][0] >= 0.01:
            return "Chatbot: This news is REAL!"
        else:
            return "Chatbot: This news is FAKE!"
    except Exception as e:
        return f"Chatbot: Error occurred – {str(e)}"
        


def chat(user_input):
    print("You:", user_input)
    response = chatbot.respond(user_input)
    if response:
        return response
    else:
        return "Chatbot: Sorry, I didn’t quite get that. Can you rephrase?"
