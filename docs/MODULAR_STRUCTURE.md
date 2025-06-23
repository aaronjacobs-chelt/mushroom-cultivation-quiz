# 🍄 Modular Structure Documentation

## Overview

The Mushroom Cultivation Quiz has been restructured from a simple script-based application into a professional, modular Python package. This document outlines the new structure, improvements, and usage patterns.

## Version Information

- **Current Version**: 2.0.1
- **Author**: Aaron J
- **Email**: git@aaronemail.xyz
- **License**: MIT
- **Repository**: https://github.com/aaronjacobs-chelt/mushroom-cultivation-quiz

## Directory Structure

```
mushroom-cultivation-quiz/
├── src/mushroom_quiz/           # Main package directory
│   ├── __init__.py              # Package initialization (v2.0.1)
│   ├── __main__.py              # Entry point for `python -m mushroom_quiz`
│   ├── app.py                   # Main application logic (v2.0.1)
│   ├── core/                    # Core functionality
│   │   ├── __init__.py          # Core module exports
│   │   ├── quiz_engine.py       # Quiz game logic (v2.0.1)
│   │   └── timer.py             # Timer functionality (v2.0.1)
│   ├── ui/                      # User interface modules
│   │   ├── __init__.py          # UI module exports
│   │   └── terminal_ui.py       # Terminal UI functions (v2.0.1)
│   ├── data/                    # Data management
│   │   ├── __init__.py          # Data module exports
│   │   ├── question_loader.py   # Question loading abstraction (v2.0.1)
│   │   └── quiz_questions.py    # Original questions database
│   └── utils/                   # Utility functions
│       ├── __init__.py          # Utils module exports
│       └── helpers.py           # Helper functions (v2.0.1)
├── tests/                       # Test suite
│   ├── __init__.py              # Test package init (v2.0.1)
│   └── test_question_loader.py  # Question loader tests (v2.0.1)
├── docs/                        # Documentation
│   ├── DEVELOPMENT_NOTES.md     # Development notes
│   ├── VERSIONING.md            # Version history
│   └── MODULAR_STRUCTURE.md     # This file
├── web/                         # Web interface files
├── setup.py                     # Package installation script (v2.0.1)
├── requirements.txt             # Dependencies
├── README.md                    # Main documentation
├── LICENSE                      # MIT License
├── mushroom_quiz_app_legacy.py  # Backward compatibility wrapper (v2.0.1)
└── mushroom_quiz_app.py         # Original entry point (preserved)
```

## Module Documentation

### Core Package (`src/mushroom_quiz/`)

**Main Entry Points:**
- `__init__.py`: Package initialization with version info
- `__main__.py`: Allows `python -m mushroom_quiz` execution
- `app.py`: Main application coordination logic

### Core Functionality (`src/mushroom_quiz/core/`)

**Modules:**
- `quiz_engine.py`: Contains `QuizGame` class and `create_quiz()` function
- `timer.py`: Handles timed input with visual countdown

**Key Classes:**
- `QuizGame`: Main quiz execution and scoring logic
- `TimedInput`: Thread-based timed input handling

### User Interface (`src/mushroom_quiz/ui/`)

**Modules:**
- `terminal_ui.py`: All terminal-based UI functions and styling

**Key Functions:**
- `clear_screen()`: Cross-platform screen clearing
- `print_header()`: ASCII art header display
- `display_question()`: Formatted question presentation
- `display_final_score()`: Comprehensive results with rankings

### Data Management (`src/mushroom_quiz/data/`)

**Modules:**
- `question_loader.py`: Abstraction layer for question access
- `quiz_questions.py`: Original question database (preserved)

**Key Functions:**
- `get_questions_by_difficulty()`: Filter questions by difficulty
- `get_all_questions()`: Retrieve all available questions
- `get_question_count_by_difficulty()`: Count questions per difficulty

### Utilities (`src/mushroom_quiz/utils/`)

**Modules:**
- `helpers.py`: Common utility functions

**Key Functions:**
- `validate_input()`: Input validation within ranges
- `format_percentage()`: Percentage formatting
- `get_performance_level()`: Performance level categorization

## Usage Examples

### Installation
```bash
# Development installation
pip install -e .

# Regular installation (when published)
pip install mushroom-cultivation-quiz
```

