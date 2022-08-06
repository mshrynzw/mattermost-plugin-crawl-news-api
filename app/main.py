import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel
# from tfidf import extract_important_words
from typing import List
from logging_context import LoggingContextRoute
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

app = FastAPI()
app.router.route_class = LoggingContextRoute


class Item(BaseModel):
    url: str
    keyword: str


@app.post("/items")
def update_item(items: List[Item]):
    for item in items:
        crawl_news(item)

    return ulrs


def crawl_news(item):
    try:
        # Set driver
        options = Options()
        options.add_argument('--disable-dev-shm-usage')  # ディスクのメモリスペースを使う
        options.add_argument('--disable-extensions')  # すべての拡張機能を無効
        options.add_argument('--disable-gpu')  # GPUハードウェアアクセラレーションを無効
        options.add_argument('--headless')  # ヘッドレスモードで起動
        options.add_experimental_option("excludeSwitches", ['enable-automation'])  # Chromeは自動テスト ソフトウェア~~ を非表示
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    
        # Set Google advanced search
        driver.get(r"https://www.google.com/advanced_search")
        keyword_text_box = driver.find_element(By.XPATH, r'//*[@id="xX4UFf"]')
        keyword_text_box.clear()
        keyword_text_box.send_keys(item.keyword)
        url_text_box = driver.find_element(By.XPATH, r'//*[@id="NqEkZd"]')
        url_text_box.clear()
        url_text_box.send_keys(item.url)
    
        # Search
        driver.find_element(By.XPATH, r'//*[@id="s1zaZb"]/div[5]/div[9]/div[2]/input[2]').click()
    
        # Go a page
        elements = driver.find_elements(By.XPATH, r'//*[@id="rso"]/div')
        for i in range(len(elements)):
            if i < 2:
                continue
            driver.find_element(By.XPATH, r'//*[@id="rso"]/div[{}]/div/div/div[1]/div/a'.format(str(i + 1))).click()
            break
    
        # Get text
        # TODO CONTINUE
        text = driver.find_element(By.XPATH, r'//*[@id="content"]/div[1]/div/div[2]/div/div[2]').text
    except Exception as e:
        logger.exception('Raise Exception: %s', e)
    finally:
        driver.quit()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
