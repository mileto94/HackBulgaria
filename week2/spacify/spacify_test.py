import spacify
import unittest

#from subprocess import call

class Testing(unittest.TestCase):
		
	def test_spacify(self):
		self.assertEqual('', spacify.read_and_write(sys.argv[1],sys.argv[2]))

	#def test_program_running(call):
	#	self.assertEqual(True, call("spacify.py"))

if __name__ == '__main__':
	unittest.main()