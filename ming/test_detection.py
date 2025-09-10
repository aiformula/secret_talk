#!/usr/bin/env python3

from custom_story_reader import read_custom_story

# Test the detection
data = read_custom_story('../my_custom_story.txt')
print('🎭 檢測結果:', data.get('perspective', 'unknown'))

if 'perspective_detection' in data:
    detection = data['perspective_detection']
    print('📁 檔案名檢測:', detection['filename'])
    print('📝 內容檢測:', detection['content'])
    print('✅ 最終選擇:', detection['final'])
else:
    print('❌ 沒有檢測信息')

print('\n📖 故事標題:', data.get('title', 'N/A')) 