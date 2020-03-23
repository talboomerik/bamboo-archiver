import os

from git import Repo

from config import bamboo_config as config


class BambooSpecSaver(object):

    def __init__(self, bamboo_fetcher):
        self.bamboo_fetcher = bamboo_fetcher

    def save_bamboo_specs(self, black_plan):
        java_content = self.bamboo_fetcher.get_bamboo_spec(black_plan)
        plan_position = self.create_position(black_plan)
        if not os.path.exists(plan_position):
            os.makedirs(plan_position)
        with open(plan_position+"/PlanSpec.java", "w") as java_file:
            java_file.write(java_content)
        return (java_content, plan_position)

    def create_position(self, black_plan):
        return "archive/" + black_plan.project_name + "/" + black_plan.name

    def add_bamboo_spec_to_git_repo(self, filepath, black_plan):
        repo = Repo(config.git_path)
        git = repo.git
        git.pull()
        if filepath not in repo.untracked_files:
            return
        git.add(filepath)
        git.commit(message="Adding {}".format(black_plan))
        git.push()
