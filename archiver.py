from black_plan_fetcher import BlackPlanFetcher
from bamboo_query_service import BambooFetcher
from bamboo_spec_saver import BambooSpecSaver
from bamboo_deleter import BambooPlanDeleter

if __name__ == '__main__':
    fetcher = BambooFetcher()
    black_plan_ftcher = BlackPlanFetcher(fetcher)
    black_plans = black_plan_ftcher.fetch_black_plans()
    for plan in black_plans:
        print("Processing {}".format(plan))
        spec_saver = BambooSpecSaver()
        content, position = spec_saver.save_bamboo_specs(black_plan)
        spec_saver.add_bamboo_spec_to_git_repo(position, black_plan)
        deleter = BambooPlanDeleter()
        deleter.delete_plan(black_plan.key)
