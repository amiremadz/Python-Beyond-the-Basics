import myprogram
import pytest
import shutil
import os

class TestDoubleIt(object):
    
    file_template = 'testnums_template.txt'
    file_tester = 'testnums_tester.txt'
    
    @classmethod
    def setup_class(cls):
        shutil.copy(TestDoubleIt.file_template, TestDoubleIt.file_tester)

    @classmethod
    def teardown_class(cls):
        os.remove(TestDoubleIt.file_tester)

    def test_doublelines(self):
        myprogram.doublelines(TestDoubleIt.file_tester)
        
        old_vals = [int(item) for item in open(TestDoubleIt.file_template)]
        new_vals = [int(item) for item in open(TestDoubleIt.file_tester)]

        for old, new in zip(old_vals, new_vals):
            assert 2*old == new

    

    def test_doubleit_value(self):
        assert myprogram.doubleit(10) == 20

    def test_doubleit_type(self):
        #assert myprogram.doubleit('hi') raises TypeError
        with pytest.raises(TypeError):
            myprogram.doubleit('hi')
