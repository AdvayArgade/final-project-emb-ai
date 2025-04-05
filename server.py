"""
Flask server to handle emotion detection requests.
"""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_api():
    """
    API endpoint to process a text input and return emotion analysis.

    Returns:
        JSON response with emotion scores and dominant emotion.
        If input is invalid, returns an error message.
    """
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({"error": "Missing 'text' field"}), 400

    text = data['text']
    result = emotion_detector(text)

    if result["dominant_emotion"] is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({"response": formatted_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
