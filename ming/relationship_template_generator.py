def format_text_with_comma_linebreaks(text):
    """Format text to put content after comma on new line and remove comma"""
    if '，' in text:
        # Split at comma and join with line break
        parts = text.split('，')
        return '<br>'.join(part.strip() for part in parts if part.strip())
    return text

def generate_exact_custom_template(content, template_type="content", perspective="female"):
    """Generate HTML template that preserves user's EXACT text with original beautiful design"""
    
    # Use the EXACT content without any processing except line breaks
    exact_content = content.replace('\n', '<br>')
    
    # Adjust font size based on content length for better fit
    content_length = len(content)
    if template_type == "content" and content_length > 50:
        font_size = "32px"  # Smaller font for longer content
    elif template_type == "content" and content_length > 40:
        font_size = "36px"  # Medium font for medium content
    elif template_type == "content" and content_length > 30:
        font_size = "40px"  # Larger font for shorter content
    
    # Choose styling based on template type with proper sizing for mobile display
    if template_type == "title":
        bg_image = "content_page1_girl.png" if perspective == "female" else "content_page1_boy.png"
        font_size = "52px"  # Reduced from 78px
        font_weight = "900"
        color = "#3f3257"
        content_class = "title"
        extra_style = """
            -webkit-text-stroke: 1px rgba(255,255,255,0.9);
            paint-order: stroke fill;
            filter: drop-shadow(0 0 8px rgba(255,255,255,0.7));
            text-align: center;
        """
    elif template_type == "conclusion":
        bg_image = "content_page1_girl.png" if perspective == "female" else "content_page1_boy.png"
        font_size = "36px"  # Reduced from 42px
        font_weight = "700"
        color = "#8B4B91"
        content_class = "question"
        extra_style = "text-align: center;"
    else:  # content pages
        bg_image = "content_page1_girl.png" if perspective == "female" else "content_page1_boy.png"
        if 'font_size' not in locals():  # Only set if not already set above
            font_size = "38px"  # Default font size for content pages
        font_weight = "500"
        color = "#3f3257"
        content_class = "story-content"
        extra_style = ""
    
    html_template = f"""
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Custom Story - Beautiful Design</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;900&display=swap');
            
            #xiaohongshu-post {{
                margin: 0;
                padding: 40px 20px 60px 20px;
                width: 1080px;
                height: 1350px;
                background: url('https://raw.githubusercontent.com/Liuhangfung/secret_talk/main/{bg_image}') center center/cover no-repeat;
                font-family: 'Noto Sans TC', sans-serif;
                display: flex;
                flex-direction: column;
                justify-content: flex-start;
                align-items: center;
                position: relative;
                box-sizing: border-box;
                overflow: hidden;
            }}
            
            .container {{
                width: 100%;
                max-width: 1000px;
                display: flex;
                justify-content: center;
                align-items: flex-start;
                z-index: 2;
                position: relative;
                padding: 20px 10px;
                box-sizing: border-box;
                margin-top: 80px;
            }}
            
            .{content_class} {{
                font-size: {font_size};
                color: {color};
                line-height: 1.5;
                font-weight: {font_weight};
                text-align: left;
                text-shadow: 2px 2px 4px rgba(255,255,255,0.9), -2px -2px 4px rgba(255,255,255,0.9);
                letter-spacing: 0.5px;
                {extra_style}
                word-wrap: break-word;
                overflow-wrap: break-word;
                hyphens: auto;
                max-width: 800px;
                width: 100%;
                padding: 25px;
                box-sizing: border-box;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 15px;
                backdrop-filter: blur(5px);
            }}
        </style>
    </head>
    <body>
        <div id="xiaohongshu-post">
            <div class="container">
                <div class="{content_class}">{exact_content}</div>
            </div>
        </div>
    </body>
    </html>
    """
    
    return html_template

