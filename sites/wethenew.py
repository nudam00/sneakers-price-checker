import time


class Wethenew():

    def __init__(self, sku, size, page):
        self.sku = sku
        self.size = size
        self.page = page

    def __get_product(self):
        # Gets product page

        try:
            self.page.goto('https://sell.wethenew.com/listing', timeout=0)
            self.page.wait_for_load_state('load')
            self.page.locator(
                'xpath=//input[@type="search"]').type(self.sku)
            self.page.wait_for_load_state('load')
            time.sleep(2)
            self.page.locator(
                'xpath=//*[@id="__next"]/div/div[1]/div/div/div[3]/div/div/div/div/div/div[2]/button').click()
            self.page.wait_for_load_state('load')
            time.sleep(2)
            return True
        except:
            return False

    def get_price(self):
        # Gets price

        # Sometimes there are more than one product page
        self.__get_product()

        try:  # Cos jest nie tak
            print("self size:"+self.size)
            print("WTB\n{}".format(self.size))
            print("WTB{}".format(self.size))
            print(self.page.locator(
                'xpath=//li[@role="button"]').all())
            try:
                self.page.locator(
                    'xpath=//li[@role="button"]', has_text=self.size).click()
            except:
                self.page.locator(
                    'xpath=//li[@role="button"]', has_text="WTB\n{}".format(self.size)).click()
            time.sleep(1)
            price = self.page.locator(
                'xpath=//span[@style="font-weight: 500;"]').inner_text()
            return price.replace('€', '')
        except:
            return 0
