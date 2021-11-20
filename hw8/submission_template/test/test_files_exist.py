import unittest
from pathlib import Path
import os, sys

parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)


class FilesExistTest(unittest.TestCase):
    def setUp(self):
        self.word_count_pyfile = os.path.join(parentdir, 'src', 'compile_word_counts.py')
        self.pony_lang_file = os.path.join(parentdir, 'src', 'compute_pony_lang.py')
        self.unit_test_file = os.path.join(parentdir, 'test', 'test_tasks.py')
        self.word_count_json = os.path.join(parentdir, 'word_counts.json')
    
    def test_unit_test(self):
        print(f"Test test_tasks.py file")
        assert os.path.isfile(self.unit_test_file)
        print("Passed")
    
    def test_data(self):    
        print(f"Test required data files")
        assert os.path.isfile(self.word_count_json)
        print("Passed")

    def pony_lang_test(self):
        print(f"Test compute_pony_lang.py file")
        assert os.path.isfile(self.pony_lang_file)
        print("Passed")
    
    

    def word_count_test(self):
        print(f"Test compile_word_counts.py file")
        assert os.path.isfile(self.word_count_pyfile)
        print("Passed")
    


    
if __name__ == '__main__':
    unittest.main()