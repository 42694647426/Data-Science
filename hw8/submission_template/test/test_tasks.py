import unittest
from pathlib import Path
import os, sys
import json
from unittest.mock import patch
from io import StringIO
parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)
import src.compile_word_counts
import src.compute_pony_lang
import yaml

class TasksTest(unittest.TestCase):
    def setUp(self):
        dir = os.path.dirname(__file__)
        self.mock_dialog = os.path.join(dir, 'fixtures', 'mock_dialog.csv')
        self.true_word_counts = os.path.join(dir, 'fixtures', 'word_counts.true.json')
        self.true_tf_idfs = os.path.join(dir, 'fixtures', 'tf_idfs.true.json')
        self.output_word_counts = os.path.join(os.path.dirname(__file__), 'test_output.json')
    
    def test_task1(self):
        sys.argv = ["src/compile_word_counts.py",'-o', self.output_word_counts, '-d', self.mock_dialog]
        
        src.compile_word_counts.main()
        with open(self.output_word_counts) as f:
            tested = json.load(f)
        with open(self.true_word_counts) as f:
            expected = json.load(f)
        self.assertEqual(expected, tested)
        print("Task 1 Passed")
    

    def test_task2(self):
        sys.argv = ["src/compute_pony_lang.py",'-c', self.true_word_counts, '-n', '3']
        with open(self.true_tf_idfs) as f:
            expected = json.load(f)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            src.compute_pony_lang.main()
            tested = yaml.safe_load(fake_out.getvalue())
            
            self.assertEqual(tested, expected)
        print("Task 2 Passed")
        

 
         
    def delete_tempfile(self):
        if os.path.isfile(self.output_word_counts):
            os.remove(self.output_word_counts)


    
if __name__ == '__main__':
    unittest.main(TasksTest)
