import yt_dlp
import time
import requests
import os

def is_network_stable():
    """Check if the network is stable by pinging a reliable server."""
    try:
        response = requests.get("https://www.google.com", timeout=5)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

def get_available_formats(video_url):
    """Fetch available formats for the given video URL."""
    with yt_dlp.YoutubeDL() as ydl:
        info_dict = ydl.extract_info(video_url, download=False)  # Get info without downloading
        formats = info_dict.get('formats', [])
        return formats

def download_video(video_url, download_dir, format_choice):
    """Download the video with retry logic for network issues."""
    ydl_opts = {
        'format': format_choice,  # Download the specified format
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),  # Save file with the title of the video
        'socket_timeout': 30,  # Increase socket timeout
        'noprogress': False,  # Show download progress
        'continue_dl': True,  # Enable resume download
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        while True:
            try:
                print("Starting download...")
                ydl.download([video_url])
                break  # Exit loop if download is successful
            except Exception as e:
                print(f"An error occurred: {e}")
                print("Waiting for network to stabilize...")
                while not is_network_stable():
                    print("Network is unstable. Waiting for 2 minutes before checking again...")
                    time.sleep(120)  # Wait for 2 minutes before checking the network status again
                print("Network is stable. Retrying download...")

if __name__ == "__main__":
    while True:
        video_url = input("Enter the video URL of your choice: ")  # Prompt for the video URL
        if video_url.strip():  # Check if the input is not empty
            download_dir = input("Enter the directory to save the video (leave blank for current directory): ")
            if not download_dir.strip():
                download_dir = os.getcwd()  # Use current directory if no input is given
            
            # Fetch available formats
            formats = get_available_formats(video_url)
            if not formats:
                print("No formats available for this video.")
                continue
            
            # Display available formats
            print("Available formats:")
            for i, fmt in enumerate(formats):
                format_id = fmt.get('format_id', 'N/A')
                format_desc = fmt.get('format_note', 'N/A')
                print(f"{i + 1}: {format_id} - {format_desc}")

            # Prompt user to select a format
            while True:
                try:
                    format_choice_index = int(input("Select a format by number: ")) - 1
                    if 0 <= format_choice_index < len(formats):
                        format_choice = formats[format_choice_index]['format_id']
                        break
                    else:
                        print("Invalid selection. Please try again.")
                except ValueError:
                    print("Please enter a valid number.")

            print("Checking network stability...")
            while not is_network_stable():
                print("Network is unstable. Waiting for 2 minutes before checking again...")
                time.sleep(120)  # Wait for 2 minutes before checking the network status again
            
            print("Network is stable. Starting download...")
            download_video(video_url, download_dir, format_choice)
            break  # Exit the loop after successful download
        else:
            print("Please enter a valid video URL.")  # Prompt for valid input
