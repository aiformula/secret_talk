#!/usr/bin/env python3

from custom_story_reader import read_custom_story
from relationship_template_generator import generate_exact_custom_template

# Read the story
story = read_custom_story('my_custom_story.txt')
print('First content part:')
print(repr(story['content_parts'][0]))
print()

# Generate template for first part
template = generate_exact_custom_template(story['content_parts'][0], 'content', 'female')

# Save template to file for inspection
with open('debug_template.html', 'w', encoding='utf-8') as f:
    f.write(template)

print('Template saved to debug_template.html')

# Find the content between the div tags
import re
content_match = re.search(r'<div class="story-content">(.*?)</div>', template, re.DOTALL)
if content_match:
    print('Generated HTML content:')
    print(repr(content_match.group(1)))
else:
    print('Could not find content div')
