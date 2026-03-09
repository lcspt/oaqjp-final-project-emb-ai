
import requests # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):

    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, json = Input_json, headers=Headers)
    
    if response.status_code == 400:
        print(response.status_code)
        data = {'emotionPredictions': 
        [{'emotion': {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None}}]}
    else:
        data = response.json()
    
    print(data)

    emotions = data['emotionPredictions'][0]['emotion']
    ranked = sorted(emotions.items(), key=lambda x: x[1], reverse=True)

    sorted_emotions = dict(ranked)
    sorted_emotions['dominant_emotion'] = ranked[0][0]

    return sorted_emotions