def generate_short_relationship_content_template(content, keywords, perspective="female"):
    """Generate HTML template for short relationship content - concise and engaging"""
    
    # Highlight keywords in the content
    highlighted_content = content
    for keyword in keywords:
        if keyword in highlighted_content:
            highlighted_content = highlighted_content.replace(
                keyword,
                f'<span style="color: #ff6b6b; font-weight: 700;">{keyword}</span>'
            )
    
    # Choose background image based on perspective
    bg_image = "content_page1_girl.png" if perspective == "female" else "content_page1_boy.png"
    
    html_template = f"""
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Relationship Story Short Content</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;900&display=swap');
            
            #xiaohongshu-post {{
                margin: 0;
                padding: 0;
                width: 1080px;
                height: 1350px;
                background: url('https://raw.githubusercontent.com/Liuhangfung/secret_talk/main/{bg_image}') center center/cover no-repeat;
                font-family: 'Noto Sans TC', sans-serif;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                position: relative;
                padding: 40px;
                box-sizing: border-box;
            }}
            
            .container {{
                width: 95%;
                max-width: 1000px;
                text-align: center;
                z-index: 2;
                position: relative;
            }}
            
            .story-content {{
                font-size: 46px;
                color: #3f3257;
                line-height: 1.6;
                font-weight: 500;
                text-align: center;
                text-shadow: 2px 2px 4px rgba(255,255,255,0.9), -2px -2px 4px rgba(255,255,255,0.9);
                letter-spacing: 0.8px;
                margin-bottom: 30px;
            }}
            
            .question {{
                font-size: 42px;
                color: #8B4B91;
                font-weight: 700;
                text-align: center;
                margin-top: 20px;
                text-shadow: 2px 2px 4px rgba(255,255,255,0.9), -2px -2px 4px rgba(255,255,255,0.9);
            }}
        </style>
    </head>
    <body>
        <div id="xiaohongshu-post">
            <div class="container">
                <div class="story-content">{highlighted_content}</div>
            </div>
        </div>
    </body>
    </html>
    """
    
    return html_template

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
    
    # Choose background image based on perspective (use same as content pages)
    bg_image = "content_page1_girl.png" if perspective == "female" else "content_page1_boy.png"
    
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
                background: url('https://raw.githubusercontent.com/Liuhangfung/secret_talk/main/{bg_image}') center center/cover no-repeat;
                font-family: 'Noto Sans TC', sans-serif;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                position: relative;
                overflow: hidden;
                padding: 30px;
                box-sizing: border-box;
            }}
            
            /* 移除遮罩效果，與其他頁面保持一致 */
            
            .container {{
                width: 95%;
                max-width: 1000px;
                text-align: center;
                z-index: 2;
                position: relative;
            }}
            
            .title {{
                font-size: 78px;
                font-weight: 900;
                color: #3f3257;
                line-height: 1.1;
                margin-bottom: 50px;
                text-shadow: 2px 2px 4px rgba(255,255,255,0.9), -2px -2px 4px rgba(255,255,255,0.9);
                letter-spacing: 1px;
                /* 調整文字邊框效果 */
                -webkit-text-stroke: 1px rgba(255,255,255,0.9);
                paint-order: stroke fill;
            }}
            
            .subtitle {{
                font-size: 36px;
                color: #3f3257;
                font-weight: 700;
                margin-top: 40px;
                text-shadow: 2px 2px 4px rgba(255,255,255,0.9), -2px -2px 4px rgba(255,255,255,0.9);
                letter-spacing: 2px;
                /* 調整發光效果 */
                filter: drop-shadow(0 0 8px rgba(255,255,255,0.7));
            }}
            
            /* 移除動畫效果，與其他頁面保持一致 */
        </style>
    </head>
    <body>
        <div id="xiaohongshu-post">
            <div class="container">
                <div class="title">{highlighted_title}</div>
                <div class="subtitle">💕 感情煩惱分享 💕</div>
            </div>
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
                background: url('https://raw.githubusercontent.com/Liuhangfung/secret_talk/main/{bg_image}') center center/cover no-repeat;
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
                color: #3f3257;
                line-height: 1.5;
                font-weight: 500;
                text-align: left;
                text-shadow: 2px 2px 4px rgba(255,255,255,0.9), -2px -2px 4px rgba(255,255,255,0.9);
                letter-spacing: 0.5px;
            }}
        </style>
    </head>
    <body>
        <div id="xiaohongshu-post">
            <div class="container">
                <div class="story-content">{highlighted_description}</div>
            </div>
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
                background: url('https://raw.githubusercontent.com/Liuhangfung/secret_talk/main/{bg_image}') center center/cover no-repeat;
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
                color: #3f3257;
                line-height: 1.5;
                font-weight: 600;
                margin-bottom: 60px;
                text-shadow: 2px 2px 4px rgba(255,255,255,0.8), -2px -2px 4px rgba(255,255,255,0.8);
            }}
            
            .call-to-action {{
                font-size: 32px;
                color: #3f3257;
                font-weight: 500;
                margin-top: 40px;
                text-shadow: 1px 1px 2px rgba(255,255,255,0.8), -1px -1px 2px rgba(255,255,255,0.8);
            }}
        </style>
    </head>
    <body>
        <div id="xiaohongshu-post">
            <div class="container">
                <div class="conclusion-text">{highlighted_conclusion}</div>
                <div class="call-to-action">你哋會點做？留言分享下諗法啦 💭</div>
            </div>
        </div>
    </body>
    </html>
    """
    
    return html_template

def generate_relationship_end_template(perspective="female"):
    """Generate HTML template for relationship post ending slide"""
    
    # Choose background image based on perspective
    bg_image = "end_girl.png" if perspective == "female" else "end_boy.png"
    
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
                background: url('https://raw.githubusercontent.com/Liuhangfung/secret_talk/main/{bg_image}') center center/cover no-repeat;
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