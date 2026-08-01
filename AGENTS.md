# AGENTS.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

A Python-based educational quiz application for mushroom cultivation. Features a modular package architecture with terminal UI, web version, and retro versions (ZX Spectrum, C64 BASIC).

## Commands

### Running the Application
```bash
# Recommended: run as Python module
python -m mushroom_quiz

# After editable install
pip install -e .
mushroom-quiz

# Legacy entry points (preserved for compatibility)
python mushroom_quiz_app.py
python mushroom_quiz_app_legacy.py
```

### Testing
```bash
# Run all tests
python -m pytest tests/

# Run with verbose output
python -m pytest tests/ -v

# Run specific test file
python -m pytest tests/test_question_loader.py
```

### Web Version
```bash
cd web && python -m http.server 8000
# Open http://localhost:8000
```

## Architecture

### Modular Package (`src/mushroom_quiz/`)
- **`app.py`** - Main application entry point, menu flow coordination
- **`core/quiz_engine.py`** - `QuizGame` class, question processing, scoring logic
- **`core/timer.py`** - `TimedInput` class with visual countdown threading
- **`ui/terminal_ui.py`** - All display functions, ANSI colors, menus
- **`data/quiz_questions.py`** - Question database (111 questions)
- **`data/question_loader.py`** - Question filtering/access abstraction layer
- **`utils/helpers.py`** - Input validation, formatting, performance levels

### Legacy Files (Root Directory)
Files `quiz_*.py` and `mushroom_quiz_app*.py` in root are preserved for backward compatibility. New features should go in `src/mushroom_quiz/`.

### Web Version (`web/`)
Static JavaScript/HTML implementation - runs client-side only. Questions are duplicated in `web/questions.js`.

## Key Patterns

### Question Format
Questions in `src/mushroom_quiz/data/quiz_questions.py` follow this structure:
```python
{
    "question": "Question text?",
    "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
    "answer": "Correct option (must match one option exactly)",
    "difficulty": "beginner|intermediate|advanced",
    "explanation": "Educational explanation shown after answering",
    "topic": "category_name"
}
```

### Version Consistency
All module files contain version headers. When releasing, update version in:
- `setup.py` (line 21)
- `src/mushroom_quiz/__init__.py`
- All module file headers

## Dependencies

No external dependencies required - uses Python standard library only. Development dependencies (pytest, black, flake8) are optional.
