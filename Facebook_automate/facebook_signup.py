from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def automate_facebook_signup(first_name, last_name, email, password, birth_month, birth_day, birth_year, gender):
    # Replace 'path_to_chromedriver' with the actual path to your Chrome WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Open Facebook signup page
        driver.get('https://www.facebook.com')
        # selects the Create New Account button
        driver.find_element(By.XPATH, "//*[text()='Create New Account']").click()
        time.sleep(2)

        # Locate the signup fields and enter the provided information
        first_name_field = driver.find_element('name', 'firstname')
        last_name_field = driver.find_element('name', 'lastname')
        email_field = driver.find_element('name', 'reg_email__')
        password_field = driver.find_element('name', 'reg_passwd__')
        birth_month_dropdown = driver.find_element('name', 'birthday_month')
        birth_day_dropdown = driver.find_element('name', 'birthday_day')
        birth_year_dropdown = driver.find_element('name', 'birthday_year')
        gender_radiobuttons = driver.find_elements('name', 'sex')

        first_name_field.send_keys(first_name)
        last_name_field.send_keys(last_name)
        email_field.send_keys(email)
        password_field.send_keys(password)

        # Select birth date from dropdowns
        birth_month_dropdown.send_keys(birth_month)
        birth_day_dropdown.send_keys(birth_day)
        birth_year_dropdown.send_keys(birth_year)

        # Select gender
        for radio in gender_radiobuttons:
            if radio.get_attribute('value').lower() == gender.lower():
                radio.click()
                break

        # Submit the signup form
        password_field.send_keys(Keys.RETURN)

        # Wait for a while to ensure the signup process completes
        time.sleep(5)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser window after completion
        driver.quit()

if __name__ == "__main__":
    first_name = 'John'
    last_name = 'Doe'
    email = 'johndoe@example.com'
    password = 'your_password'
    birth_month = 'January'  # Replace with the desired birth month
    birth_day = '1'  # Replace with the desired birth day
    birth_year = '2000'  # Replace with the desired birth year
    gender = 'Male'  # Replace with 'Male' or 'Female'

    automate_facebook_signup(first_name, last_name, email, password, birth_month, birth_day, birth_year, gender)
