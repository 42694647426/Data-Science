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




class TasksTest(unittest.TestCase):
    def setUp(self):
        dir = os.path.dirname(__file__)
        self.mock_dialog = os.path.join(dir, 'fixtures', 'mock_dialog.csv')
        self.true_word_counts = os.path.join(dir, 'fixtures', 'word_counts.true.json')
        self.true_tf_idfs = os.path.join(dir, 'fixtures', 'tf_idfs.true.json')
        self.output_word_counts = os.path.join(os.path.dirname(__file__), 'test_output.json')
    
    def task2_test(self):
        
        args = ['-c', self.true_word_counts, '-n', '10']
        
        with open(self.true_tf_idfs) as f:
            expected = json.load(f)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            src.compute_pony_lang.main(args)
            self.assertEqual(fake_out.getvalue(), expected)
        print("Task 2 Passed")
        
        
    def delete_tempfile(self):
        if os.path.isfile(self.output_word_counts):
            os.remove(self.output_word_counts)

    def task1_test(self):
        args = ['-o', self.output_word_counts, '-d', self.mock_dialog]
        src.compile_word_counts.main(args)
        with open(self.output_word_counts) as f:
            tested = json.load(f)
        with open(self.true_word_counts) as f:
            expected = json.load(f)
        self.assertEqual(expected, tested)
        print("Task 1 Passed")


    
if __name__ == '__main__':
    unittest.main()
