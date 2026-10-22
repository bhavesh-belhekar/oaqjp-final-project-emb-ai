
import unittest
from unittest.mock import patch, Mock

from emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    @patch("emotion_detection.requests.post")
    def test_emotion_detector(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.85,
                        "disgust": 0.05,
                        "fear": 0.02,
                        "joy": 0.03,
                        "sadness": 0.05
                    }
                }
            ]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("I am really mad about this")

        self.assertEqual(result["anger"], 0.85)
        self.assertEqual(result["disgust"], 0.05)
        self.assertEqual(result["fear"], 0.02)
        self.assertEqual(result["joy"], 0.03)
        self.assertEqual(result["sadness"], 0.05)
        self.assertEqual(result["dominant_emotion"], "anger")

    @patch("emotion_detection.requests.post")
    def test_http_400(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 400
        mock_post.return_value = mock_response

        result = emotion_detector("")

        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
