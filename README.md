# 🍄 Mushroom Cultivation Quiz Application

A comprehensive, modular quiz application that tests knowledge about mushroom cultivation techniques, varieties, substrates, terminology, and medicinal properties. This educational tool provides an interactive learning experience for mushroom cultivation enthusiasts at all skill levels.

## ✨ Latest Updates (v2.0.0)

- **Expanded Question Database**: Now includes **111 questions** (up from 45)
- **Enhanced Medicinal Mushroom Coverage**: 19 dedicated questions on health benefits
- **Comprehensive Headers**: Professional documentation in all code files
- **Improved Balance**: Better distribution across all topics and difficulty levels
- **Advanced Cultivation Topics**: Sterilization, cultivation processes, and growing methods

## 📁 Project Structure

The application is organized into separate modules for better maintainability:

```
## Terminal Version
mushroom_quiz_app.py     # Main application entry point (v2.0.0)
quiz_ui.py              # User interface and display functions
quiz_questions.py       # Question database (111 questions)
quiz_logic.py           # Core quiz game logic and flow
quiz_timer.py           # Timed input functionality

## Web Version
web/
├── index.html          # Main HTML file
├── styles.css          # CSS styling
├── questions.js        # Question database (JavaScript)
└── quiz.js             # Main quiz logic (JavaScript)

## Documentation
README.md               # This documentation file
LICENSE                 # MIT License
docs/                   # Additional documentation
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

### Terminal Version
```bash
python mushroom_quiz_app.py
```

### Web Version
1. **Local Development**:
   ```bash
   cd web
   python -m http.server 8000
   # Open http://localhost:8000 in your browser
   ```

2. **Production Deployment**:
   - Deploy the `web/` folder to any web server
   - No server-side processing required (static files only)
   - Compatible with GitHub Pages, Netlify, Vercel, etc.

## 🌐 Web Version Features

- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Modern UI**: Beautiful gradient backgrounds and smooth animations
- **Interactive Elements**: Hover effects and visual feedback
- **Progress Tracking**: Visual progress bar and real-time scoring
- **Timer Visualization**: Circular countdown timer with color coding
- **Keyboard Support**: Use number keys (1-4) to select answers
- **Social Sharing**: Share results with friends
- **Accessibility**: Semantic HTML and keyboard navigation
- **Cross-browser Compatible**: Works in all modern browsers

## 📊 Question Database Stats (v2.0.0)

### 🎯 **Total Questions: 111**

### **Difficulty Distribution:**
- **Beginner**: 38 questions (34.2%) - Perfect for newcomers
- **Intermediate**: 46 questions (41.4%) - Core learning content
- **Advanced**: 27 questions (24.3%) - Expert-level challenges

### **Topic Distribution:**
1. **Cultivation Process**: 22 questions (19.8%) - Step-by-step procedures
2. **Medicinal Mushrooms**: 19 questions (17.1%) - Health benefits & compounds
3. **Mushroom Varieties**: 14 questions (12.6%) - Species identification
4. **Sterilization**: 13 questions (11.7%) - Contamination prevention
5. **Growing Conditions**: 9 questions (8.1%) - Environmental factors
6. **Growing Methods**: 8 questions (7.2%) - Techniques & systems
7. **Biology Basics**: 7 questions (6.3%) - Fundamental knowledge
8. **Timing**: 7 questions (6.3%) - Schedules & lifecycle stages
9. **Substrates**: 6 questions (5.4%) - Growing media
10. **Beginner Varieties**: 6 questions (5.4%) - Entry-level species

### **Topics Covered:**
- **🧬 Biology Basics**: Hyphae, mycelium, spores, fungal lifecycle
- **🌱 Beginner Varieties**: Oyster mushrooms, coffee ground cultivation
- **⚗️ Cultivation Process**: Inoculation, colonization, pinning, flushing
- **🌡️ Growing Conditions**: Temperature, humidity, pH, CO2, lighting
- **🔧 Growing Methods**: Log cultivation, monotub, SGFC, vertical systems
- **💊 Medicinal Mushrooms**: Reishi, Lion's Mane, Cordyceps, Turkey Tail, Chaga
- **🍄 Mushroom Varieties**: Shiitake, King Oyster, Maitake, Enoki, Wine Cap
- **🧪 Sterilization**: Pressure cooking, autoclaves, sterile technique
- **🌾 Substrates**: Sawdust, straw, coffee grounds, supplements
- **⏰ Timing**: Harvest timing, spawn storage, flush intervals

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

## 🏆 Version 2.0.0 Achievements

✅ **Database Expansion**: Increased from 45 to 111 questions (147% growth)
✅ **Topic Balance**: Eliminated small categories, improved distribution
✅ **Medicinal Focus**: Comprehensive coverage of health benefits
✅ **Professional Headers**: Complete documentation in all code files
✅ **Advanced Topics**: Sterilization and cultivation process depth
✅ **Beginner Support**: Enhanced entry-level content
✅ **Quality Assurance**: All questions fact-checked and explained

## 🌟 Future Enhancements

### **Planned Features:**
- Question difficulty auto-adjustment based on performance
- Statistics tracking across sessions
- Question categories filtering
- Import/export of custom question sets
- Multi-language support
- Enhanced web interface version
- Progress tracking and achievement system
- Advanced cultivation calculator tools

### **Potential Expansions:**
- Commercial cultivation business topics
- Mushroom identification mini-games
- Growing equipment recommendations
- Seasonal cultivation planning
- Troubleshooting problem solver

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### **Ways to Contribute:**
1. **Add Questions**: Submit new mushroom cultivation questions
2. **Improve Documentation**: Enhance code comments or README
3. **Bug Reports**: Report issues or unexpected behavior
4. **Feature Requests**: Suggest new functionality
5. **Code Improvements**: Optimize existing code
6. **Translation**: Help with multi-language support

### **Submission Guidelines:**
- Fork the repository
- Create a feature branch
- Follow existing code style and documentation standards
- Test your changes thoroughly
- Submit a pull request with clear description

### **Question Quality Standards:**
- Factually accurate and well-researched
- Clear, unambiguous wording
- Educational explanations
- Appropriate difficulty level
- Real-world applicability

## 📋 Requirements

### **Terminal Version:**
- Python 3.6 or higher
- No external dependencies (uses only standard library)
- Cross-platform compatible (Windows, macOS, Linux)

### **Web Version:**
- Modern web browser with JavaScript support
- No server requirements (runs client-side)
- Mobile and desktop compatible

## 🛠️ Development Setup

```bash
# Clone the repository
git clone https://github.com/username/mushroom-cultivation-quiz.git
cd mushroom-cultivation-quiz

