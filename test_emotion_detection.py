from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotoin_detector(self):
        test_cases=[('I am glad this happened','joy'),
        ('I am really mad about this','anger'),
        ('I feel disgusted just hearing about this','disgust'),
        ('I am so sad about this','sadness'),
        ('I am really afraid that this will happen','fear')]
        
        for case in test_cases:
            result= emotion_detector(case[0])
            self.assertEqual(result['dominant_emotion'], case[1])

unittest.main()