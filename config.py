import yaml


class Config:
    def __init__(self) -> None:
        with open("config.yaml", 'r') as f:
            self.config = yaml.safe_load(f)
        self.log_file = self.config['settings']['log_file']

    def getZapSettings(self) -> dict:
        return self.config['settings']['zap_settings']
