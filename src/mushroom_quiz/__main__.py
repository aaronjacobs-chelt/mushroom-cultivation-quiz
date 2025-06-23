#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🍄 Mushroom Cultivation Quiz - Main Entry Point 🍄

Entry point for running the mushroom quiz package directly.

File: __main__.py
Author: Aaron J
Email: git@aaronemail.xyz
Version: 2.0.1
Created: 2025-06-23
Last Modified: 2025-06-23
License: MIT

Description:
    This module allows the package to be run directly using:
    python -m mushroom_quiz
    
    It imports and executes the main application function from app.py.
    
Usage:
    python -m mushroom_quiz
    
Repository:
    https://github.com/aaronjacobs-chelt/mushroom-cultivation-quiz
"""

from .app import main

if __name__ == "__main__":
    main()
