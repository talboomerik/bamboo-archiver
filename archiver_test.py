import unittest
import json
import codecs

from archiver import BlackPlanFetcher
from domain import BlackPlan
from bamboo_query_service import BambooFetcher
from bamboo_deleter import BambooPlanDeleter
from bamboo_spec_saver import BambooSpecSaver

BLACK_PLAN_KEY = "plan key"
BLACK_PLAN_PROJECT = "project"
BLACK_PLAN_NAME = "plan name"

class ArchiverTest(unittest.TestCase):

    def test_fixture_for_fetching_all_black_label_plans(self):
        fetcher = BambooFetcher()
        black_plan_ftcher = BlackPlanFetcher(fetcher)
        black_plans = black_plan_ftcher.fetch_black_plans()

        print(black_plans)

        for plan in black_plans:
            self.assertIsInstance(plan, BlackPlan)
            self.assertTrue(len(plan.project_name) > 0)
            self.assertIsNotNone(plan.name)

    def test_fixture_for_fetching_the_bamboo_specs_for_a_plan(self):
        fetcher = BambooFetcher()
        black_plan = BlackPlan(BLACK_PLAN_KEY, BLACK_PLAN_PROJECT, BLACK_PLAN_NAME)
        saver = BambooSpecSaver(fetcher)
        bamboo_spec = saver.save_bamboo_specs(black_plan)
        print(bamboo_spec)
        self.assertTrue(len(bamboo_spec) > 0)

    def test_fixture_for_delete_a_plan(self):
        fetcher = BambooFetcher()
        black_plan_key = BLACK_PLAN_KEY
        deleter = BambooPlanDeleter()
        key = deleter.delete_plan(black_plan_key)

    def test_add_plan_to_repo(self):
        fetcher = BambooFetcher()
        black_plan = BlackPlan(BLACK_PLAN_KEY, BLACK_PLAN_PROJECT, BLACK_PLAN_NAME)
        file_path = "archive/" + BLACK_PLAN_PROJECT + "/" + BLACK_PLAN_NAME + "/PlanSpec.java"
        saver = BambooSpecSaver(fetcher)
        saver.add_bamboo_spec_to_git_repo(file_path, black_plan)


if __name__ == '__main__':
    unittest.main()
