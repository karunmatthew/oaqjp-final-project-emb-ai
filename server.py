from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

OUTPUT_FORMAT_STRING = "For the given statement, the system response is {}. The dominant emotion is {}."

@app.route("/")
def render_home_page():
    return render_template("index.html")

@app.route("/emotionDetector")
def identify_emotion():
    try:
        text_to_analyze = request.args.get('textToAnalyze')
        response = emotion_detector(text_to_analyze)
        dominant_emotion = response['dominant_emotion']
        # construct the output response string
        # using list comprehension to extract the required keys
        entries = [f"'{key}': '{value}'" for key, value in response.items() if key != 'dominant_emotion']
        # join the list entries back to string with the appropriate delimiters
        emotion_scores = ' and '.join([', '.join(entries[:-1]), entries[-1]])
    except:
        return ""
    else:
        return OUTPUT_FORMAT_STRING.format(emotion_scores, dominant_emotion)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)