# Run the terminal version
python mushroom_quiz_app.py

# Serve the web version locally
cd web
python -m http.server 8000
# Open http://localhost:8000
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### **MIT License Summary:**
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use
- ❌ Liability
- ❌ Warranty

## 👨‍💻 Author

**Aaron J**
- Created: June 21, 2025
- Version: 2.0.0
- Contact: git@aaronemail.xyz

## 🙏 Acknowledgments

- Mushroom cultivation community for knowledge sharing
- Educational resources and research papers
- Open source contributors and testers
- Mycology experts who provided fact-checking

## 📚 Educational Resources

### **Recommended Reading:**
- "The Mushroom Cultivator" by Paul Stamets
- "Growing Gourmet and Medicinal Mushrooms" by Paul Stamets
- "Organic Mushroom Farming and Mycoremediation" by Tradd Cotter
- "Radical Mycology" by Peter McCoy

### **Online Communities:**
- r/MushroomGrowers (Reddit)
- Shroomery.org forums
- Mushroom cultivation Facebook groups
- Local mycology societies

### **Scientific Resources:**
- PubMed mushroom research papers
- International Journal of Medicinal Mushrooms
- Mycological societies and conferences

## 🎮 How to Play

### **Getting Started:**
1. Choose your difficulty level (Beginner/Intermediate/Advanced/Mixed)
2. Select quiz length (5, 10, or 20 questions)
3. Pick timer mode (Relaxed/Timed/Speed)
4. Answer multiple-choice questions
5. Learn from detailed explanations
6. Review personalized study recommendations

### **Scoring System:**
- 🌟 **90%+**: MUSHROOM MASTER
- 🍄 **70%+**: FUNGI EXPERT
- 🌱 **50%+**: GROWING CULTIVATOR
- 🔰 **<50%**: SPORE BEGINNER

### **Tips for Success:**
- Start with beginner difficulty to build confidence
- Read all explanations, even for correct answers
- Use study recommendations to focus learning
- Retake quizzes to reinforce knowledge
- Progress from easier to harder difficulties

---

**Happy Mushroom Growing! 🍄✨**

*Built with ❤️ for the mushroom cultivation community*

