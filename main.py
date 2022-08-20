import unittest
from HTMLTestRunner import HTMLTestRunner
from TestSuite.test_Add_to_Cart_Dress_and_Lipstick import *
import os

# get the directory path to output report file
dir = os.getcwd()


testsuite = unittest.TestLoader().discover('.')
# open the report file
outfile = open(dir + "\SeleniumPythonTestSummary.html", "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='Test report', report_name='report',
                            open_in_browser=True, description="HTMLTestReport")
runner.run(testsuite)

