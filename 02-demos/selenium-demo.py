import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.save_screenshot('screenshot.png')
# driver.close()

driver = webdriver.Chrome()
driver.get("https://www.quora.com/search?q=machine+learning")
body = driver.find_element_by_css_selector('body')
#
for _ in range(100):
    body.send_keys(Keys.DOWN)
    time.sleep(1.00)

soup = BeautifulSoup(driver.page_source, 'html.parser')

questions = soup.select("a.question_link span.ui_qtext_rendered_qtext")

for i, q in enumerate(questions):
    print(i, q.get_text())
    print("\n")

driver.close()
