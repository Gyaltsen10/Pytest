import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup WebDriver
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

# Test case to search for a product on Daraz Nepal
def test_search_product(driver):
    driver.get("https://www.daraz.com.np/")

    # Find the search bar and enter a product name (e.g., "laptop")
    search_box = driver.find_element(By.XPATH, "//input[@name='q']")
    search_box.send_keys("laptop")
    search_box.send_keys(Keys.RETURN)

    # Wait for the results to load and verify the search results
    driver.implicitly_wait(5)

    # Assert that the search results are displayed
    results = driver.find_elements(By.CLASS_NAME, "c16H9d")
    assert len(results) > 0, "No products found for 'laptop'"
    
    # Optionally, print out the first result
    print("First product result:", results[0].text)
