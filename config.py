import os
#from git import Repo


class Config(object):
    '''
    a config object for the plan archiver
    '''

    def __init__(self, base_url, auth):
        self.base_url = base_url
        self.auth = auth
        self.git_path = os.getcwd()


bamboo_config = Config('your_bamboo_instance_url', ('your_user', 'your_password'))
