"""
This module implements a Flask-based web server that provides two primary services:

1. Serving a static HTML page: A simple web page is rendered and returned to the
                               user while accessing the root endpoint ("/")
2. Emotion Detection: Users can submit a text string, and the server will analyze
                      and return the dominant emotion and other emotion scores behind the input.

Endpoints:
    - "/": Returns the index.html page.
    - "/emotionDetector": Accepts a text string and returns the dominant emotion
                          and associates emotion scores.
    
Author: Karun Mathew
Version: 1.0.1
Date: September 10, 2024
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")
OUTPUT_FORMAT = "For the given statement, the system response is {}. The dominant emotion is {}."

@app.route("/")
def render_home_page():
    """
        Renders the home page of the application
        Returns:
            An HTML response
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def identify_emotion():
    """
        Analyzes the passed input text and responds with the dominant emotion and scores
        Returns:
            A response string that contains the emotion scores of the user inputed string
    """

    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    # construct the output response string
    # using list comprehension to extract the required keys
    entries = [ f"'{key}': '{value}'"
                for key, value in response.items()
                if key != "dominant_emotion" ]
    # join the list entries back to string with the appropriate delimiters
    emotion_scores = ' and '.join([', '.join(entries[:-1]), entries[-1]])
    return OUTPUT_FORMAT.format(emotion_scores, dominant_emotion)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
