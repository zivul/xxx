import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from time import sleep
import logging.config
from os import path
import logging

logging.basicConfig(level=logging.DEBUG, filename='../my_log.log',
                    format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]',
                    datefmt='%d/%m/%Y %I:%M:%S', encoding='utf-8', filemode='w')

logger = logging.getLogger(__name__)
handler = logging.FileHandler('../test.log', encoding='utf-8')
formatter = logging.Formatter('%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info('Тестируем файл на данные')


# log_file_level = path.join(path.dirname(path.abspath(__file__)), 'loggin.ini')
# logging.config.fileConfig(log_file_level)


@pytest.fixture()
def set_up_browser():
    options = ChromeOptions()
    driver = webdriver.Chrome(options=options)
    options.page_load_strategy = 'none'
    driver.implicitly_wait(60)
    yield driver
    sleep(5)
    driver.quit()
