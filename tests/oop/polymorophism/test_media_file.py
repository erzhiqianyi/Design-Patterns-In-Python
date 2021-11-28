import unittest

from oop.polymorophism.media_file import MP3File
from oop.polymorophism.media_file import OggFile
from oop.polymorophism.media_file import WaveFile


class MediaPlayTestCase(unittest.TestCase):

    def test_mp3_play_correct(self):
        mp3 = MP3File('test.mp3')
        mp3.play()

    def test_mp3_play_incorrect(self):
        mp3 = MP3File('test.wav')
        self.assertRaises(Exception, mp3.play)

    def test_wav_play_correct(self):
        wave = WaveFile('test.wav')
        wave.play()

    def test_wav_play_incorrect(self):
        wave = WaveFile('test.mp3')
        self.assertRaises(Exception, wave.play)

    def test_ogg_play_correct(self):
        ogg = OggFile('test.ogg')
        ogg.play()

    def test_ogg_play_incorrect(self):
        ogg = OggFile('test.mps')
        self.assertRaises(Exception, ogg.play)


if __name__ == '__main__':
    unittest.main()
