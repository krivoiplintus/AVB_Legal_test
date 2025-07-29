import configparser


global_config = configparser.ConfigParser()
global_config.read('test_config.ini')


class ConfigProvider:

    def __init__(self) -> None:
        self.config = global_config

    def get(self, section: str, property: str) -> str:
        return self.config[section].get(property)

    def getint(self, section: str, property: str) -> int:
        return self.config[section].getint(property)

    def get_ui_url_main_page(self) -> str:
        return self.config["ui"].get("url_main_page")

    def get_ui_url_cart_page(self) -> str:
        return self.config["ui"].get("url_cart_page")

    def get_ui_url_novelty_page(self) -> str:
        return self.config["ui"].get("url_novelty_page")

    def get_ui_timeout(self) -> int:
        return self.config["ui"].getint('timeout')

    def get_api_base_url(self) -> str:
        return self.config["api"].get("base_url")

    def get_api_token(self) -> str:
        return self.config["api"].get("token")
