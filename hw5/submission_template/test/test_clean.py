import unittest
from pathlib import Path
import os, sys
import json
import tempfile
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
        
    def test_0(self):
        print("\nRUNNING TESTS FOR HW5 - clean.py")
        print("Ensure txt file exists")
        self.assertEqual(os.path.isfile(self.clean_file), True)
        print("OK")
    
    def test_3(self):
        temp =  tempfile.NamedTemporaryFile(delete=False)
        os.system(f'python src/clean.py -i {self.test_3} -o {temp.name}')
        assert os.stat(temp.name).st_size == 0
        print("Pass test 3!")
        temp.close()
        
    
    def test_1(self):
        temp =  tempfile.NamedTemporaryFile(delete=False)
        os.system(f'python src/clean.py -i {self.test_1} -o {temp.name}')
        assert os.stat(temp.name).st_size == 0
        print("Pass test 1!")
        temp.close()
        
    def test_4(self):
        temp =  tempfile.NamedTemporaryFile(delete=False)
        os.system(f'python src/clean.py -i {self.test_4} -o {temp.name}')
        assert os.stat(temp.name).st_size == 0
        print("Pass test 4!")
        temp.close()

    def test_2(self):
        temp =  tempfile.NamedTemporaryFile(delete=False)
        os.system(f'python src/clean.py -i {self.test_2} -o {temp.name}')
        assert os.stat(temp.name).st_size == 0
        print("Pass test 2!")
        temp.close()
    
    
    def test_5(self):
        temp =  tempfile.NamedTemporaryFile(delete=False)
        os.system(f'python src/clean.py -i {self.test_5} -o {temp.name}')
        assert os.stat(temp.name).st_size == 0
        print("Pass test 5!")
        temp.close()
    
    def test_6(self):
        temp =  tempfile.NamedTemporaryFile(delete=False)
        os.system(f'python src/clean.py -i {self.test_6} -o {temp.name}')
        dict = load_json(temp.name)
        assert (not " " in x for x in dict['tags'])
        print("Pass test 6!")
        temp.close()
        
    
if __name__ == '__main__':
    unittest.main()