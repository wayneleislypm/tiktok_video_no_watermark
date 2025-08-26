import requests

def download_tiktokvideo_no_watermark():
    url = input("Enter the TikTok video URL: ")
    api_url = f"https://www.tikwm.com/api/?url={url}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        # TikWM puts the video link inside data['data']['play']
        if "data" in data and "play" in data["data"]:
            video_url = data["data"]["play"]
            video_response = requests.get(video_url)
            video_response.raise_for_status()  # important (previously you did this on .content)

            with open("tiktok_video_no_watermark.mp4", "wb") as file:
                file.write(video_response.content)

            print("✅ Video downloaded successfully as 'tiktok_video_no_watermark.mp4'")
        else:
            print("❌ Could not find video URL in the response. API response:", data)

    except Exception as e:
        print(f"⚠️ An error occurred: {e}")

if __name__ == "__main__":
    download_tiktokvideo_no_watermark()
