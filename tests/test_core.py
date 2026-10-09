import tempfile,unittest
from pathlib import Path
from mediashift import unique_output,command
class Tests(unittest.TestCase):
    def test_build_command(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);inp=p/"a.mp3";inp.write_bytes(b"hello")
            self.assertEqual(unique_output(inp,p,"mp3").name,"a (1).mp3")
            self.assertIn("-nostdin",command("ffmpeg",inp,p/"a.wav","wav"))
            with self.assertRaises(ValueError):command("ffmpeg",inp,inp,"mp3")
