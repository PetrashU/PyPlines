from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

print(f"Chrome version: {webdriver.Chrome(executable_path=ChromeDriverManager().install()).capabilities['browserVersion']}")
print(f"ChromeDriver version: {ChromeDriverManager().install()}")

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('http://localhost:5000/shirts')

i = 0

new_color = "New color"
new_text = "New text"

updated_color = "Updated color"
updated_text = "Updated text"

def test_add_shirt():
    color_input = driver.find_element(By.NAME, "color")
    text_input = driver.find_element(By.NAME, 'text')
    add_button = driver.find_element(By.NAME, "AddButton")

    color_input.send_keys(new_color)
    text_input.send_keys(new_text)
    time.sleep(4)
    add_button.click()

    time.sleep(4)
    assert new_color in driver.page_source, f"Error: New Shirt record with color '{new_color}' isn't on the page. Check CREATE function, or related."
    assert new_text in driver.page_source, f"Error: New Shirt record with text '{new_text}' isn't on the page. Check CREATE function, or related."

def test_update_shirt():
    try:
        update_button = driver.find_elements(By.NAME,"UpdateButton")[i]
        new_color_input = driver.find_elements(By.NAME,"new_color")[i]
        new_text_input = driver.find_elements(By.NAME, "new_text")[i]
    except IndexError as e:
        print(f"'Update' test expects a record on {i} position. Exception: {e}")
        exit(1)

    new_color_input.send_keys('Updated color')
    new_text_input.send_keys('Updated text')
    time.sleep(4)
    update_button.click()
    time.sleep(4)

    assert 'Updated color' in driver.page_source, f"Error: Updated Shirt record with color '{updated_color}' isn't on the page. Check UPDATE function, or related."
    assert 'Updated text' in driver.page_source, f"Error: Updated Shirt record with text '{updated_text}' isn't on the page. Check UPDATE function, or related."

def test_delete_shirt():
    try:
        delete_button = driver.find_elements(By.NAME, "DeleteButton")[i]
    except IndexError as e:
        print(f"'Delete' test expects a record on {i} position. Exception: {e}")
        exit(1)
    
    delete_button.click()

    time.sleep(4)

    assert 'Updated color' in driver.page_source, f"Error: Deleted Shirt record with color '{updated_color}' is still on the page. Check if there is any other record with that color or inspect DELETE function and related."
    assert 'Updated text' not in driver.page_source,  f"Error: Deleted Shirt record with text '{updated_text}' is still on the page. Check if there is any other record with that text or inspect DELETE function and related."


test_add_shirt()

i = len(driver.find_elements(By.NAME, "DeleteButton")) - 1

test_update_shirt()
test_delete_shirt()


driver.quit()
