# news_video.py
import requests
import base64
import time

class VideoGenerator:
    def __init__(self, api_key: str):
        if not api_key:
            raise Exception("API key is missing. Please check your .env and streamlit_app.py setup.")

        # Encode key into Base64 for D-ID API
        self.auth_str = base64.b64encode(api_key.encode("utf-8")).decode("utf-8")

    def generate_video(self, input_text: str, source_url: str, voice_id: str = "en-US-JennyNeural") -> str:
        """
        Generate a video using the D-ID API.
        Args:
            input_text (str): The script the avatar should speak.
            source_url (str): The image URL for the avatar face.
            voice_id (str): The voice to use (default: en-US-JennyNeural).
        Returns:
            str: URL to the generated video.
        """
        url = "https://api.d-id.com/talks"
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Basic {self.auth_str}"
        }

        payload = {
            "script": {
                "type": "text",
                "input": input_text,
                "subtitles": False,
                "provider": {
                    "type": "microsoft",
                    "voice_id": voice_id
                }
            },
            "source_url": source_url
        }

        # Step 1: Create video job
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=60)
            response.raise_for_status()
            job = response.json()
        except requests.RequestException as e:
            raise Exception(f"Request error while creating video: {str(e)}")
        except Exception:
            raise Exception(f"Video creation failed. Raw response: {response.text}")

        print("Create response:", job)

        if "id" not in job:
            # Show D-ID error message if available
            raise Exception(f"Video generation failed: {job.get('message', job)}")

        talk_id = job["id"]

        # Step 2: Poll until job is done
        talk_url = f"{url}/{talk_id}"
        for _ in range(30):  # max ~150 seconds
            try:
                resp = requests.get(talk_url, headers=headers, timeout=30)
                status = resp.json()
            except requests.RequestException as e:
                raise Exception(f"Request error while polling: {str(e)}")
            except Exception:
                raise Exception(f"Polling failed. Raw response: {resp.text}")

            print("Poll response:", status)

            if status.get("status") == "done":
                return status["result_url"]

            if status.get("status") == "error":
                raise Exception(f"Video failed: {status}")

            time.sleep(5)  # wait 5s before next poll

        raise Exception("Video generation timed out after 150 seconds")









