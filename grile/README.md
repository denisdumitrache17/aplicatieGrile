# Grile Simulator - Quiz/Exam Web Application

A clean and modern quiz application built with Flask (Python backend) and Vanilla JavaScript (frontend). Users can take randomized IT knowledge tests with **custom question counts** and instant answer validation.

## ✨ New Feature: Custom Question Count

Users can now choose how many questions they want (1-30) before starting the test!

## Features

✅ **Custom Question Count**: Choose between 1-30 questions per test  
✅ **Randomized Questions**: Each test generates random questions from a pool of 30  
✅ **Multi-Select Options**: Checkbox-based answers supporting multiple correct options  
✅ **Instant Validation**: Questions turn green (correct) or red (incorrect) on check  
✅ **Score Tracking**: Displays correct/incorrect count and percentage score  
✅ **Modern UI**: Clean gradient design with smooth animations  
✅ **Responsive Layout**: Works seamlessly on desktop and mobile devices

## Project Structure

```
grile/
├── app.py                  # Flask backend server
├── questions.json          # 30 IT knowledge questions
├── templates/
│   └── index.html          # Frontend (HTML/CSS/JS combined)
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Steps

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   Or manually:
   ```bash
   pip install Flask==3.0.0
   ```

2. **Run the Application**
   ```bash
   python app.py
   ```
   Or on Windows:
   ```bash
   py -3 app.py
   ```

3. **Access the Application**
   Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## How to Use

1. **Choose Question Count**: Enter a number between 1-30 in the input field
2. **Start Test**: Click the "Start Test" button
3. **Answer Questions**: Select your answers using checkboxes (multiple selections allowed)
4. **Verify Answers**: Click "Verifică" to check your answers
5. **View Results**: See your score and question-by-question feedback
6. **Restart**: Click "Test Nou" to take another test

## API Endpoints

### GET `/api/get-quiz`
Returns a random selection of questions from the question bank.

**Query Parameters:**
- `count` (optional): Number of questions to return (1-30). If not provided, defaults to random 15-20.

**Examples:**
```
GET /api/get-quiz?count=10   # Returns 10 random questions
GET /api/get-quiz?count=25   # Returns 25 random questions
GET /api/get-quiz            # Returns 15-20 random questions
```

**Response Example:**
```json
[
  {
    "id": 1,
    "text": "Which of the following are Python web frameworks?",
    "options": ["Flask", "React", "Django", "Vue.js"],
    "correct_indices": [0, 2]
  }
]
```

## Question Format

Each question in `questions.json` follows this structure:

```json
{
  "id": 1,
  "text": "Question text here?",
  "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
  "correct_indices": [0, 2]
}
```

- **id**: Unique identifier
- **text**: Question text
- **options**: Array of answer options
- **correct_indices**: Array of indices for correct answers (0-based)

## Customization

### Adding More Questions
Edit `questions.json` and add new question objects following the format above.

### Changing Default Question Range
Edit `app.py` to modify the default range when no count parameter is provided:
```python
num_questions = random.randint(15, 20)  # Change these values
```

### Styling
Modify the `<style>` section in `templates/index.html` to customize colors, fonts, and layout.

## Technology Stack

- **Backend**: Python 3 + Flask
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Data**: JSON file-based storage
- **Validation**: Client-side instant validation

## Features in Detail

### Custom Question Count
- Input field validates user input (1-30 range)
- Backend validates and limits to available questions
- User can press Enter to start test

### Validation Logic
- Compares user-selected checkboxes against `correct_indices`
- Green background = All correct answers selected, no incorrect ones
- Red background = Missing correct answers OR selected incorrect answers
- Disables all inputs after validation to prevent changes

### Scoring System
- Tracks correct vs incorrect answers
- Displays percentage score
- Shows detailed statistics after submission

## Troubleshooting

**Issue**: Flask won't start  
**Solution**: Make sure Flask is installed: `pip install Flask`

**Issue**: Questions don't load  
**Solution**: Ensure `questions.json` is in the same directory as `app.py`

**Issue**: Port already in use  
**Solution**: Change the port in `app.py`: `app.run(debug=True, port=5001)`

**Issue**: Input field not showing  
**Solution**: Clear browser cache and refresh the page

## License

Free to use for educational purposes.

## Author

Built as a Senior Full Stack Developer demonstration project.

## Changelog

### v1.1 (Latest)
- ✨ Added custom question count selector (1-30 questions)
- 🔧 Backend now accepts `count` query parameter
- 🎨 Updated UI with number input field
- ✅ Input validation for question count

### v1.0
- Initial release with 30 IT questions
- Random 15-20 questions per test
- Multi-select quiz functionality
- Instant validation and scoring
