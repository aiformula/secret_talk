def format_text_with_comma_linebreaks(text):
    """Format text to put content after comma on new line and remove comma"""
    if '，' in text:
        # Split at comma and join with line break
        parts = text.split('，')
        return '<br>'.join(part.strip() for part in parts if part.strip())
    return text

def generate_relationship_title_template(title_content, keywords, perspective="female"):
    """Generate HTML template for relationship post title slide"""
    
    # Format title with comma line breaks
    formatted_title = format_text_with_comma_linebreaks(title_content['title'])
    
    # Highlight keywords in the title
    highlighted_title = formatted_title
    for keyword in keywords:
        if keyword in highlighted_title:
            highlighted_title = highlighted_title.replace(
                keyword, 
                f'<span style="color: #ff6b6b; font-weight: 700;">{keyword}</span>'
            )
    
    # Choose background image based on perspective - use local fallback
    bg_image = "title_girl.png" if perspective == "female" else "title_boy.png"
    # Fallback to solid color if image not available
    bg_style = f"background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);"
    
    html_template = f"""
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Relationship Story Title</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;900&display=swap');
            
            #xiaohongshu-post {{
                margin: 0;
                padding: 0;
                width: 1080px;
                height: 1350px;
                {bg_style}
                font-family: 'Noto Sans TC', sans-serif;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                position: relative;
                overflow: hidden;
            }}
            
            .container {{
                width: 90%;
                max-width: 900px;
                text-align: center;
                z-index: 2;
                position: relative;
            }}
            
            .title {{
                font-size: 72px;
                font-weight: 900;
                color: #2c3e50;
                line-height: 1.2;
                margin-bottom: 40px;
                text-shadow: 3px 3px 6px rgba(0,0,0,0.1), -3px -3px 6px rgba(255,255,255,0.9);
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                padding: 20px;
                border-radius: 15px;
                box-shadow: 0 8px 32px rgba(0,0,0,0.1);
            }}
            
            .subtitle {{
                font-size: 32px;
                color: #34495e;
                font-weight: 600;
                margin-top: 30px;
                text-shadow: 2px 2px 4px rgba(255,255,255,0.9), -2px -2px 4px rgba(255,255,255,0.9);
                background: rgba(255,255,255,0.9);
                padding: 10px 20px;
                border-radius: 25px;
                box-shadow: 0 4px 16px rgba(0,0,0,0.1);
            }}
        </style>
    </head>
    <body>
        <div id="xiaohongshu-post">
            <div class="container">
                <div class="title">{highlighted_title}</div>
                <div class="subtitle">感情煩惱分享 💭</div>
            </div>
            <!-- Decorative elements -->
            <div style="position: absolute; top: 50px; left: 50px; width: 100px; height: 100px; background: linear-gradient(45deg, #667eea, #764ba2); border-radius: 50%; opacity: 0.3;"></div>
            <div style="position: absolute; bottom: 100px; right: 80px; width: 80px; height: 80px; background: linear-gradient(45deg, #f093fb, #f5576c); border-radius: 50%; opacity: 0.3;"></div>
        </div>
    </body>
    </html>
    """
    
    return html_template

def generate_relationship_story_template(story_point, keywords, page_number=1, perspective="female"):
    """Generate HTML template for relationship story content slide"""
    
    # Highlight keywords in the description
    highlighted_description = story_point['description']
    for keyword in keywords:
        if keyword in highlighted_description:
            highlighted_description = highlighted_description.replace(
                keyword,
                f'<span style="color: #ff6b6b; font-weight: 700;">{keyword}</span>'
            )
    
    # Use different background images for different story pages based on perspective
    if perspective == "female":
        bg_images = {
            1: 'content_page1_girl.png',
            2: 'content_page2_girl.png', 
            3: 'content_page3_girl.png'
        }
    else:  # male perspective
        bg_images = {
            1: 'content_page1_boy.png',
            2: 'content_page2_boy.png', 
            3: 'content_page3_boy.png'
        }
    
    bg_image = bg_images.get(page_number, bg_images[1])
    # Fallback to solid color if image not available
    bg_style = f"background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);"
    
    html_template = f"""
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Relationship Story Content</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;900&display=swap');
            
            #xiaohongshu-post {{
                margin: 0;
                padding: 0;
                width: 1080px;
                height: 1350px;
                {bg_style}
                font-family: 'Noto Sans TC', sans-serif;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                position: relative;
                padding: 30px;
                box-sizing: border-box;
            }}
            
            .container {{
                width: 95%;
                max-width: 1000px;
                text-align: left;
                z-index: 2;
                position: relative;
            }}
            
            .story-content {{
                font-size: 40px;
                color: #2c3e50;
                line-height: 1.6;
                font-weight: 500;
                text-align: left;
                text-shadow: 2px 2px 4px rgba(255,255,255,0.95), -2px -2px 4px rgba(255,255,255,0.95);
                letter-spacing: 0.5px;
                background: rgba(255,255,255,0.9);
                padding: 30px;
                border-radius: 20px;
                box-shadow: 0 8px 32px rgba(0,0,0,0.1);
                backdrop-filter: blur(10px);
            }}
        </style>
    </head>
    <body>
        <div id="xiaohongshu-post">
            <div class="container">
                <div class="story-content">{highlighted_description}</div>
            </div>
            <!-- Decorative elements -->
            <div style="position: absolute; top: 30px; right: 40px; width: 60px; height: 60px; background: linear-gradient(45deg, #667eea, #764ba2); border-radius: 50%; opacity: 0.2;"></div>
            <div style="position: absolute; bottom: 50px; left: 60px; width: 40px; height: 40px; background: linear-gradient(45deg, #f093fb, #f5576c); border-radius: 50%; opacity: 0.2;"></div>
        </div>
    </body>
    </html>
    """
    
    return html_template

