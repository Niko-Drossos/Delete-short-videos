import sys
from moviepy.editor import VideoFileClip
import os

def delete_short_videos(directory_path, max_duration=180):
    deleted_count = 0

    for filename in os.listdir(directory_path):
        if filename.endswith(('.mp4', '.avi', '.mkv')):
            video_path = os.path.join(directory_path, filename)
            
            try:
                clip = VideoFileClip(video_path)
                duration = clip.duration
                clip.close()

                if duration < max_duration:
                    os.remove(video_path)
                    print(f"Deleted: {filename}")
                    deleted_count += 1
                else:
                    print(f"Kept: {filename}")
                    
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    print(f"\nTotal videos deleted: {deleted_count}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    video_directory = sys.argv[1]
    # max_duration = sys.argv[2]

    if not os.path.isdir(video_directory):
        print(f"Error: {video_directory} is not a valid directory.")
        sys.exit(1)

    

    delete_short_videos(video_directory)
