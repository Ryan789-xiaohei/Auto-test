from idlelib.iomenu import encoding

import yaml
from yaml import Loader

from common.tool import get_project_path, sep


class GetConf:
    def __init__(self):
        # with open("D:\\PycharmProjects\\python_auro_request\\auto_test\config\\environment.yaml", "r", encoding="utf-8)") as file:
        #    a = file.read()
        #  print(a)
        # with open("D:\\PycharmProjects\\python_auro_request\\auto_test\\config\\environment.yaml", "r",
        #           encoding="utf-8") as env_file:
        with open(get_project_path() + sep(["config", "environment.yaml"], True), "r", encoding="utf-8") as env_file:
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)
            print(self.env)



#
GetConf()
#
