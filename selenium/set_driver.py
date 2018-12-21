from selenium import webdriver


def set_driver():
    driver = webdriver.Chrome("C:\\Users\\ehtis_000\\Downloads\\Compressed\\chromedriver.exe")
    driver.maximize_window()
    driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
    return driver
#
#
# if __name__ == '__main__':
#     set_driver()
