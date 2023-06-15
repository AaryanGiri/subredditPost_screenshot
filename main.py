import random
from selenium import webdriver
from selenium.webdriver.common.by import By


url = "https://www.reddit.com/r/maths/"


options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(url)

# Find the parent container element that contains the div elements
div_element = driver.find_element(By.XPATH, "//div[contains(@class, '_31N0dvxfpsO6Ur5AKx4O5d')]")

# Find all the div elements within the container
div_main_elements = div_element.find_elements(By.XPATH, "//div[contains(@class, '_1oQyIsiPHYt6nx7VOmd1sz')]")

# integer = int(input("How many post: "))
# requirements = div_main_elements[:integer]

# Generate a random number for screenshot names as it will prevent overwriting files with the same name when the program is executed multiple times.
j = random.randrange(100000, 1000000)
for i in div_main_elements:
    # Take a screenshot of the div element
    i.screenshot(f"ss{j}.png")
    j += 1

# element.screenshot("./Image/screen.png")
