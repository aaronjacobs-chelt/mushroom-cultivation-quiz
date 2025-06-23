#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📚 Question Loading and Management Module 📚

Provides functions to load and filter quiz questions by difficulty level.

File: question_loader.py
Author: Aaron J
Email: git@aaronemail.xyz
Version: 2.0.1
Created: 2025-06-23
Last Modified: 2025-06-23
License: MIT

Description:
    This module provides an abstraction layer for loading and filtering
    quiz questions from the question database. It handles difficulty-based
    filtering and provides convenient functions for question management.
    
Functions:
    - get_questions_by_difficulty(): Filter questions by difficulty level
    - get_all_questions(): Get all available questions
    - get_question_count_by_difficulty(): Count questions by difficulty
    - get_difficulty_levels(): Get list of available difficulty levels
    
Supported Difficulty Levels:
    - beginner: Easy questions for newcomers
    - intermediate: Moderate difficulty questions
    - advanced: Challenging questions for experts
    - mixed: Questions from all difficulty levels
    
Repository:
    https://github.com/aaronjacobs-chelt/mushroom-cultivation-quiz
"""

from .quiz_questions import get_questions_by_difficulty as _get_questions_by_difficulty, QUESTIONS

def get_questions_by_difficulty(difficulty):
    """
    Get questions filtered by difficulty level.
    
    Args:
        difficulty (str): Difficulty level ('beginner', 'intermediate', 'advanced', 'mixed')
        
    Returns:
        list: List of question dictionaries for the specified difficulty
    """
    if difficulty == 'mixed':
        return get_all_questions()
    else:
        return _get_questions_by_difficulty(difficulty)

def get_all_questions():
    """
    Get all questions from all difficulty levels.
    
    Returns:
        list: Combined list of all questions
    """
    return QUESTIONS

def get_question_count_by_difficulty(difficulty):
    """
    Get the number of questions available for a given difficulty.
    
    Args:
        difficulty (str): Difficulty level
        
    Returns:
        int: Number of questions available
    """
    return len(get_questions_by_difficulty(difficulty))

def get_difficulty_levels():
    """
    Get list of available difficulty levels.
    
    Returns:
        list: Available difficulty level strings
    """
    return ['beginner', 'intermediate', 'advanced', 'mixed']
