# 🍄 Mushroom Cultivation Quiz Application

A comprehensive, modular quiz application that tests knowledge about mushroom cultivation techniques, varieties, substrates, and terminology.

## 📁 Project Structure

The application is organized into separate modules for better maintainability:

```
mushroom_quiz_app.py     # Main application entry point
quiz_ui.py              # User interface and display functions
quiz_questions.py       # Question database and utilities
quiz_logic.py           # Core quiz game logic and flow
quiz_timer.py           # Timed input functionality
README_quiz.md          # This documentation file
```

## 🔧 Module Descriptions

### `mushroom_quiz_app.py` - Main Application
- Entry point for the application
- Coordinates all other modules
- Handles main menu navigation
- Manages quiz sessions

### `quiz_ui.py` - User Interface
- ANSI color definitions and styling
- Screen clearing and header display
- Menu functions (difficulty, questions, timer)
- Result display functions
- Study recommendations

### `quiz_questions.py` - Question Database
- Comprehensive database of 45+ questions
- Questions organized by difficulty and topic
- Utility functions for filtering questions
- Statistics functions for question distribution

### `quiz_logic.py` - Core Logic
- `QuizGame` class that manages quiz flow
- Question preparation and randomization
- Score tracking and topic analysis
- Integration between UI and timer modules

### `quiz_timer.py` - Timer Functionality
- `TimedInput` class for countdown timers
- Threaded input handling
- Visual countdown display
- Timeout management

## 🎮 Features

- **Multiple Difficulty Levels**: Beginner, Intermediate, Advanced, Mixed
- **Flexible Quiz Length**: 5, 10, or 20 questions
- **Timer Modes**: Relaxed (no timer), Timed (30s), Speed (15s)
- **Colorful Interface**: ANSI colors and emojis
- **Study Recommendations**: Personalized based on wrong answers
- **Screen Management**: Clean interface with screen clearing

## 🚀 Running the Application

```bash
python mushroom_quiz_app.py
```

## 📊 Question Database Stats

- **Total Questions**: 45
- **Difficulty Distribution**:
  - Beginner: 15 questions
  - Intermediate: 20 questions  
  - Advanced: 10 questions
- **Topics Covered**:
  - Growing conditions (temperature, humidity, pH)
  - Mushroom varieties and identification
  - Substrates and growing media
  - Cultivation processes and terminology
  - Sterilization techniques
  - Medicinal mushrooms
  - Growing methods and timing

## 🔧 Extending the Application

### Adding New Questions
Add questions to the `QUESTIONS` list in `quiz_questions.py`:

```python
{
    "question": "Your question here?",
    "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
    "answer": "Correct option",
    "difficulty": "beginner|intermediate|advanced",
    "explanation": "Educational explanation",
    "topic": "topic_category"
}
```

### Adding New Features
- **New UI elements**: Add to `quiz_ui.py`
- **New timer modes**: Extend `quiz_timer.py`
- **New game modes**: Modify `quiz_logic.py`
- **Statistics tracking**: Extend the main app

## 🎯 Benefits of Modular Design

1. **Maintainability**: Each module has a single responsibility
2. **Scalability**: Easy to add new features without breaking existing code
3. **Testability**: Modules can be tested independently
4. **Reusability**: Components can be reused in other projects
5. **Readability**: Code is organized and well-documented
6. **Collaboration**: Multiple developers can work on different modules

## 🌟 Future Enhancements

- Question difficulty auto-adjustment based on performance
- Statistics tracking across sessions
- Question categories filtering
- Import/export of custom question sets
- Multi-language support
- Web interface version

