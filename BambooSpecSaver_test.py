import unittest
import os
import shutil

from domain import BlackPlan
from bamboo_query_service import BambooFetcher
from bamboo_spec_saver import BambooSpecSaver
from unittest.mock import Mock


class BambooSpecSaverTest(unittest.TestCase):
    def test_should_call_the_fetcher_when_build_plan_from_key(self):
        fetcher = self.a_mock_bamboo_fetcher()
        black_plan = BlackPlan("TEST", "TEST_PROJECT", "TEST_NAME")
        saver = BambooSpecSaver(fetcher)
        content, position = saver.save_bamboo_specs(black_plan)
        fetcher.get_bamboo_spec.assert_called()
        self.assertTrue(content.strip() == "JAVACONTENT")
        test_file_path = "archive/TEST_PROJECT/TEST_NAME/PlanSpec.java"
        self.assertTrue(os.path.exists(test_file_path))
        shutil.rmtree("archive/TEST_PROJECT")

    def a_mock_bamboo_fetcher(self):
        bamboo_fetcher = Mock()
        bamboo_fetcher.spec = BambooFetcher
        bamboo_fetcher.get_bamboo_spec.return_value = """
            JAVACONTENT
        """
        return bamboo_fetcher


if __name__ == '__main__':
    unittest.main()
