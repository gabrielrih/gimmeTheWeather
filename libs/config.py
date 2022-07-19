import yaml

class YmlConfig:
    def __init__(self, path):
        self.path = path
        self._get_configs_by_yml()

    def _get_configs_by_yml(self):
        with open(self.path) as f:
            self.configs = yaml.load(f, Loader=yaml.FullLoader)
        try:
            self.token = self.configs['climaTempo']['token']
        except:
            self.token = None
        try:
            self.cityId = self.configs['climaTempo']['cityId']
        except:
            self.cityId = None
        try:
            self.phoneNumbers = self.configs['callMeBot']
        except:
            self.phoneNumbers = []
        return self