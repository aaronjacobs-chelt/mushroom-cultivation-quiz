#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔧 Utility Modules 🔧

Utility modules for the Mushroom Cultivation Quiz application.

File: utils/__init__.py
Author: Aaron J
Email: git@aaronemail.xyz
Version: 2.0.1
Created: 2025-06-23
Last Modified: 2025-06-23
License: MIT

Description:
    This module provides utility functions and helper classes for the
    quiz application. It includes common functionality that can be
    shared across different parts of the application.
    
Exports:
    - validate_input: Validate user input within specified ranges
    - format_percentage: Format percentages for display
    
Repository:
    https://github.com/aaronjacobs-chelt/mushroom-cultivation-quiz
"""

from .helpers import validate_input, format_percentage

__all__ = ["validate_input", "format_percentage"]
