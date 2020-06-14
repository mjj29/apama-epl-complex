from pysys.constants import *
from pysys.basetest import BaseTest
from apama.correlator import CorrelatorHelper
import os

class PySysTest(BaseTest):
	def execute(self):
		corr = CorrelatorHelper(self, name='correlator')
		corr.start(logfile='correlator.log')
		corr.injectEPL('../../../Complex.mon')
		for test in os.listdir(self.input):
			if test.endswith('.mon'):
				corr.injectEPL(test)
				corr.flush()
		corr.shutdown()

	def validate(self):
		self.assertGrep('correlator.log', expr=' ERROR ', contains=False)
