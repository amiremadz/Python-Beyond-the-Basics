import pytest
from assignment6 import ConfigDict, ConfigKeyError
import shutil
import os

class TestConfigDict(object):
	file_template = 'file_template.txt'
	file_tester = 'file_tester.txt'
	file_new = 'file_new.txt'
	bad_path = os.path.join('./nonexistent','test.txt')

	@classmethod
	def setup_class(cls):
		shutil.copy(TestConfigDict.file_template, TestConfigDict.file_tester)


	@classmethod
	def teardown_class(cls):
		os.remove(TestConfigDict.file_tester)
		os.remove(TestConfigDict.file_new)


	def test_object_type(self):
		mydict = ConfigDict(TestConfigDict.file_tester)
		assert isinstance(mydict, dict) 
		assert isinstance(mydict, ConfigDict)

	def test_existing_filename(self):
		mydict = ConfigDict(TestConfigDict.file_tester)	
		assert mydict._filename == TestConfigDict.file_tester

	def test_new_file_exists(self):
		assert not os.path.isfile(TestConfigDict.file_new)
		mydict = ConfigDict(TestConfigDict.file_new)
		assert os.path.isfile(TestConfigDict.file_new)
	

	def test_bad_path(self):
		# Method 1
		#with pytest.raises(IOError):
		#	ConfigDict(TestConfigDict.bad_path)

		# Method 2
		try:
			mydict = ConfigDict(TestConfigDict.bad_path)
			assert False
		except IOError:
			assert True

	def test_read_nonexisting_key(self):
		mydict = ConfigDict(TestConfigDict.file_tester)
		try:
			print mydict['non-existent']
			assert False
		except ConfigKeyError:
			assert True

	def test_read_existing_keys(self):
		mydict = ConfigDict(TestConfigDict.file_tester)
		with open(TestConfigDict.file_tester) as fh:
			for line in fh:
				line = line.rstrip()
				key, val = line.split("=", 1)
				assert mydict[key] == val

	def test_write_key(self):
		mydict = ConfigDict(TestConfigDict.file_tester)
		mydict["han"] = "hen"
		assert mydict["han"] == "hen"
		with open(TestConfigDict.file_tester) as fh:
			for line in fh:
				line = line.rstrip()
				key, val = line.split('=', 1)
				if key == "han":
					assert True
					return
		assert False			


	def test_write_key_read(self):
		dict_1 = ConfigDict(TestConfigDict.file_tester)
		dict_1['new_key'] = 'new_val'
		dict_2 = ConfigDict(TestConfigDict.file_tester)
		assert dict_2['new_key'] == 'new_val'

	def test_preexisiting_file(self):
		dict_1 = ConfigDict(TestConfigDict.file_tester)
		assert os.path.isfile(TestConfigDict.file_tester)
		dict_2 = ConfigDict(TestConfigDict.file_tester)
		assert os.path.isfile(TestConfigDict.file_tester)
		assert set(dict_1.items()) == set(dict_2.items())
			

	