#!/usr/bin/env python3
"""
Quiz UI Module
Contains all user interface elements, colors, and display functions
"""

import os
import time

# ANSI color codes
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    PURPLE = '\033[35m'
    YELLOW = '\033[33m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    CYAN = '\033[36m'

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print the game header with mushroom art"""
    header = f"""
{Colors.CYAN}╔══════════════════════════════════════════════════════════════╗
║                🍄 MUSHROOM CULTIVATION QUIZ 🍄               ║
║                   Test Your Fungi Knowledge!                 ║
╚══════════════════════════════════════════════════════════════╝{Colors.ENDC}

{Colors.PURPLE}    🍄    🍄    🍄    🍄    🍄    🍄    🍄    🍄
  ╱   ╲ ╱   ╲ ╱   ╲ ╱   ╲ ╱   ╲ ╱   ╲ ╱   ╲ ╱   ╲
 ╱     ╲     ╲     ╲     ╲     ╲     ╲     ╲     ╲
╱_______╲___╱_╲___╱_╲___╱_╲___╱_╲___╱_╲___╱_╲___╱_╲{Colors.ENDC}

{Colors.YELLOW}Welcome to the ultimate mushroom cultivation challenge!{Colors.ENDC}
    """
    print(header)

def get_difficulty_level():
    """Let user choose difficulty level"""
    print(f"\n{Colors.BOLD}Choose your difficulty level:{Colors.ENDC}")
    print(f"{Colors.GREEN}1. 🟢 Beginner (Easy questions)") 
    print(f"{Colors.YELLOW}2. 🟡 Intermediate (Moderate questions)")
    print(f"{Colors.RED}3. 🔴 Advanced (Hard questions)")
    print(f"{Colors.CYAN}4. 🌈 Mixed (All difficulty levels){Colors.ENDC}")
    
    while True:
        try:
            choice = int(input(f"\n{Colors.BOLD}Enter your choice (1-4): {Colors.ENDC}"))
            if choice == 1:
                return "beginner"
            elif choice == 2:
                return "intermediate"
            elif choice == 3:
                return "advanced"
            elif choice == 4:
                return "mixed"
            else:
                print(f"{Colors.FAIL}Please enter a number between 1 and 4.{Colors.ENDC}")
        except ValueError:
            print(f"{Colors.FAIL}Please enter a valid number.{Colors.ENDC}")

def get_number_of_questions():
    """Let user choose number of questions"""
    print(f"\n{Colors.BOLD}How many questions would you like?{Colors.ENDC}")
    print(f"{Colors.GREEN}1. ⚡ Quick Quiz (5 questions)")
    print(f"{Colors.YELLOW}2. 🎯 Standard Quiz (10 questions)")
    print(f"{Colors.RED}3. 🏆 Challenge Quiz (20 questions){Colors.ENDC}")
    
    while True:
        try:
            choice = int(input(f"\n{Colors.BOLD}Enter your choice (1-3): {Colors.ENDC}"))
            if choice == 1:
                return 5
            elif choice == 2:
                return 10
            elif choice == 3:
                return 20
            else:
                print(f"{Colors.FAIL}Please enter a number between 1 and 3.{Colors.ENDC}")
        except ValueError:
            print(f"{Colors.FAIL}Please enter a valid number.{Colors.ENDC}")

def get_timer_mode():
    """Let user choose if they want timed mode"""
    print(f"\n{Colors.BOLD}Choose quiz mode:{Colors.ENDC}")
    print(f"{Colors.GREEN}1. 🐌 Relaxed Mode (No time limit)")
    print(f"{Colors.YELLOW}2. ⏰ Timed Mode (30 seconds per question)")
    print(f"{Colors.RED}3. 🚀 Speed Mode (15 seconds per question){Colors.ENDC}")
    
    while True:
        try:
            choice = int(input(f"\n{Colors.BOLD}Enter your choice (1-3): {Colors.ENDC}"))
            if choice == 1:
                return None  # No timer
            elif choice == 2:
                return 30  # 30 seconds
            elif choice == 3:
                return 15  # 15 seconds
            else:
                print(f"{Colors.FAIL}Please enter a number between 1 and 3.{Colors.ENDC}")
        except ValueError:
            print(f"{Colors.FAIL}Please enter a valid number.{Colors.ENDC}")

def display_question(question_num, total_questions, question_data, options):
    """Display a formatted question with options"""
    print(f"{Colors.BOLD}Question {question_num}/{total_questions}:{Colors.ENDC}")
    print(f"{Colors.BLUE}📚 Difficulty: {question_data['difficulty'].title()}{Colors.ENDC}")
    print(f"\n{Colors.YELLOW}{question_data['question']}{Colors.ENDC}\n")
    
    for j, option in enumerate(options, 1):
        print(f"{Colors.CYAN}{j}. {option}{Colors.ENDC}")

def display_result(is_correct, user_answer, correct_answer, explanation, is_timeout=False):
    """Display the result of an answer"""
    if is_correct:
        print(f"\n{Colors.GREEN}✅ Correct! Well done! 🎉{Colors.ENDC}")
    elif is_timeout:
        print(f"\n{Colors.YELLOW}⏰ No answer given. The correct answer was: {correct_answer}{Colors.ENDC}")
    else:
        print(f"\n{Colors.RED}❌ Wrong! The correct answer is: {correct_answer}{Colors.ENDC}")
    
    print(f"{Colors.PURPLE}💡 {explanation}{Colors.ENDC}")

def display_final_score(score, total_questions):
    """Display final quiz results and ranking"""
    percentage = (score / total_questions) * 100
    
    print(f"\n{Colors.BOLD}{Colors.CYAN}🏆 QUIZ COMPLETE! 🏆{Colors.ENDC}\n")
    print(f"{Colors.YELLOW}Final Score: {score}/{total_questions} ({percentage:.1f}%){Colors.ENDC}\n")
    
    # Score evaluation
    if percentage >= 90:
        print(f"{Colors.GREEN}🌟 MUSHROOM MASTER! 🌟")
        print(f"Outstanding! You're ready to start your own mushroom farm! 🍄🚜{Colors.ENDC}")
    elif percentage >= 70:
        print(f"{Colors.CYAN}🍄 FUNGI EXPERT! 🍄")
        print(f"Great job! You have solid mushroom cultivation knowledge! 🎯{Colors.ENDC}")
    elif percentage >= 50:
        print(f"{Colors.YELLOW}🌱 GROWING CULTIVATOR! 🌱")
        print(f"Good start! Keep learning and you'll be a mushroom pro! 📚{Colors.ENDC}")
    else:
        print(f"{Colors.PURPLE}🔰 SPORE BEGINNER! 🔰")
        print(f"Don't worry! Every expert started somewhere. Keep studying! 💪{Colors.ENDC}")

def display_study_recommendations(wrong_topics):
    """Display personalized study recommendations"""
    if wrong_topics:
        unique_topics = list(set(wrong_topics))
        print(f"\n{Colors.BOLD}{Colors.CYAN}📚 Study Recommendations:{Colors.ENDC}")
        
        study_tips = {
            "growing_conditions": "Review optimal temperature and humidity ranges.",
            "mushroom_varieties": "Learn about different types of mushrooms and their characteristics.",
            "substrates": "Explore various substrates used in mushroom cultivation.",
            "biology_basics": "Understand the structure and function of mycelium.",
            "sterilization": "Look into sterilization techniques like pressure cooking.",
            "medicinal_mushrooms": "Research the benefits and uses of medicinal mushrooms.",
            "cultivation_process": "Familiarize yourself with the steps in mushroom cultivation.",
            "beginner_varieties": "Identify beginner-friendly mushrooms to start growing.",
            "growing_methods": "Discover different growing methods such as log cultivation.",
            "timing": "Learn about the timelines for various mushroom cultivation stages."
        }
        
        for topic in unique_topics:
            if topic in study_tips:
                print(f"- {study_tips[topic]}")
    else:
        print(f"{Colors.GREEN}🎉 You're well-rounded in your mushroom knowledge! 🎉{Colors.ENDC}")

def display_main_menu():
    """Display the main menu options"""
    print(f"\n{Colors.BOLD}What would you like to do?{Colors.ENDC}")
    print(f"{Colors.GREEN}1. 🎮 Start Quiz")
    print(f"{Colors.BLUE}2. 📖 About This Quiz")
    print(f"{Colors.RED}3. 🚪 Exit{Colors.ENDC}")

def display_about():
    """Display information about the quiz"""
    print(f"\n{Colors.CYAN}📖 About This Quiz:{Colors.ENDC}")
    print(f"{Colors.YELLOW}This quiz tests your knowledge of mushroom cultivation including:")
    print(f"• Basic growing techniques and conditions")
    print(f"• Different mushroom varieties and their requirements")
    print(f"• Substrate preparation and sterilization")
    print(f"• Common cultivation terminology")
    print(f"• Tips for successful mushroom farming{Colors.ENDC}\n")

