#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🎯 Quiz Engine Module

Core quiz functionality and game logic for the Mushroom Cultivation Quiz.

File: quiz_engine.py
Author: Aaron J
Email: git@aaronemail.xyz
Version: 2.0.1
Created: 2025-06-21
Last Modified: 2025-06-23

Description:
    This module contains the QuizGame class and related functions that handle
    the core quiz logic, including question selection, answer processing,
    scoring, and result analysis. It serves as the central coordinator between
    the UI, timer, and question database modules.

Classes:
    QuizGame: Main quiz game class that manages quiz flow and scoring
        - Handles question preparation and randomization
        - Processes user answers and maintains score
        - Tracks wrong topics for study recommendations
        - Coordinates with UI and timer modules

Functions:
    create_quiz(): Factory function to create and run a quiz instance

Features:
    - Intelligent question selection based on difficulty
    - Random question and option shuffling for variety
    - Answer validation and timeout handling
    - Topic-based performance tracking
    - Integration with timed and untimed input modes
    - Comprehensive result reporting

Dependencies:
    - random: For question and option shuffling
    - time: For timing delays and user experience
    - ..data.question_loader: Question database and filtering functions
    - ..ui.terminal_ui: Display functions and color constants
    - .timer: Timed input functionality

Usage:
    from mushroom_quiz.core import create_quiz
    score, total = create_quiz("intermediate", 10, 30)

License:
    MIT License - See LICENSE file for details
"""

import random
import time
from ..data.question_loader import get_questions_by_difficulty, get_all_questions
from ..ui.terminal_ui import (clear_screen, print_header, display_question, 
                     display_result, display_final_score, display_study_recommendations, Colors)
from .timer import get_user_input

class QuizGame:
    """Main quiz game class that handles quiz flow and scoring"""
    
    def __init__(self, difficulty="mixed", num_questions=10, timer_seconds=None):
        self.difficulty = difficulty
        self.num_questions = num_questions
        self.timer_seconds = timer_seconds
        self.score = 0
        self.wrong_topics = []
        
    def prepare_questions(self):
        """Prepare and select questions for the quiz"""
        questions = get_questions_by_difficulty(self.difficulty)
        
        # Fallback to all questions if not enough in the selected difficulty
        if len(questions) < self.num_questions:
            questions = get_all_questions()
        
        # Select random questions
        return random.sample(questions, min(self.num_questions, len(questions)))
    
    def run_quiz(self):
        """Main quiz execution method"""
        selected_questions = self.prepare_questions()
        total_questions = len(selected_questions)
        
        # Initialize quiz
        clear_screen()
        print_header()
        print(f"\n{Colors.BOLD}{Colors.CYAN}🎯 Quiz Starting! You'll answer {total_questions} questions.{Colors.ENDC}\n")
        time.sleep(2)
        
        # Process each question
        for i, question_data in enumerate(selected_questions, 1):
            self._process_question(i, total_questions, question_data)
            
            # Show continuation prompt except for last question
            if i < total_questions:
                input(f"\n{Colors.BOLD}Press Enter to continue...{Colors.ENDC}")
                clear_screen()
                print_header()
        
        # Display final results
        self._show_final_results(total_questions)
        
        return self.score, total_questions
    
    def _process_question(self, question_num, total_questions, question_data):
        """Process a single question"""
        # Shuffle options for variety
        options = question_data['options'].copy()
        random.shuffle(options)
        
        # Display question
        display_question(question_num, total_questions, question_data, options)
        
        # Get user answer
        answer_num = get_user_input(
            f"\n{Colors.BOLD}Your answer (1-{len(options)}): {Colors.ENDC}",
            len(options),
            self.timer_seconds
        )
        
        # Process answer
        if answer_num is not None:
            user_answer = options[answer_num - 1]
            is_correct = user_answer == question_data['answer']
            is_timeout = False
        else:
            user_answer = None
            is_correct = False
            is_timeout = True
        
        # Update score and track wrong topics
        if is_correct:
            self.score += 1
        elif not is_timeout:
            self.wrong_topics.append(question_data['topic'])
        
        # Display result
        display_result(
            is_correct, 
            user_answer, 
            question_data['answer'], 
            question_data['explanation'],
            is_timeout
        )
    
    def _show_final_results(self, total_questions):
        """Display final quiz results and recommendations"""
        display_final_score(self.score, total_questions)
        display_study_recommendations(self.wrong_topics)

def create_quiz(difficulty, num_questions, timer_seconds):
    """Factory function to create and run a quiz"""
    quiz = QuizGame(difficulty, num_questions, timer_seconds)
    return quiz.run_quiz()
