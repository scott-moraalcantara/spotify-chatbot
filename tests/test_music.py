import unittest
from app.handlers.music import search_track

class TestMusic(unittest.TestCase):
    def test_search_track(self):
        track_uri = search_track("Shape of You")
        self.assertIsNotNone(track_uri)

if __name__ == "__main__":
    unittest.main()
