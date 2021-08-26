#!/usr/bin/python3
import youtube_dl
import json

# Quick demo on the youtube_dl module
# Note this module is a downloader but this demo is using it as API to get data from 
# Youtube


class Youtube_data:
    def __init__(self):
        # initialize youtube_dl
        self.ydl = youtube_dl.YoutubeDL()
        self.query_video()
        self.print_data()
        self.save_to_json()



    def query_video(self):
        # the link below is Ginger by Wizkid, you can replace it with any other
        # Youtube link
        self.url  = 'https://www.youtube.com/watch?v=YSy2lBZ1QrA'

        # uses the youtube_dl as a context manager
        with self.ydl:
            # the download=False is to tell it not to download the video
            # remember the module is a downnloader but we're using it for its
            # API-like functions
            # so it just extracts the info we want
            self.result  =  self.ydl.extract_info(self.url, download=False)


    def save_to_json(self):
        # this function saves the output to a json file in the current directory
        # for easy viewing
        # NOTE: it overwrites the file result.json everytime it is run
        with open('result.json', 'w') as f:
            json_data  = json.dumps(self.result, indent=4)
            f.write(json_data)

    def print_data(self):
        # this function prints some important data we need about the Youtube
        # video
        # Title of the video
        video_title  =self.result['title']
        print(f"Video title is {video_title}\n")

        # video id for easy storage in database
        video_id  =self.result['id']
        print(f"Video id is {video_id}\n")

        # thumbnails that we can display for audio files
        thumbnails  =self.result['thumbnails']
        print(f"Video thumbnail links are  {thumbnails}\n")

        # duration of the video
        video_duration  =self.result['duration']
        print(f"Video duration is {video_duration}\n")

        # the artist name
        artist  =self.result['artist']
        print(f"Video artist is {artist}\n")



if __name__ == '__main__':
    # initializes the class
    yt = Youtube_data()

