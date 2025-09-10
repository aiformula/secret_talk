#!/usr/bin/env python3
"""
Test script to verify language improvements in the relationship content generator.
This script tests that the AI avoids unnatural Cantonese expressions and uses more natural alternatives.
"""

import asyncio
import openai
import sys
import os

# Add the ming directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'ming'))

from relationship_content_generator import (
    generate_relationship_title_content,
    generate_relationship_story_content,
    generate_relationship_conclusion_content,
    generate_instagram_caption,
    get_random_story_scenario
)

# Test story that previously generated unnatural expressions
TEST_STORY = "我男朋友為咗買翻版公仔，就算要行好遠都要去買。我覺得佢好傻，但佢話呢啲公仔好有紀念價值。我唔知應該點睇呢件事。"

# Unnatural expressions to check for
UNNATURAL_EXPRESSIONS = [
    "借咩",  # Should be "咩男朋友嚟㗎" or "邊個男朋友"
    "靠山走水",  # Should be "翻山越嶺" or "就算要行好遠"
    "有形嘅",  # Should be "有型嘅" or "靚仔嘅"
    "意外嚇",  # Should be "嚇親" or "嚇到"
    "曬爛",  # Should be "曬到爛" or "曬到變色"
    "真係為咗錢咩真係咁啦一齊",  # Should be "真係為咗錢咩？真係咁樣一齊？"
]

# Natural alternatives that should be used instead
NATURAL_ALTERNATIVES = [
    "咩男朋友嚟㗎",
    "邊個男朋友",
    "翻山越嶺",
    "就算要行好遠",
    "有型嘅",
    "靚仔嘅",
    "嚇親",
    "嚇到",
    "曬到爛",
    "曬到變色",
    "真係為咗錢咩？真係咁樣一齊？"
]

async def test_language_improvements():
    """Test that the content generator avoids unnatural expressions"""
    
    # Initialize OpenAI client (you'll need to set your API key)
    try:
        client = openai.AsyncOpenAI()
    except Exception as e:
        print(f"Error initializing OpenAI client: {e}")
        print("Please make sure you have set your OpenAI API key.")
        return
    
    print("🧪 Testing Language Improvements in Relationship Content Generator")
    print("=" * 60)
    
    # Get a random scenario
    scenario = get_random_story_scenario()
    print(f"📝 Using scenario: {scenario['theme']}")
    print(f"📖 Base story: {scenario['story_template'][:100]}...")
    print()
    
    try:
        # Test title generation
        print("1️⃣ Testing Title Generation...")
        title_content = await generate_relationship_title_content(client, TEST_STORY, scenario)
        print(f"   Generated title: {title_content['title']}")
        print(f"   Keywords: {title_content['keywords']}")
        
        # Check for unnatural expressions in title
        found_unnatural = []
        for expr in UNNATURAL_EXPRESSIONS:
            if expr in title_content['title']:
                found_unnatural.append(expr)
        
        if found_unnatural:
            print(f"   ⚠️  Found unnatural expressions: {found_unnatural}")
        else:
            print("   ✅ No unnatural expressions found in title")
        
        print()
        
        # Test story content generation
        print("2️⃣ Testing Story Content Generation...")
        story_content = await generate_relationship_story_content(client, TEST_STORY, scenario)
        print(f"   Hook: {story_content['hook']}")
        
        # Check for unnatural expressions in story content
        all_content = f"{story_content['hook']} " + " ".join([point['description'] for point in story_content['story_points']])
        found_unnatural = []
        for expr in UNNATURAL_EXPRESSIONS:
            if expr in all_content:
                found_unnatural.append(expr)
        
        if found_unnatural:
            print(f"   ⚠️  Found unnatural expressions: {found_unnatural}")
        else:
            print("   ✅ No unnatural expressions found in story content")
        
        print()
        
        # Test conclusion generation
        print("3️⃣ Testing Conclusion Generation...")
        conclusion_content = await generate_relationship_conclusion_content(client, story_content)
        print(f"   Conclusion: {conclusion_content['conclusion']}")
        
        # Check for unnatural expressions in conclusion
        found_unnatural = []
        for expr in UNNATURAL_EXPRESSIONS:
            if expr in conclusion_content['conclusion']:
                found_unnatural.append(expr)
        
        if found_unnatural:
            print(f"   ⚠️  Found unnatural expressions: {found_unnatural}")
        else:
            print("   ✅ No unnatural expressions found in conclusion")
        
        print()
        
        # Test Instagram caption generation
        print("4️⃣ Testing Instagram Caption Generation...")
        ig_caption = await generate_instagram_caption(client, story_content, word_limit=200)
        print(f"   Caption preview: {ig_caption[:100]}...")
        
        # Check for unnatural expressions in caption
        found_unnatural = []
        for expr in UNNATURAL_EXPRESSIONS:
            if expr in ig_caption:
                found_unnatural.append(expr)
        
        if found_unnatural:
            print(f"   ⚠️  Found unnatural expressions: {found_unnatural}")
        else:
            print("   ✅ No unnatural expressions found in caption")
        
        print()
        
        # Summary
        print("📊 Summary:")
        print("   The AI should now avoid these unnatural expressions:")
        for expr in UNNATURAL_EXPRESSIONS:
            print(f"   - ❌ {expr}")
        
        print("\n   And use these natural alternatives instead:")
        for alt in NATURAL_ALTERNATIVES:
            print(f"   - ✅ {alt}")
        
        print("\n🎯 Test completed! Check the results above to see if the improvements are working.")
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_language_improvements()) 