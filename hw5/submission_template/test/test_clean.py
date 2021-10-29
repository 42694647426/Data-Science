import unittest
from pathlib import Path
import os, sys
import json
import pytest
parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)


def load_json(filename):
    with open(filename, 'r') as f:
        for i in f:
            return json.loads(i)


class CleanTest(unittest.TestCase):

    def setUp(self):
        self.clean_file = os.path.join(parentdir, 'src/clean.py')
        self.test_1 = 'test/fixtures/test_1.json'
        self.test_2 = 'test/fixtures/test_2.json'
        self.test_3 = 'test/fixtures/test_3.json'
        self.test_4 = 'test/fixtures/test_4.json'
        self.test_5 = 'test/fixtures/test_5.json'
        self.test_6 = 'test/fixtures/test_6.json'
        
    def test_clean_file(self):
        print("\nRUNNING TESTS FOR HW5 - clean.py")
        print("Ensure txt file exists")
        self.assertEqual(os.path.isfile(self.clean_file), True)
        print("OK")
    
    def test_format(self):
        os.system(f'python src/clean.py -i {self.test_3} -o {self.test_3}')
        assert os.stat(self.test_3).st_size == 0
        print("Pass test 3!")
    
    def test_title(self):
        os.system(f'python src/clean.py -i {self.test_1} -o {self.test_1}')
        assert os.stat(self.test_1).st_size == 0
        print("Pass test 1!")
    
    def test_date(self):
        os.system(f'python src/clean.py -i {self.test_2} -o {self.test_2}')
        assert os.stat(self.test_2).st_size == 0
        print("Pass test 2!")
    
    
    def test_author(self):
        os.system(f'python src/clean.py -i {self.test_4} -o {self.test_4}')
        assert os.stat(self.test_4).st_size == 0
        print("Pass test 4!")
    
    def test_count(self):
        os.system(f'python src/clean.py -i {self.test_5} -o {self.test_5}')
        assert os.stat(self.test_5).st_size == 0
        print("Pass test 5!")
    
    def test_json(self):
        os.system(f'python src/clean.py -i {self.test_6} -o {self.test_6}')
        dict = load_json(self.test_6)
        assert (not " " in x for x in dict['tags'])
        print("Pass test 6!")
        
    
if __name__ == '__main__':
    unittest.main()