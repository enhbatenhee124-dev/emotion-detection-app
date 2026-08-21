# Emotion Detection Web App

A web application that uses IBM Watson NLP's Embeddable AI Emotion Predict
function to detect the emotions (anger, disgust, fear, joy, sadness) expressed
in a piece of text, and reports the dominant emotion. Built with Flask and
packaged as a reusable Python module (EmotionDetection), with unit tests
and pylint-clean code.

## Project structure

- EmotionDetection/__init__.py
- EmotionDetection/emotion_detection.py
- templates/index.html
- static/mywebscript.js
- server.py
- test_emotion_detection.py
- requirements.txt
- README.md

## Running locally (inside the Skills Network Cloud IDE / IBM Cloud environment with Watson NLP access)

pip install -r requirements.txt
python3 server.py

Then open the app and enter text to analyze.

## Running the unit tests

python3 -m unittest test_emotion_detection.py
