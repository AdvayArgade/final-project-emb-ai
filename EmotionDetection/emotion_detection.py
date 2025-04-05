import requests

def emotion_detector(text):
    if not text.strip():  # Check if input is blank or only whitespace
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    response = requests.post("https://some-emotion-api.com/detect", json={"text": text})

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    data = response.json()

    emotions = {
        'anger': data.get('anger', 0),
        'disgust': data.get('disgust', 0),
        'fear': data.get('fear', 0),
        'joy': data.get('joy', 0),
        'sadness': data.get('sadness', 0),
    }

    emotions['dominant_emotion'] = max(emotions, key=emotions.get) if any(emotions.values()) else None

    return emotions
