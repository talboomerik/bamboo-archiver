import requests
from config import bamboo_config as config
from lxml import html

headers = {'Accept': 'application/json'}


class BambooFetcher(object):
    '''compontent that fetcher all the plans from bamboo'''

    def fetch_labels(self, plan_key):
        '''return the lables in a plan by its key'''
        url = config.base_url + '/rest/api/latest/plan/' + plan_key + '/label'
        r = requests.get(url, headers=headers, auth=config.auth, verify=False)
        plan = r.json()
        lables = [internal_lables['name']
                  for internal_lables in plan['labels']['label']]
        return lables

    def get_plan_keys(self):
        return self.extract_keys(self.fetch_plans_as_map())

    def fetch_plans_as_map(self):
        url = config.base_url + '/rest/api/latest/plan.json?max-results=1500'
        r = requests.get(url, headers=headers, auth=config.auth, verify=False)
        return r.json()

    def extract_keys(self, fetched_plans):
        keys = [plan['key'] for plan in fetched_plans['plans']['plan']]
        return keys

    def fetch_plan_info(self, plan_key):
        '''return the project name in a plan by its key'''
        url = config.base_url + '/rest/api/latest/plan/' + plan_key
        r = requests.get(url, headers=headers, auth=config.auth, verify=False)
        plan = r.json()
        project_name = plan['projectName']
        name = plan['shortName']
        return (project_name, name)

    def get_bamboo_spec(self, black_plan):
        bamboo_spec_page_content = self.get_bamboo_spec_page_content(
            black_plan)
        java_content = self.extract_java_content(bamboo_spec_page_content)
        return java_content

    def get_bamboo_spec_page_content(self, black_plan):
        url = config.base_url + '/exportSpecs/plan.action?buildKey=' + black_plan.key
        r = requests.get(url, auth=config.auth, verify=False)
        return r.content

    def extract_java_content(self, bamboo_spec_page_content):
        tree = html.fromstring(bamboo_spec_page_content)
        content = tree.xpath('//div[@id="fieldArea_exportItem"]/textarea')
        java_content = content[0].text
        return java_content
