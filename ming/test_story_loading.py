#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

# Add the current directory to the path so we can import the module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from relationship_content_generator import load_story_ideas_from_file

def test_story_loading():
    """Test if story loading works correctly"""
    print("=== 測試故事載入功能 ===")
    
    # Test loading stories
    scenarios = load_story_ideas_from_file()
    
    print(f"📊 載入到 {len(scenarios)} 個故事場景")
    
    if scenarios:
        print("\n📝 故事列表：")
        for i, scenario in enumerate(scenarios, 1):
            print(f"{i}. 主題：{scenario['theme']}")
            print(f"   故事：{scenario['story_template'][:50]}...")
            print(f"   視角：{scenario['perspective']}")
            print()
    else:
        print("❌ 冇載入到任何故事")
    
    return scenarios

if __name__ == "__main__":
    test_story_loading() 