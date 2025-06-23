#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧪 Test Suite for Question Loader Module 🧪

Tests for the question loader functionality.

File: test_question_loader.py
Author: Aaron J
Email: git@aaronemail.xyz
Version: 2.0.1
Created: 2025-06-23
Last Modified: 2025-06-23
License: MIT

Description:
    This module contains unit tests for the question loader functionality,
    testing question filtering, counting, and difficulty level management.
    
Test Classes:
    - TestQuestionLoader: Main test class for question loader functionality
    
Usage:
    python -m pytest tests/test_question_loader.py
    python -m unittest tests.test_question_loader
    
Repository:
    https://github.com/aaronjacobs-chelt/mushroom-cultivation-quiz
"""

import unittest
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from mushroom_quiz.data.question_loader import (
    get_questions_by_difficulty, get_all_questions, 
    get_question_count_by_difficulty, get_difficulty_levels
)

class TestQuestionLoader(unittest.TestCase):
    """Test cases for question loader functionality."""
    
    def test_get_difficulty_levels(self):
        """Test that difficulty levels are returned correctly."""
        levels = get_difficulty_levels()
        expected_levels = ['beginner', 'intermediate', 'advanced', 'mixed']
        self.assertEqual(levels, expected_levels)
    
    def test_get_questions_by_difficulty_beginner(self):
        """Test getting beginner questions."""
        questions = get_questions_by_difficulty('beginner')
        self.assertIsInstance(questions, list)
        self.assertGreater(len(questions), 0)
    
    def test_get_questions_by_difficulty_intermediate(self):
        """Test getting intermediate questions."""
        questions = get_questions_by_difficulty('intermediate')
        self.assertIsInstance(questions, list)
        self.assertGreater(len(questions), 0)
    
    def test_get_questions_by_difficulty_advanced(self):
        """Test getting advanced questions."""
        questions = get_questions_by_difficulty('advanced')
        self.assertIsInstance(questions, list)
        self.assertGreater(len(questions), 0)
    
    def test_get_questions_by_difficulty_mixed(self):
        """Test getting mixed questions."""
        questions = get_questions_by_difficulty('mixed')
        all_questions = get_all_questions()
        self.assertEqual(len(questions), len(all_questions))
    
    def test_get_questions_invalid_difficulty(self):
        """Test handling of invalid difficulty level."""
        questions = get_questions_by_difficulty('invalid')
        self.assertIsInstance(questions, list)
        self.assertEqual(len(questions), 0)  # Should return empty list for invalid difficulty
    
    def test_get_all_questions(self):
        """Test getting all questions."""
        all_questions = get_all_questions()
        self.assertIsInstance(all_questions, list)
        self.assertGreater(len(all_questions), 0)
    
    def test_get_question_count_by_difficulty(self):
        """Test question count functionality."""
        beginner_count = get_question_count_by_difficulty('beginner')
        self.assertIsInstance(beginner_count, int)
        self.assertGreater(beginner_count, 0)

if __name__ == '__main__':
    unittest.main()
