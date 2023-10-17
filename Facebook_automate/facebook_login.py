from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def automate_facebook_login(username, password):
    # Replace 'path_to_chromedriver' with the actual path to your Chrome WebDriver
    driver = webdriver.Edge()

    try:
        # Open Facebook login page
        driver.get('https://www.facebook.com')

        # Locate the email and password fields and enter your credentials
        email_field = driver.find_element('name', 'email')
        password_field = driver.find_element('name', 'pass')

        email_field.send_keys(username)
        password_field.send_keys(password)

        # Submit the login form
        password_field.send_keys(Keys.RETURN)

        # Wait for a while to ensure the page loads completely
        time.sleep(10)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser window after completion
        driver.quit()

if __name__ == "__main__":
    # Replace 'your_username' and 'your_password' with your actual Facebook credentials
    automate_facebook_login('petkany7@gmail.com', 'Pkn2030**')
