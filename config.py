import yaml


class Config:
    def __init__(self) -> None:
        with open("config.yaml", 'r') as f:
            self.config = yaml.safe_load(f)

    def getZapSettings(self) -> dict:
        return self.config['settings']['zap_settings']
