#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📊 Data Management Module 📊

Data management modules for quiz questions and content.

File: data/__init__.py
Author: Aaron J
Email: git@aaronemail.xyz
Version: 2.0.1
Created: 2025-06-23
Last Modified: 2025-06-23
License: MIT

Description:
    This module handles data management for the Mushroom Cultivation Quiz,
    including question loading, filtering, and organization. It provides
    a clean interface for accessing quiz questions by difficulty level.
    
Exports:
    - get_questions_by_difficulty: Get questions filtered by difficulty
    - get_all_questions: Get all available questions
    
Repository:
    https://github.com/aaronjacobs-chelt/mushroom-cultivation-quiz
"""

from .question_loader import get_questions_by_difficulty, get_all_questions

__all__ = ["get_questions_by_difficulty", "get_all_questions"]
