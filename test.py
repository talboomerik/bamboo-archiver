import unittest
from BlackPlanFetcher_test import BlackPlanFetcherTest
from archiver_test import ArchiverTest
from BambooSpecSaver_test import BambooSpecSaverTest

def suite():
    """
        Gather all the tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(BlackPlanFetcherTest))
    test_suite.addTest(unittest.makeSuite(ArchiverTest))
    test_suite.addTest(unittest.makeSuite(BambooSpecSaverTest))
    return test_suite


if __name__ == '__main__':
    mySuit=suite()
    runner=unittest.TextTestRunner()
    runner.run(mySuit)