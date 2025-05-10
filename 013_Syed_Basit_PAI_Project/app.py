from flask import Flask, request, render_template
from chatbot import chat, classify_news

app = Flask(__name__)

# Store last bot response to determine if we need news content
last_bot_response = {"message": ""}

@app.route('/', methods=['GET', 'POST'])
def chatbot_interface():
    bot_reply = ''
    classification_result = ''
    user_input = ''

    if request.method == 'POST':
        user_input = request.form['message']
        
        # If last message asked for news content, classify it
        if last_bot_response['message'] in [
            "Please enter the full news content, and I'll check it for you.",
            "Sure, paste the news article you'd like me to analyze.",
            "Go ahead and share the news content — I'll run it through the fake news model."
        ]:
            classification_result = classify_news(user_input)
            bot_reply = classification_result
            last_bot_response['message'] = ''
        else:
            bot_reply = chat(user_input)
            last_bot_response['message'] = bot_reply

    return render_template('index.html', user_input=user_input, bot_reply=bot_reply)

if __name__ == '__main__':
    app.run(debug=True)
