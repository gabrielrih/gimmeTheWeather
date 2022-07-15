import configparser

class Config:
    def __init__(self, path):
        self.path = path
        self._get_configs()

    def _get_configs(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.path)
        try:
            self.token = self.config['CREDENTIALS']['TOKEN']
        except:
            self.token = None
        try:
            self.cityId = self.config['CREDENTIALS']['CITY_ID']
        except:
            self.cityId = None
        return self