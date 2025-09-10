import asyncio
import json
import os
from pathlib import Path

# Import the new relationship modules
from relationship_content_generator import (
    generate_relationship_title_content,
    generate_relationship_story_content, 
    generate_relationship_conclusion_content,
    generate_instagram_caption,
    generate_varied_relationship_content,
    RELATIONSHIP_STORY_TEMPLATES
)
from relationship_template_generator import (
    generate_relationship_title_template,
    generate_relationship_story_template,
    generate_relationship_conclusion_template,
    generate_relationship_end_template
)
from image_generator import generate_images_from_templates
from telegram_sender import send_telegram_photos
from config import setup_environment

async def generate_relationship_content():
    """Main function to generate relationship story content with variation each time"""
    try:
        # Setup environment and get clients
        print("\n=== Setting up environment ===")
        clients = setup_environment()
        
        # Generate varied content using random scenarios
        print("\n=== Generating Varied AI Content ===")
        content_data = await generate_varied_relationship_content(clients['openai_client'])
        
        # Extract generated content
        scenario = content_data['scenario']
        title_content = content_data['title_content'] 
        story_content = content_data['story_content']
        conclusion_content = content_data['conclusion_content']
        ig_caption = content_data['ig_caption']
        
        print(f"\n=== 生成內容摘要 ===")
        print(f"主題：{scenario['theme']}")
        print("標題:", json.dumps(title_content, indent=2, ensure_ascii=False))
        print("故事要點:", len(story_content['story_points']), "個")
        print("結論:", conclusion_content['conclusion'][:50] + "...")
        print("\nInstagram Caption預覽:")
        print(ig_caption[:100] + "...")
        
        # Save the Instagram caption to file (replace existing)
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        caption_filename = 'generated_ig_caption.txt'
        with open(caption_filename, 'w', encoding='utf-8') as f:
            f.write(f"主題：{scenario['theme']}\n")
            f.write(f"生成時間：{timestamp}\n\n")
            f.write(ig_caption)
        print(f"Instagram標題已保存到：{caption_filename}")
        
        # Generate HTML templates
        print("\n=== Generating HTML Templates ===")
        
        # Get perspective from scenario
        perspective = scenario.get('perspective', 'female')
        print(f"使用視角：{perspective} ({'男性' if perspective == 'male' else '女性'})")
        
        templates = {
            'title': generate_relationship_title_template(
                title_content, 
                title_content['keywords'],
                perspective=perspective
            ),
            'story1': generate_relationship_story_template(
                story_content['story_points'][0], 
                story_content['keywords'],
                page_number=1,
                perspective=perspective
            ),
            'story2': generate_relationship_story_template(
                story_content['story_points'][1], 
                story_content['keywords'],
                page_number=2,
                perspective=perspective
            ),
            'story3': generate_relationship_story_template(
                story_content['story_points'][2], 
                story_content['keywords'],
                page_number=3,
                perspective=perspective
            ),
            'conclusion': generate_relationship_conclusion_template(
                conclusion_content, 
                story_content['keywords'],
                perspective=perspective
            ),
            'end': generate_relationship_end_template(perspective=perspective)
        }
        
        # Generate images from templates
        print("\n=== Generating Images ===")
        png_paths = await generate_images_from_templates(templates, f"relationship_{timestamp}")
        
        # Send to Telegram if images were generated successfully
        if png_paths:
            print("\n=== Sending to Telegram ===")
            telegram_caption = f"🎭 {scenario['theme']} 故事\n生成時間：{timestamp}\n\n{ig_caption}"
            await send_telegram_photos(
                clients['telegram_bot'], 
                clients['telegram_chat_id'], 
                png_paths, 
                telegram_caption
            )
            print("Successfully sent to Telegram!")
        else:
            print("No images generated, skipping Telegram upload")
        
        return {
            'scenario': scenario,
            'title_content': title_content,
            'story_content': story_content,
            'conclusion_content': conclusion_content,
            'ig_caption': ig_caption,
            'templates': templates,
            'png_paths': png_paths,
            'timestamp': timestamp
        }
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise

async def test_template_generation():
    """Test function to generate templates without AI content"""
    print("\n=== Testing Template Generation ===")
    
    # Use the predefined template
    template_data = RELATIONSHIP_STORY_TEMPLATES["superstition_plastic_surgery"]
    
    templates = {
        'title': generate_relationship_title_template(
            {'title': template_data['title']}, 
            template_data['keywords']
        ),
        'story1': generate_relationship_story_template(
            template_data['story_points'][0], 
            template_data['keywords'],
            page_number=1
        ),
        'story2': generate_relationship_story_template(
            template_data['story_points'][1], 
            template_data['keywords'],
            page_number=2
        ),
        'story3': generate_relationship_story_template(
            template_data['story_points'][2], 
            template_data['keywords'],
            page_number=3
        ),
        'conclusion': generate_relationship_conclusion_template(
            {'conclusion': '愛情路上，理解與支持的界線在哪裡？'}, 
            template_data['keywords']
        ),
        'end': generate_relationship_end_template()
    }
    
    # Generate images from templates
    print("\n=== Generating Test Images ===")
    png_paths = await generate_images_from_templates(templates, "relationship_test")
    
    if png_paths:
        print(f"Successfully generated {len(png_paths)} images:")
        for path in png_paths:
            print(f"  - {path}")
    else:
        print("Failed to generate images")
    
    return templates, png_paths

if __name__ == "__main__":
    # Choose which function to run
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        # Run test mode
        asyncio.run(test_template_generation())
    else:
        # Run full content generation
        asyncio.run(generate_relationship_content()) 