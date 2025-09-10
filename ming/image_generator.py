import asyncio
import os
from playwright.async_api import async_playwright

async def generate_images_from_templates(templates, person):
    """Generate PNG images from HTML templates using Playwright"""
    # Get the current script directory for saving PNGs
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Store all generated PNG paths
    png_paths = []
    
    # Define the mapping from template names to PNG file names
    template_to_png_name = {
        'title': 'title.png',
        'story1': 'content_page1.png',
        'story2': 'content_page2.png', 
        'story3': 'content_page3.png',
        'conclusion': 'conclusion.png',
        'end': 'end.png'
    }
    
    async with async_playwright() as p:
        # Launch browser with specific viewport size
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={'width': 1080, 'height': 1440},
            device_scale_factor=2  # Higher resolution
        )
        page = await context.new_page()
        
        # Set page timeout to 120 seconds
        page.set_default_timeout(120000)
        
        for template_name, html_content in templates.items():
            print(f"Generating {template_name} template...")
            
            try:
                # Set content with increased timeout and better error handling
                await page.set_content(html_content, timeout=120000)
                
                # Wait for DOM to be ready with shorter timeout
                try:
                    await page.wait_for_load_state('domcontentloaded', timeout=30000)
                except Exception as e:
                    print(f"Warning: DOM content loaded timeout for {template_name}, continuing anyway: {str(e)}")
                
                # Wait for network to be idle with shorter timeout
                try:
                    await page.wait_for_load_state('networkidle', timeout=30000)
                except Exception as e:
                    print(f"Warning: Network idle timeout for {template_name}, continuing anyway: {str(e)}")
                
                # Additional wait to ensure rendering
                await asyncio.sleep(3)

                # Get the post element
                post_element = await page.query_selector('#xiaohongshu-post')
                if post_element:
                    # Ensure element is visible
                    await post_element.scroll_into_view_if_needed()
                    
                    # Get the PNG file name from mapping, fallback to template_name if not found
                    png_filename = template_to_png_name.get(template_name, f"{template_name}.png")
                    png_path = os.path.join(current_dir, png_filename)
                    
                    await post_element.screenshot(
                        path=png_path,
                        omit_background=False  # Include background
                    )
                    print(f"Screenshot saved successfully to {png_path}")
                    png_paths.append(png_path)
                else:
                    print(f"Error: Could not find the element with ID 'xiaohongshu-post' for {template_name}")
                    # Take full page screenshot for debugging
                    await page.screenshot(
                        path=os.path.join(current_dir, f"debug_full_{template_name}.png")
                    )
            except Exception as e:
                print(f"Error generating {template_name} template: {str(e)}")
                print(f"Error details: {type(e).__name__}")
                
                # Try to take error screenshot
                try:
                    await page.screenshot(
                        path=os.path.join(current_dir, f"error_{template_name}.png")
                    )
                    print(f"Error screenshot saved as error_{template_name}.png")
                except Exception as screenshot_error:
                    print(f"Failed to save error screenshot: {str(screenshot_error)}")
                
                # Continue with next template instead of failing completely
                continue

        await browser.close()
    
    return png_paths 