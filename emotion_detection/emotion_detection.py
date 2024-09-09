import requests
import json

# Constants
URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyse):
    # Validate the input
    # Input has to be a non-empty string
    if not isinstance(text_to_analyse, str):
        return "Please enter a valid string"
    elif text_to_analyse == "":
        return "Please enter a non-empty string"

    # Construct the payload for the POST request
    payload = { "raw_document": { "text": text_to_analyse } }

    # Add error handling for server requests
    try:
        response = requests.post(URL, json = payload, headers=HEADERS)
        json_response = json.loads(response.text)
        emotion_data = json_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion_data, key=emotion_data.get)
        emotion_data['dominant_emotion'] = dominant_emotion
    except:
        return "There has been an error in the server"
    else:
        # format the json response data with proper indentation
        return json.dumps(emotion_data, indent=4)