### Running the Application
```bash
# As a module
python -m mushroom_quiz

# After installation
mushroom-quiz

# Legacy compatibility
python mushroom_quiz_app_legacy.py
```

### Programmatic Usage
```python
# Import and run main function
from mushroom_quiz import main
main()

# Import specific components
from mushroom_quiz.core import create_quiz
from mushroom_quiz.data import get_questions_by_difficulty
from mushroom_quiz.utils import format_percentage

# Run a quiz programmatically
score, total = create_quiz("intermediate", 10, 30)
print(f"Score: {format_percentage(score, total)}")
```

## Testing

### Running Tests
```bash
# Run all tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/test_question_loader.py -v

# Run with unittest
python -m unittest discover tests/
```

### Test Coverage
- ✅ Question loading and filtering
- ✅ Difficulty level management
- ✅ Question counting functionality
- ✅ Invalid input handling

## Version History

### 2.0.1 (2025-06-23)
- ✅ Complete modular restructuring
- ✅ Proper documentation and headers
- ✅ Version consistency across all files
- ✅ Professional package structure
- ✅ Comprehensive test coverage
- ✅ Multiple execution methods
- ✅ Backward compatibility maintained

### 2.0.0 (2025-06-21)
- Initial modular restructuring
- Basic package structure implementation

## Benefits of Modular Structure

### Developer Benefits
- **Clear Separation of Concerns**: Each module has a specific responsibility
- **Better Code Organization**: Easy to locate and modify specific functionality
- **Enhanced Maintainability**: Changes can be made to individual modules without affecting others
- **Improved Testing**: Each component can be tested in isolation
- **IDE Support**: Better code completion and navigation

### User Benefits
- **Multiple Execution Methods**: Various ways to run the application
- **Easy Installation**: Standard Python package installation
- **Backward Compatibility**: Existing scripts continue to work
- **Professional Experience**: Well-structured, reliable application

### Future Development
- **Scalability**: Easy to add new features and components
- **Extensibility**: New UI modes, question types, or features can be added easily
- **Modularity**: Components can be reused in other projects
- **Community Contributions**: Clear structure makes it easier for others to contribute

## API Documentation

### Core API
```python
# Main application entry point
mushroom_quiz.main() -> None

# Create and run a quiz
mushroom_quiz.core.create_quiz(
    difficulty: str,     # 'beginner', 'intermediate', 'advanced', 'mixed'
    num_questions: int,  # Number of questions (5, 10, 20)
    timer_seconds: int   # Timer in seconds (None for no timer)
) -> tuple[int, int]     # Returns (score, total_questions)
```

### Data API
```python
# Get questions by difficulty
mushroom_quiz.data.get_questions_by_difficulty(difficulty: str) -> list[dict]

# Get all questions
mushroom_quiz.data.get_all_questions() -> list[dict]

# Count questions by difficulty
mushroom_quiz.data.get_question_count_by_difficulty(difficulty: str) -> int
```

### Utility API
```python
# Validate input range
mushroom_quiz.utils.validate_input(user_input: str, min_val: int, max_val: int) -> int|None

# Format percentage
mushroom_quiz.utils.format_percentage(correct: int, total: int) -> str

# Get performance level
mushroom_quiz.utils.get_performance_level(score: int, total: int) -> tuple[str, str, str]
```

## Migration Guide

### For Existing Users
1. **No Action Required**: Old entry points still work
2. **Recommended**: Switch to `python -m mushroom_quiz` for better experience
3. **Optional**: Install package with `pip install -e .` for system-wide access

### For Developers
1. **Import Changes**: Use new modular imports for better structure
2. **Testing**: Use the test suite for validation
3. **Extensions**: Follow the modular pattern for new features

## Contributing

When contributing to the project:
1. Follow the established modular structure
2. Add appropriate documentation headers to new files
3. Include version numbers and author information
4. Write tests for new functionality
5. Update this documentation for structural changes

## Support

For questions, issues, or contributions:
- **GitHub**: https://github.com/aaronjacobs-chelt/mushroom-cultivation-quiz
- **Issues**: Use the GitHub issue tracker
- **Email**: git@aaronemail.xyz
