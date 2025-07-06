# 🍄 Retro Mushroom Cultivation Quiz Collection

A collection of vintage computer versions of the Mushroom Cultivation Quiz, bringing the educational experience to classic 8-bit and 16-bit systems!

## 🕹️ Available Retro Versions

### ZX Spectrum BASIC (mushroom_quiz_spectrum.bas)
- **Platform**: Sinclair ZX Spectrum (48K/128K)
- **Language**: ZX Spectrum BASIC
- **Features**:
  - Classic 1980s interface with BORDER, PAPER, INK commands
  - 18 carefully selected questions across 3 difficulty levels
  - Color-coded screen presentation
  - Authentic retro scoring system
  - Memory-efficient string array storage

### Technical Specifications

#### ZX Spectrum Version
- **Memory Requirements**: ~8K (fits comfortably on 48K Spectrum)
- **Questions**: 18 total (5 Beginner, 8 Intermediate, 5 Advanced)
- **Display**: 32x24 character screen with color
- **Input**: Keyboard numbers 1-4 for answers
- **Storage**: Cassette tape (.TAP format) or disk

## 🎮 How to Run

### ZX Spectrum
1. **Real Hardware**: Load via cassette or DivIDE interface
2. **Emulators**: 
   - FUSE (Linux/Windows/Mac)
   - ZEsarUX (Multi-platform)
   - SpectEmu (Windows)
   - Retro Virtual Machine (Commercial)

### Loading Instructions

**From TAP file (recommended):**
```basic
LOAD ""
```
*Note: The TAP file includes auto-start functionality - the program will run automatically after loading.*

**From typed BASIC:**
```basic
LOAD "MUSHROOM"
RUN
```

Or type in the BASIC code manually (authentic 1980s experience!):
```basic
10 REM MUSHROOM CULTIVATION QUIZ
20 REM ZX SPECTRUM VERSION
...
```

## 🎯 Gameplay Features

### Classic Retro Elements
- **Authentic BASIC Programming**: Uses period-appropriate coding techniques
- **Classic Color Scheme**: Blue border, black paper, white ink
- **Simple Navigation**: Number key selection (1-4)
- **Educational Feedback**: Immediate answer explanation
- **Score Tracking**: Percentage-based performance ratings

### Difficulty Levels
- **Beginner**: 5 questions about basic mushroom growing concepts
- **Intermediate**: 8 questions covering cultivation techniques
- **Advanced**: 5 questions on specialized topics like pH and contamination

### Scoring System
- **80%+**: "EXCELLENT! MUSHROOM MASTER!"
- **60-79%**: "GOOD! FUNGI EXPERT!"
- **40-59%**: "OK! KEEP STUDYING!"
- **<40%**: "POOR! MORE PRACTICE NEEDED!"

## 📺 Technical Details

### ZX Spectrum BASIC Features Used
- **Arrays**: Multi-dimensional string arrays for questions/answers
- **Graphics**: BORDER, PAPER, INK color commands
- **Screen Control**: CLS, PRINT AT positioning
- **Input**: INPUT and PAUSE commands
- **Logic**: IF/THEN, FOR/NEXT, GOSUB/RETURN

### Memory Layout
```
Lines 10-150:    Initialization and setup
Lines 160-280:   Main program flow  
Lines 290-820:   Menu and quiz logic
Lines 1000-1510: Subroutines
Lines 1900-1940: Exit routine
Lines 2000-3470: Question database
```

### String Array Structure
```basic
Q$(20,60)     - Questions (up to 60 characters)
A$(20,4,20)   - Answers (4 per question, 20 chars each)
C$(20,20)     - Correct answers (20 characters)
E$(20,80)     - Explanations (80 characters)
```

## 🎨 Retro Aesthetics

### Visual Design
- Classic ZX Spectrum color palette
- Text-based interface with character graphics
- Authentic 1980s computer feel
- Simple but effective layout

### User Experience
- Keyboard-only navigation
- Clear, simple menus
- Immediate feedback
- No graphics - pure text appeal
- Authentic computer "beeps" and pauses

## 🔧 Development Notes

### Programming Considerations
- **Memory Constraints**: Designed to fit in 48K Spectrum memory
- **String Limitations**: Kept within ZX BASIC string length limits
- **Line Numbers**: Used traditional 10-step increments
- **Subroutines**: Organized with GOSUB for code reuse
- **Error Handling**: Simple validation with re-prompting

### Historical Accuracy
- Uses period-appropriate BASIC syntax
- Follows 1980s programming conventions
- Memory-conscious design patterns
- Simple but effective user interface

## 🕰️ Historical Context

### Why ZX Spectrum?
The Sinclair ZX Spectrum (1982) was one of the most popular home computers in the UK and Europe. Creating a version for this platform honors the educational software tradition of the 1980s when learning programs were commonly distributed on cassette tapes.

### Educational Software Heritage
This retro version pays homage to the educational software of the 1980s, when simple BASIC programs taught everything from math to science. The mushroom cultivation quiz continues this tradition with modern mycological knowledge presented in classic format.

## 🎯 Future Retro Versions

### Planned Platforms
- **Commodore 64**: Enhanced with SID sound and better graphics
- **Apple II**: Classic green phosphor text display
- **Amstrad CPC**: Color graphics and enhanced presentation
- **BBC Micro**: Educational computer standard in UK schools
- **Atari 8-bit**: GTIA graphics capabilities

### Potential Enhancements
- Sound effects using platform-specific audio
- Simple graphics for question illustrations
- Save/load high score functionality
- Extended question databases
- Multi-disk/tape versions with more content

## 📚 Educational Value

### Learning Benefits
- **Accessibility**: Runs on vintage hardware or emulators
- **Simplicity**: Focus on content without modern distractions
- **Historical**: Experience how computer education worked in the 1980s
- **Programming**: Study BASIC code for educational purposes

### Target Audience
- Retro computing enthusiasts
- Mycology students and hobbyists
- Computer history educators
- Anyone nostalgic for 8-bit computing

## 🔗 Resources

### Emulators
- **FUSE**: Free ZX Spectrum emulator (Linux/Windows/Mac)
- **ZEsarUX**: Multi-system emulator including Spectrum
- **SpectEmu**: Windows-specific Spectrum emulator

### File Formats
- `.BAS`: BASIC text file for manual typing
- `.TAP`: Cassette tape image with auto-start functionality
- `.TZX`: Enhanced tape format (future release)

### Building TAP Files
The TAP file is generated using zmakebas:
```bash
./zmakebas/zmakebas -n "MUSHROOM" -a 10 -o mushroom.tap mushroom_quiz_spectrum.bas
```
- `-n "MUSHROOM"`: Sets the filename visible to the Spectrum
- `-a 10`: Auto-start from line 10 (equivalent to SAVE "MUSHROOM" LINE 10)
- `-o mushroom.tap`: Output filename

### Documentation
- ZX Spectrum BASIC manual
- Vintage computer programming guides
- Educational software development history

## 🏆 Credits

- **Original Quiz**: Aaron J (2025)
- **Retro Adaptation**: Aaron J (2025)
- **Platform**: Sinclair ZX Spectrum (1982)
- **Language**: Sinclair BASIC
- **Inspiration**: Classic 1980s educational software

## 📄 License

This retro collection is released under the same MIT License as the main project, honoring both modern open-source principles and the sharing culture of early home computing.

---

**Experience mushroom cultivation education the way it might have been taught in 1985!** 🍄💾

*"Press any key to continue..."*
