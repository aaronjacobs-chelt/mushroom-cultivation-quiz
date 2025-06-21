#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
⏰ Quiz Timer Module

Handles timed input functionality with visual countdown for quiz questions.

File: quiz_timer.py
Author: Aaron J
Version: 2.0.0
Created: 2025-06-21
Last Modified: 2025-06-21

Description:
    This module provides timed input functionality for the quiz application,
    featuring visual countdown displays and thread-based input handling.
    It supports both timed and untimed input modes with proper timeout
    management and user feedback.

Classes:
    TimedInput: Handles timed input with countdown display
        - Thread-based input collection
        - Visual countdown with color-coded time remaining
        - Timeout detection and handling
        - Answer validation within time constraints

Functions:
    get_user_input(): Main interface for getting user input (timed or untimed)

Features:
    - Visual countdown timer with color coding:
      * Green: >10 seconds remaining
      * Yellow: 5-10 seconds remaining  
      * Red: <5 seconds remaining
    - Thread-safe input handling
    - Graceful timeout management
    - Answer validation (numeric range checking)
    - Support for both timed and untimed modes
    - Real-time countdown display

Timer Modes:
    - Relaxed Mode: No time limit
    - Timed Mode: 30 seconds per question
    - Speed Mode: 15 seconds per question

Dependencies:
    - threading: For non-blocking input collection
    - time: For countdown timing and delays
    - quiz_ui: Color constants for countdown display

Usage:
    from quiz_timer import get_user_input
    answer = get_user_input("Your choice: ", 4, 30)  # 30 second timeout
    answer = get_user_input("Your choice: ", 4)      # No timeout

License:
    MIT License - See LICENSE file for details
"""

import threading
import time
from quiz_ui import Colors

class TimedInput:
    """Class to handle timed input with countdown display"""
    def __init__(self, timeout):
        self.timeout = timeout
        self.answer = None
        self.timed_out = False
    
    def input_thread(self, prompt):
        """Thread function to get input"""
        try:
            self.answer = input(prompt)
        except:
            pass
    
    def get_timed_input(self, prompt, options_count):
        """Get input with timeout and countdown display"""
        print(f"\n{Colors.WARNING}⏰ You have {self.timeout} seconds to answer!{Colors.ENDC}")
        
        # Start input thread
        input_thread = threading.Thread(target=self.input_thread, args=(prompt,))
        input_thread.daemon = True
        input_thread.start()
        
        # Countdown loop
        for remaining in range(self.timeout, 0, -1):
            if not input_thread.is_alive():
                break
            
            # Display countdown
            countdown_color = Colors.GREEN if remaining > 10 else Colors.YELLOW if remaining > 5 else Colors.RED
            print(f"\r{countdown_color}⏰ Time remaining: {remaining:2d} seconds{Colors.ENDC}", end="", flush=True)
            time.sleep(1)
        
        if input_thread.is_alive():
            self.timed_out = True
            print(f"\n\n{Colors.FAIL}⏰ Time's up!{Colors.ENDC}")
            return None
        else:
            print()  # New line after countdown
            try:
                answer_num = int(self.answer)
                if 1 <= answer_num <= options_count:
                    return answer_num
                else:
                    return None
            except (ValueError, TypeError):
                return None

def get_user_input(prompt, options_count, timer_seconds=None):
    """Get user input with optional timer"""
    if timer_seconds:
        timer = TimedInput(timer_seconds)
        return timer.get_timed_input(prompt, options_count)
    else:
        # Normal mode without timer
        while True:
            try:
                answer_num = int(input(prompt))
                if 1 <= answer_num <= options_count:
                    return answer_num
                else:
                    print(f"{Colors.FAIL}Please enter a number between 1 and {options_count}.{Colors.ENDC}")
            except ValueError:
                print(f"{Colors.FAIL}Please enter a valid number.{Colors.ENDC}")

