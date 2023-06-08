import random
from selenium import webdriver
from selenium.webdriver.common.by import By


url = "https://www.reddit.com/r/maths/"


options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(url)

div_element = driver.find_element(By.XPATH, "//div[contains(@class, '_31N0dvxfpsO6Ur5AKx4O5d')]")

div_main_elements = div_element.find_elements(By.XPATH, "//div[contains(@class, '_1oQyIsiPHYt6nx7VOmd1sz')]")

# integer = int(input("How many post: "))
# requirements = div_main_elements[:integer]

j = random.randrange(100000, 1000000)
for i in div_main_elements:
    i.screenshot(f"ss{j}.png")
    j += 1

# element.screenshot("./Image/screen.png")
