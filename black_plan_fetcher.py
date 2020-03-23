import datetime
import json
import requests

from concurrent.futures import ThreadPoolExecutor
from dateutil.parser import parse
from domain import BlackPlan, Plan


class BlackPlanFetcher(object):
    '''Component that fetches black labelled plans'''

    def __init__(self, bamboo_fetcher):
        self.bamboo_fetcher = bamboo_fetcher

    def fetch_black_plans(self):
        plan_keys = self.bamboo_fetcher.get_plan_keys()
        with ThreadPoolExecutor(max_workers=100) as executor:
            plan_structure_generator = executor.map(
                self.build_plan_from_key, plan_keys)
            black_plans = self.get_black_plans(list(plan_structure_generator))
            return black_plans

    def get_black_plans(self, plans):
        black_plans = self.filter_on_label(plans, "black")
        return self.decorate_with_info(black_plans)

    def decorate_with_info(self, black_plans):
        returnValue = []
        for black_plan in black_plans:
            project_name, plan_name = self.bamboo_fetcher.fetch_plan_info(
                black_plan.key)
            returnValue.append(
                BlackPlan(black_plan.key, project_name, plan_name))
        return returnValue

    def build_plan_from_key(self, plan_key):
        plan_lables = self.bamboo_fetcher.fetch_labels(plan_key)
        return Plan(plan_key, plan_lables)

    def filter_on_label(self, plans, label):
        return [plan for plan in plans if label in plan.labels]
