import os

from dotenv import load_dotenv
from flask import Flask, request, jsonify

from openai_api.utils import chat_completion

load_dotenv()

app = Flask(__name__)


@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')
    app.logger.info(question)
    system_message = ' '.join([
        'Return only answer for the given question.',
    ])
    chat_response = chat_completion(system_message, question)
    app.logger.info(chat_response)
    return jsonify({'reply': chat_response})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv('APP_PORT'))
