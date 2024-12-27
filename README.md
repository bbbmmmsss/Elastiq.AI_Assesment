# Elastiq.AI_Assesment

*Overview
This Selenium automation script validates the search functionality on the Selenium Playground's Table Search Demo page. It checks that searching for "New York" filters the table to display exactly 5 entries.

**Approach**
1. **##First Install the pytest##**

- pip install pytest

2. Setup

- Use Selenium WebDriver to interact with the browser.
- The URL is navigated to using driver.get().

3. Search Interaction
- Locate the search box by using XPath.
- Input the search term "New York".

4. Validates that the search results 

- By using assert method (==) 
- Count the number of visible rows using XPath.
Assert that the count matches the expected value (5 entries).

**How to Run the Script**
1. **Run the Script:**

**Use these command**

- pytest elastiqAI/qa_selenium_test.py  

- In this **"elastiqAI"** is the directory of the program file that's why i use

