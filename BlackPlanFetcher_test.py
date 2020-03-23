import unittest
from unittest.mock import Mock
from archiver import BlackPlanFetcher
from domain import Plan, BlackPlan
from bamboo_query_service import BambooFetcher

BLACK_PLAN_KEY = "plan key"
WHITE_PLAN_KEY = "WHITE_PLAN"

class BlackPlanFetcherTest(unittest.TestCase):

    def test_should_call_get_plan_keys_when_black_plans_fetched(self):
        bamboo_fetcher = self.a_mock_bamboo_fetcher()
       
        black_plan_fetcher = BlackPlanFetcher(bamboo_fetcher)
        black_plan_fetcher.fetch_black_plans()

        bamboo_fetcher.get_plan_keys.assert_called_once()

    def test_should_call_fetch_lables(self):

        bamboo_fetcher = self.a_mock_bamboo_fetcher()

        black_plan_fetcher = BlackPlanFetcher(bamboo_fetcher)
        black_plans = black_plan_fetcher.fetch_black_plans()

        self.assertTrue(bamboo_fetcher.fetch_labels.call_count == 2)

    def test_should_return_only_black_label_plan(self):

        bamboo_fetcher = self.a_mock_bamboo_fetcher()
        
        black_plan_fetcher = BlackPlanFetcher(bamboo_fetcher)
        black_plans = black_plan_fetcher.fetch_black_plans()

        self.assertTrue(len(black_plans) == 1)
        self.assertTrue(black_plans[0].key == BLACK_PLAN_KEY)
        self.assertTrue(type(black_plans[0]) == BlackPlan)

    def a_mock_plan_builder(self):
        plan_builder = Mock()
        plan_builder.build_plan_from_key.side_effect = [
            Plan(BLACK_PLAN_KEY, 'black'), Plan(WHITE_PLAN_KEY, 'white')]
        return plan_builder

    def a_mock_bamboo_fetcher(self):
        bamboo_fetcher = Mock()
        bamboo_fetcher.spec = BambooFetcher
        bamboo_fetcher.fetch_labels.side_effect = [['black'], ['white']]
        bamboo_fetcher.get_plan_keys.return_value = [BLACK_PLAN_KEY, WHITE_PLAN_KEY]
        bamboo_fetcher.fetch_plan_info.side_effect = [
            ("plan project name 1", "plan name 1"), ("plan project name 2", "plan name 2")]
        return bamboo_fetcher


if __name__ == '__main__':
    unittest.main()
