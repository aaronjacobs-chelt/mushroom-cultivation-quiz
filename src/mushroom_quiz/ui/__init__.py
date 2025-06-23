#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📺 User Interface Module 📺

User interface modules for the Mushroom Cultivation Quiz application.

File: ui/__init__.py
Author: Aaron J
Email: git@aaronemail.xyz
Version: 2.0.1
Created: 2025-06-23
Last Modified: 2025-06-23
License: MIT

Description:
    This module provides user interface components for the quiz application,
    including terminal-based UI functions, color styling, and interactive
    menu systems. It exports all the UI functions needed by the main app.
    
Exports:
    - clear_screen: Clear terminal screen
    - print_header: Display application header
    - display_main_menu: Show main menu options
    - display_about: Show about information
    - get_difficulty_level: Get user's difficulty preference
    - get_number_of_questions: Get desired number of questions
    - get_timer_mode: Get timer mode preference
    - Colors: Color constants for terminal styling
    
Repository:
    https://github.com/aaronjacobs-chelt/mushroom-cultivation-quiz
"""

from .terminal_ui import (
    clear_screen, print_header, display_main_menu, display_about,
    get_difficulty_level, get_number_of_questions, get_timer_mode, Colors
)

__all__ = [
    "clear_screen", "print_header", "display_main_menu", "display_about",
    "get_difficulty_level", "get_number_of_questions", "get_timer_mode", "Colors"
]
