import requests
from config import bamboo_config as config
from lxml import html


class BambooPlanDeleter(object):

    def delete_plan(self, plan_key):
        with requests.Session() as session:
            r = session.get(config.base_url, verify=False)
            print("Cookies: " + str(session.cookies))
            session_cookie = session.cookies.get("atl.xsrf.token")
            print("Session cookie is " + session_cookie)
            login_params = {
                "os_destination":
                "/start.action",
                "os_username": config.auth[0],
                "os_password": config.auth[1],
                "checkBoxFields": "os_cookie",
                "save": "Log+in",
                "atl_token": session_cookie
            }
            r = session.post(
                "https://" + config.base_url + "/userlogin.action", data=login_params, verify=False)
            print("Login status code: {}".format(r.status_code))
            r = session.get(
                config.base_url + '/ajax/confirmDeleteChain.action?buildKey=' + plan_key, verify=False)
            print("Cookies: " + str(session.cookies))
            tree = html.fromstring(r.content)
            token = tree.xpath('//input[@name="atl_token"]/@value')[0]
            build_key = tree.xpath('//input[@name="buildKey"]/@value')[0]
            print(token, build_key)
            my_headers = {
                'X-Atlassian-Token': 'no-check',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'X-Requested-With': 'XMLHttpRequest',
                'DNT': '1',
                'Referer': 'https://'+ config.base_url +'/chain/admin/config/defaultStages.action?buildKey=' + build_key,
                'Cookie': 'atl.xsrf.token=' + token,
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'}  # Also content-disposition
            r = session.post(config.base_url + '/ajax/deleteChain.action', headers=my_headers,
                             verify=False, data={'buildKey': build_key, 'atl_token': token})
            print("Cookies: " + str(session.cookies))
            print("Deletion status CODE: {}".format(r.status_code))
            print("Deletion Response : {}".format(r.content))
            return plan_key
