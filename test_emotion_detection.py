"""
test_emotion_detection.py

Unit tests for the emotion_detector function. Each test sends a statement
that is expected to trigger a specific dominant emotion and checks that
the function returns that emotion.
"""

import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Unit tests for the emotion_detector function."""

    def test_joy(self):
        """'I am glad this happened' should be dominantly joy."""
        result = emotion_detector('I am glad this happened')
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        """'I am really mad about this' should be dominantly anger."""
        result = emotion_detector('I am really mad about this')
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust(self):
        """'I feel disgusted just hearing about this' should be dominantly disgust."""
        result = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness(self):
        """'I am so sad about this' should be dominantly sadness."""
        result = emotion_detector('I am so sad about this')
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear(self):
        """'I am really afraid that this will happen' should be dominantly fear."""
        result = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()
