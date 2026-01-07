#!/usr/bin/env python3
"""
Wrapper script to run custom story generation
"""
import asyncio
import sys
import os

# Add the current directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from relationship_main import generate_custom_story_content

if __name__ == "__main__":
    asyncio.run(generate_custom_story_content())
