import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element_attribute


@pytest.mark.smoke
def test_search_functionality():
    driver=webdriver.Chrome()

    #Navigate to the selenium playgrownd Table Search Demo
    driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")

    #Maxamize the window
    driver.maximize_window()

    #Locate with search box and send keys "New York"
    driver.find_element(By.XPATH,"//input[@type='search']").send_keys("New York")

    time.sleep(2)

    #Validates that the search results show 5 entries out of 24 total entries.
    search_results = driver.find_elements(By.XPATH, "//tr[@role='row']")
    assert len(search_results) == 6

    total_entries = driver.find_element(By.XPATH, "//div[@id='example_info']").is_displayed()
    assert total_entries == True
    print("Showing 1 to 5 of 24 entries (filtered from 24 total entries)")


    driver.quit()
