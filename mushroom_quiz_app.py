#!/usr/bin/env python3
"""
🍄 Mushroom Cultivation Quiz Application 🍄
Main application file that coordinates all modules

This modular quiz application tests knowledge about mushroom cultivation
including growing techniques, varieties, substrates, and terminology.
"""

from quiz_ui import (clear_screen, print_header, display_main_menu, display_about,
                     get_difficulty_level, get_number_of_questions, get_timer_mode, Colors)
from quiz_logic import create_quiz

def main():
    """Main application entry point"""
    clear_screen()
    print_header()
    
    try:
        while True:
            display_main_menu()
            
            try:
                choice = int(input(f"\n{Colors.BOLD}Enter your choice (1-3): {Colors.ENDC}"))
                
                if choice == 1:
                    # Start Quiz
                    run_quiz_session()
                    
                    # Ask if they want to play again
                    play_again = input(f"\n{Colors.BOLD}Would you like to play again? (y/n): {Colors.ENDC}").lower()
                    if play_again != 'y':
                        break
                    else:
                        clear_screen()
                        print_header()
                        
                elif choice == 2:
                    # Show About information
                    display_about()
                    input(f"{Colors.BOLD}Press Enter to return to menu...{Colors.ENDC}")
                    clear_screen()
                    print_header()
                    
                elif choice == 3:
                    # Exit application
                    print(f"\n{Colors.GREEN}Thanks for playing! Happy mushroom growing! 🍄🌟{Colors.ENDC}")
                    break
                    
                else:
                    print(f"{Colors.FAIL}Please enter a number between 1 and 3.{Colors.ENDC}")
                    
            except ValueError:
                print(f"{Colors.FAIL}Please enter a valid number.{Colors.ENDC}")
                
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Thanks for playing! 🍄{Colors.ENDC}")

def run_quiz_session():
    """Handle a complete quiz session"""
    # Get quiz parameters from user
    difficulty = get_difficulty_level()
    num_questions = get_number_of_questions()
    timer_seconds = get_timer_mode()
    
    # Run the quiz
    score, total = create_quiz(difficulty, num_questions, timer_seconds)
    
    # Return results (could be used for statistics tracking)
    return score, total

if __name__ == "__main__":
    main()

