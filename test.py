import youtube_dl
import sys
import json
import pprint


ydl = youtube_dl.YoutubeDL()
# ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

with ydl:
    result = ydl.extract_info(
        'https://www.youtube.com/watch?v=YSy2lBZ1QrA',
        # 'https://www.youtube.com/watch?v=JD-age0BPVo&list=PLzMcBGfZo4-kCLWnGmK0jUBmGLaJxvi4j',
        download=False # We just want to extract the info
    )
# the line below is pretty the python dict in a nice format, uncomment if you
# want
# pprint.pprint(result)



# the line saves the result in a json file in the current directory
with open('result.json', 'w') as f:
    json_data  = json.dumps(result, indent=4)
    f.write(json_data)
sys.exit()
if 'entries' in result:
    # Can be a playlist or a list of videos
    video = result['entries'][0]
else:
    # Just a video
    video = result

print(video.keys())
# video_url = video['webpage_url']
title = video['title']
duration = video['duration']
# print(video_url)
print(title, duration)



