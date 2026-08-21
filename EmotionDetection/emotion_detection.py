"""
emotion_detection.py

Provides the emotion_detector function, which sends a piece of text to the
Watson NLP Emotion Predict function (Embeddable AI) and returns a formatted
dictionary of emotion scores plus the dominant emotion.
"""

import json
import requests


def emotion_detector(text_to_analyse):
    """
    Sends text_to_analyse to the Watson NLP EmotionPredict endpoint and
    returns a dictionary in the form:

        {
            'anger': <score>,
            'disgust': <score>,
            'fear': <score>,
            'joy': <score>,
            'sadness': <score>,
            'dominant_emotion': <label of the highest-scoring emotion>
        }

    If the input text is blank, the Watson NLP service responds with a
    400 status code. In that case every value in the returned dictionary
    is set to None, so callers (e.g. the Flask server) can detect and
    handle the error case explicitly.
    """
    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    input_json = {"raw_document": {"text": text_to_analyse}}
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    response = requests.post(url, json=input_json, headers=headers, timeout=10)

    # Task 7: blank/invalid input -> Watson NLP returns HTTP 400.
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    response_dict = json.loads(response.text)
    emotion_scores = response_dict['emotionPredictions'][0]['emotion']

    anger_score = emotion_scores['anger']
    disgust_score = emotion_scores['disgust']
    fear_score = emotion_scores['fear']
    joy_score = emotion_scores['joy']
    sadness_score = emotion_scores['sadness']

    emotions = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotions, key=emotions.get)

    formatted_response = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

    return formatted_response
