#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🎯 Core Quiz Functionality Module 🎯

Core quiz functionality modules for the Mushroom Cultivation Quiz.

File: core/__init__.py
Author: Aaron J
Email: git@aaronemail.xyz
Version: 2.0.1
Created: 2025-06-23
Last Modified: 2025-06-23
License: MIT

Description:
    This module provides the core functionality for the quiz application,
    including the quiz engine and timer functionality. It exports the main
    interfaces needed by other parts of the application.
    
Exports:
    - create_quiz: Main quiz creation and execution function
    - get_user_input: Timer-aware user input function
    - TimerColors: Color constants for timer display
    
Repository:
    https://github.com/aaronjacobs-chelt/mushroom-cultivation-quiz
"""

from .quiz_engine import create_quiz
from .timer import get_user_input, Colors as TimerColors

__all__ = ["create_quiz", "get_user_input", "TimerColors"]