def generate_relationship_conclusion_template(conclusion_content, keywords, perspective="female"):
    """Generate HTML template for relationship post conclusion slide"""
    
    # Highlight keywords in the conclusion
    highlighted_conclusion = conclusion_content['conclusion']
    for keyword in keywords:
        if keyword in highlighted_conclusion:
            highlighted_conclusion = highlighted_conclusion.replace(
                keyword,
                f'<span style="color: #ff6b6b; font-weight: 700;">{keyword}</span>'
            )
    
    # Choose background image based on perspective
    bg_image = "content_page3_girl.png" if perspective == "female" else "content_page3_boy.png"
    # Fallback to solid color if image not available
    bg_style = f"background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);"
    
    html_template = f"""
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Relationship Story Conclusion</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;900&display=swap');
            
            #xiaohongshu-post {{
                margin: 0;
                padding: 0;
                width: 1080px;
                height: 1350px;
                {bg_style}
                font-family: 'Noto Sans TC', sans-serif;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                position: relative;
                padding: 80px 40px;
                box-sizing: border-box;
            }}
            
            .container {{
                width: 90%;
                max-width: 900px;
                text-align: center;
                z-index: 2;
                position: relative;
            }}
            
            .conclusion-text {{
                font-size: 40px;
                color: #2c3e50;
                line-height: 1.5;
                font-weight: 600;
                margin-bottom: 60px;
                text-shadow: 2px 2px 4px rgba(255,255,255,0.9), -2px -2px 4px rgba(255,255,255,0.9);
                background: rgba(255,255,255,0.9);
                padding: 30px;
                border-radius: 20px;
                box-shadow: 0 8px 32px rgba(0,0,0,0.1);
                backdrop-filter: blur(10px);
            }}
            
            .call-to-action {{
                font-size: 32px;
                color: #34495e;
                font-weight: 500;
                margin-top: 40px;
                text-shadow: 1px 1px 2px rgba(255,255,255,0.9), -1px -1px 2px rgba(255,255,255,0.9);
                background: rgba(255,255,255,0.9);
                padding: 15px 25px;
                border-radius: 25px;
                box-shadow: 0 4px 16px rgba(0,0,0,0.1);
            }}
        </style>
    </head>
    <body>
        <div id="xiaohongshu-post">
            <div class="container">
                <div class="conclusion-text">{highlighted_conclusion}</div>
                <div class="call-to-action">你哋會點做？留言分享下諗法啦 💭</div>
            </div>
            <!-- Decorative elements -->
            <div style="position: absolute; top: 40px; left: 40px; width: 70px; height: 70px; background: linear-gradient(45deg, #667eea, #764ba2); border-radius: 50%; opacity: 0.2;"></div>
            <div style="position: absolute; bottom: 80px; right: 60px; width: 50px; height: 50px; background: linear-gradient(45deg, #f093fb, #f5576c); border-radius: 50%; opacity: 0.2;"></div>
        </div>
    </body>
    </html>
    """
    
    return html_template

def generate_relationship_end_template(perspective="female"):
    """Generate HTML template for relationship post ending slide"""
    
    # Choose background image based on perspective
    bg_image = "end_girl.png" if perspective == "female" else "end_boy.png"
    # Fallback to solid color if image not available
    bg_style = f"background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);"
    
    html_template = f"""
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Relationship Story End</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;900&display=swap');
            
            #xiaohongshu-post {{
                margin: 0;
                padding: 0;
                width: 1080px;
                height: 1350px;
                {bg_style}
                font-family: 'Noto Sans TC', sans-serif;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                position: relative;
            }}
        </style>
    </head>
    <body>
        <div id="xiaohongshu-post">
        </div>
    </body>
    </html>
    """
    
    return html_template 