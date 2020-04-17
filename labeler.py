import requests
from config import bamboo_config  as config

def fetch_latest_build_date(plan_key):
    url = config.base_url + '/rest/api/latest/result/' + plan_key + '/latest'
    r = requests.get(url, headers=headers, auth=config.auth)
    plan = r.json()
    buildCompletedDate = plan['buildCompletedDate']
    d = datetime.datetime.strptime( buildCompletedDate, "%Y-%m-%dT%H:%M:%S.%f%z" )
    return d.date()

def has_ever_run(plan_key):
    url = config.base_url + '/rest/api/latest/result/' + plan_key 
    r = requests.get(url, headers=headers, auth=config.auth)
    results = r.json()
    return results["results"]["size"] > 0

def get_latest_update_date_of_plan(plan_key):
    #scrape info from audit log: /chain/admin/config/viewChainAuditLog.action?buildKey=TEST-PLAN
    pass

def label_plans_black():
    #label all plans that have not been run in the last month and also not updated in the last month
    pass