import os
import uuid
from dotenv import load_dotenv
from flask import Flask, request, jsonify, session
from ownapi.models import db
from ownapi.utils import chat_completion, save_message, get_messages

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
db.init_app(app)


@app.route('/ask', methods=['POST'])
def ask():
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())

    user_id = session['user_id']
    data = request.json
    question = data.get('question')

    if question:
        save_message(user_id, question)
        app.logger.info(f"Question: {question}")

        context = ' '.join([msg.message for msg in get_messages(user_id)])
        system_message = ' '.join([
            'Return only answer for the given question.'
            f'Given context of our conversation: {context}',
        ])
        chat_response = chat_completion(system_message, question)
        app.logger.info(f"Response: {chat_response}")
        return jsonify({'reply': chat_response})
    else:
        app.logger.error("No question provided")
        return jsonify({'error': 'No question provided'}), 400


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=os.getenv('APP_PORT', 5000))
