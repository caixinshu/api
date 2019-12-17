from base.base_driver import ShopDriver
from base.log import Log


class BasePage:
    def __init__(self,base_driver:ShopDriver):
        self.base_driver = base_driver
        # self.log = Log('..\\logs')
