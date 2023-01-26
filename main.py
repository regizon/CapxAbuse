from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time
codes = []
password_symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',  '1', '2', '3', '4', '5',
                    '6', '7', '8', '9', '0']
login_length = random.randint(5, 15)
password_length = random.randint(8, 15)

def login_generate():
    login = ''
    for i in range(login_length):
        symbol = random.choice(password_symbols)
        login = login + symbol
    return login

def password_generate():
    password = ''
    for i in range(password_length):
        symbol = random.choice(password_symbols)
        if symbol == '.' or symbol == '_' or symbol == '-':
            continue
        else:
            pass
        password = password + symbol
    return password

def reger():
    global file
    with open("invite_codes.txt", "r") as file:
        for lines in file:
            codes.append(lines)
    file = open("invites.txt", "a+")
    for invite_code in codes:
        for i in range(4):
            try:
                login = ''
                for i in range(login_length):
                    symbol = random.choice(password_symbols)
                    login = login + symbol

                password = ''
                for i in range(password_length):
                    symbol = random.choice(password_symbols)
                    if symbol == '.' or symbol == '_' or symbol == '-':
                        continue
                    else:
                        pass
                    password = password + symbol
                options = webdriver.ChromeOptions()
                #options.add_argument('--headless')
                global driver
                driver = webdriver.Chrome(executable_path="chromedriver\\chromedriver.exe", options=options)
                driver.get("https://app.capx.fi/")
                driver.maximize_window()
                time.sleep(3)
                driver.find_element(By.XPATH, "/html/body/div/div/main/div/div[1]/div/a[1]/div[1]").click()
                time.sleep(2)
                driver.find_element(By.XPATH, "/html/body/div/div/main/div/div[1]/div/a[1]/div").click()
                time.sleep(2)
                email_input = driver.find_element(By.XPATH, "/html/body/div/div/main/div/div[1]/div/form/div[1]/div/input")
                password_input = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[1]/div/form/div[2]/div/input')
                email_input.send_keys(login + "@rambler.ru")
                password_input.send_keys(password)
                driver.find_element(By.XPATH, "/html/body/div/div/main/div/div[1]/div/form/button").click()
                time.sleep(5)
                login_input = driver.find_element(By.XPATH, "/html/body/div/div/main/div/div[1]/div/form/div/div/input")
                login_input.send_keys(login)
                driver.find_element(By.XPATH, "/html/body/div/div/main/div/div[1]/div/form/button").click()
                time.sleep(5)
                ref_code = driver.find_element(By.XPATH, "/html/body/div/div/main/div/div[1]/div/form/div/div/div[1]/input")
                ref_code.send_keys(f"{invite_code}")
                time.sleep(2)
                driver.find_element(By.XPATH, "/html/body/div/div/main/div/div[1]/div/form/button").click()
                time.sleep(3)
                driver.find_element(By.XPATH, "/html/body/div/div/main/div/div[1]/div/button").click()
                time.sleep(5)
                driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/main/div/div/div/div[3]/div[2]/div/div/div/div/div/div[2]/div/div/div").click()
                time.sleep(5)
                driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/div/button").click()
                time.sleep(2)
                driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/main/div/div/div[2]/div[2]/div/button").click()
                time.sleep(3)
                driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[2]/button[2]").click()
                time.sleep(5)
                driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/main/div/div/div/div[3]/div[2]/div/div/div/div/div/div[2]/div/div/div").click()
                time.sleep(2)
                span = driver.find_element(By.CSS_SELECTOR, "#root > div > div > div.flex-grow.flex.flex-col.min-h-screen > main > div > div > div.quest.flex.flex-col-reverse.gap-10.md\:gap-0.md\:flex-row.md\:py-10.md\:px-2 > div.quest-details-2.flex.flex-col > div > div.codestep2-wrapper.mb-3 > div > span")
                new_ref_code = span.text
                file.write(new_ref_code)
                file.write("\n")
                print("Получил реф код")
            except Exception as excp:
                print(excp)
                continue

def main():
    try:
        reger()
    except:
        pass
    finally:
        driver.close()
        driver.quit()
        file.close()

if __name__ == "__main__":
    main()
