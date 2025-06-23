#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔄 Legacy Wrapper Script 🔄

Legacy wrapper script for backward compatibility.

File: mushroom_quiz_app_legacy.py
Author: Aaron J
Email: git@aaronemail.xyz
Version: 2.0.1
Created: 2025-06-23
Last Modified: 2025-06-23
License: MIT

Description:
    This script maintains compatibility with the old mushroom_quiz_app.py entry point
    while redirecting to the new modular package structure. It provides a bridge
    for users who may still be using the old entry point.
    
Usage:
    python mushroom_quiz_app_legacy.py
    
Note:
    This is a legacy entry point. Consider using:
    - python -m mushroom_quiz
    - mushroom-quiz (after installation)
    
Repository:
    https://github.com/aaronjacobs-chelt/mushroom-cultivation-quiz
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from mushroom_quiz import main
    
    if __name__ == "__main__":
        print("⚠️  Note: This is a legacy entry point. Consider using 'python -m mushroom_quiz' or 'mushroom-quiz' command.")
        main()
        
except ImportError as e:
    print(f"Error importing mushroom_quiz package: {e}")
    print("Please ensure the package is properly installed or run from the project directory.")
    sys.exit(1)
