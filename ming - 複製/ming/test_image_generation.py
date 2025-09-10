#!/usr/bin/env python3
"""
Test script to verify image generation with text content.
This script tests that the templates generate images with visible text.
"""

import asyncio
import sys
import os

# Add the ming directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'ming'))

from relationship_template_generator import (
    generate_relationship_title_template,
    generate_relationship_story_template,
    generate_relationship_conclusion_template,
    generate_relationship_end_template
)
from image_generator import generate_images_from_templates

async def test_image_generation():
    """Test that images are generated with visible text content"""
    
    print("🧪 Testing Image Generation with Text Content")
    print("=" * 50)
    
    # Test data with clear text content
    test_title_content = {
        'title': '我男朋友為咗買翻版公仔，就算要行好遠都要去買？',
        'keywords': ['男朋友', '翻版公仔', '行好遠']
    }
    
    test_story_point = {
        'title': '瘋狂購物',
        'description': '我男朋友最近迷上咗收集翻版公仔，每個禮拜都要去唔同地方買。佢話呢啲公仔好有紀念價值，但係我覺得佢已經有太多嘞。佢試過為咗買一隻限量版公仔，特登請假去排隊，仲要排咗成日。我開始擔心佢係咪太沉迷，但係佢話呢個係佢嘅興趣，叫我支持佢。'
    }
    
    test_conclusion_content = {
        'conclusion': '你哋覺得我應該點樣同佢傾呢件事？佢嘅興趣係咪真係咁重要？'
    }
    
    test_keywords = ['男朋友', '翻版公仔', '興趣', '支持']
    
    print("📝 Creating test templates...")
    
    # Create test templates
    templates = {
        'title': generate_relationship_title_template(
            test_title_content, 
            test_keywords,
            perspective="female"
        ),
        'story1': generate_relationship_story_template(
            test_story_point, 
            test_keywords,
            page_number=1,
            perspective="female"
        ),
        'conclusion': generate_relationship_conclusion_template(
            test_conclusion_content, 
            test_keywords,
            perspective="female"
        ),
        'end': generate_relationship_end_template(perspective="female")
    }
    
    print("✅ Templates created successfully")
    print()
    
    # Test HTML content
    print("🔍 Checking HTML content...")
    for template_name, html_content in templates.items():
        print(f"   {template_name}:")
        if 'xiaohongshu-post' in html_content:
            print(f"     ✅ Contains xiaohongshu-post element")
        else:
            print(f"     ❌ Missing xiaohongshu-post element")
        
        # Check for text content
        if '我男朋友' in html_content or '翻版公仔' in html_content or '你哋覺得' in html_content:
            print(f"     ✅ Contains test text content")
        else:
            print(f"     ⚠️  No test text found")
        
        # Check for styling
        if 'background:' in html_content and 'font-size:' in html_content:
            print(f"     ✅ Contains styling")
        else:
            print(f"     ❌ Missing styling")
        
        print()
    
    # Generate images
    print("🖼️  Generating images...")
    try:
        png_paths = await generate_images_from_templates(templates, "test_person")
        
        if png_paths:
            print(f"✅ Successfully generated {len(png_paths)} images:")
            for path in png_paths:
                print(f"   📄 {path}")
                
                # Check if file exists and has content
                if os.path.exists(path):
                    file_size = os.path.getsize(path)
                    print(f"      📊 File size: {file_size} bytes")
                    if file_size > 1000:  # More than 1KB
                        print(f"      ✅ File has substantial content")
                    else:
                        print(f"      ⚠️  File seems small, might be empty")
                else:
                    print(f"      ❌ File not found")
        else:
            print("❌ No images were generated")
            
    except Exception as e:
        print(f"❌ Error generating images: {e}")
        import traceback
        traceback.print_exc()
    
    print()
    print("🎯 Test completed!")
    print("If images were generated successfully, check them to verify text is visible.")

if __name__ == "__main__":
    asyncio.run(test_image_generation()) 