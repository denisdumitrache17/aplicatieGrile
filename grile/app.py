from flask import Flask, jsonify, send_from_directory
import json
import random

app = Flask(__name__, static_folder='templates', static_url_path='')

# Load questions on startup
with open('questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')

@app.route('/api/get-quiz', methods=['GET'])
def get_quiz():
    """
    Returns a random selection of N questions
    If 'count' parameter is provided, uses that value, otherwise random between 15 and 20
    """
    from flask import request
    
    # Get count from query parameter, or use random number between 15 and 20
    count_param = request.args.get('count', type=int)
    if count_param:
        # Ensure count is within valid range (1 to total questions)
        num_questions = max(1, min(count_param, len(questions)))
    else:
        num_questions = random.randint(15, 20)
    
    # Randomly sample questions
    selected_questions = random.sample(questions, num_questions)
    
    return jsonify(selected_questions)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
