
class Plan(object):
    def __init__(self, plan_key, plan_lables):
        self.key = plan_key
        self.labels = plan_lables

    def __repr__(self):
        return "Plan("+self.key+","+str(self.labels)+")"


class BlackPlan(object):
    def __init__(self, plan_key, project_name, name):
        self.key = plan_key
        self.project_name = project_name
        self.name = name

    def __repr__(self):
        return "BlackPlan("+self.project_name+"."+self.name+"("+self.key+"))"
