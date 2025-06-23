#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔧 Utility Helper Functions 🔧

Utility helper functions for the Mushroom Cultivation Quiz application.

File: helpers.py
Author: Aaron J
Email: git@aaronemail.xyz
Version: 2.0.1
Created: 2025-06-23
Last Modified: 2025-06-23
License: MIT

Description:
    This module contains common utility functions that can be used across
    different modules of the quiz application. It provides input validation,
    formatting utilities, and other helper functions.
    
Functions:
    - validate_input(): Validate user input within specified ranges
    - format_percentage(): Format percentages for display
    - get_performance_level(): Get performance level based on score
    - truncate_text(): Truncate text with ellipsis
    
Usage:
    from mushroom_quiz.utils import validate_input, format_percentage
    
    score = validate_input("5", 1, 10)  # Returns 5
    percent = format_percentage(8, 10)   # Returns "80.0%"
    
Repository:
    https://github.com/aaronjacobs-chelt/mushroom-cultivation-quiz
"""

def validate_input(user_input, min_value, max_value):
    """
    Validate user input is within specified range.
    
    Args:
        user_input (str): User input string
        min_value (int): Minimum acceptable value
        max_value (int): Maximum acceptable value
        
    Returns:
        int or None: Validated integer value or None if invalid
    """
    try:
        value = int(user_input.strip())
        if min_value <= value <= max_value:
            return value
        return None
    except (ValueError, AttributeError):
        return None

def format_percentage(correct, total):
    """
    Format a percentage from correct answers and total questions.
    
    Args:
        correct (int): Number of correct answers
        total (int): Total number of questions
        
    Returns:
        str: Formatted percentage string
    """
    if total == 0:
        return "0%"
    percentage = (correct / total) * 100
    return f"{percentage:.1f}%"

def get_performance_level(score, total):
    """
    Get performance level description based on score.
    
    Args:
        score (int): Number of correct answers
        total (int): Total number of questions
        
    Returns:
        tuple: (level_name, emoji, description)
    """
    if total == 0:
        return "No Questions", "❓", "No questions were answered"
    
    percentage = (score / total) * 100
    
    if percentage >= 90:
        return "Expert", "🏆", "Outstanding knowledge!"
    elif percentage >= 80:
        return "Advanced", "⭐", "Excellent work!"
    elif percentage >= 70:
        return "Proficient", "👍", "Good understanding!"
    elif percentage >= 60:
        return "Developing", "📚", "Keep studying!"
    else:
        return "Beginner", "🌱", "Room for improvement!"

def truncate_text(text, max_length=50):
    """
    Truncate text to a maximum length with ellipsis.
    
    Args:
        text (str): Text to truncate
        max_length (int): Maximum length before truncation
        
    Returns:
        str: Truncated text with ellipsis if needed
    """
    if len(text) <= max_length:
        return text
    return text[:max_length-3] + "..."
