import requests
import json

# Constants
URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
ERROR_OUTPUT = {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion": None}

def emotion_detector(text_to_analyse):
    # Validate the input
    # Return an error if the input is not a string
    if not isinstance(text_to_analyse, str):
        return ERROR_OUTPUT

    # Construct the payload for the POST request
    payload = { "raw_document": { "text": text_to_analyse } }

    # Add error handling for server requests
    try:
        response = requests.post(URL, json = payload, headers=HEADERS)
        if response.status_code == 400:
            return ERROR_OUTPUT
        json_response = json.loads(response.text)
        emotion_data = json_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion_data, key=emotion_data.get)
        emotion_data['dominant_emotion'] = dominant_emotion
    except:
        return ERROR_OUTPUT
    else:
        return emotion_data