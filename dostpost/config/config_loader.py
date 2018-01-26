import os

ENV_SETTINGS = {
    "development":"config.settings.development",
    "test":"config.settings.test",
    "production":"config.settings.production"
}


class DostpostConfig:
    def __init__(self):
        self.setting = None

    def load_settings(self):
        dostpost_env = os.environ['DOSTPOST_ENV'] if os.environ.get('DOSTPOST_ENV') else "development"
        print "loading settings for %s" %(dostpost_env)
        self.setting = ENV_SETTINGS[dostpost_env]
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", self.setting)
        return self.setting


dostpost_config = DostpostConfig()

