# In this program, I used Chrome as a web browser. If you want to use a different browser, you can visit this site: 
# https://selenium-python.readthedocs.io/installation.html#drivers

from github_user_info import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []
        self.following = []
        self.repositories = []

    def sign_in(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        username = self.browser.find_element(By.XPATH, '//*[@id="login_field"]').send_keys(self.username)
        password = self.browser.find_element(By.XPATH, '//*[@id="password"]').send_keys(self.password)

        time.sleep(1)

        self.browser.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[11]').click()
        

    def load_followers(self):
        items = self.browser.find_elements(By.CSS_SELECTOR, ".d-table.table-fixed")

        for name in items:
             self.followers.append(name.find_element(By.CSS_SELECTOR, ".Link--secondary").text)

    def get_followers(self):
        self.browser.get(f"https://github.com/{self.username}?tab=followers")
        time.sleep(2)
        
        self.load_followers()
        
        while True:
            if not self.browser.find_element(By.CLASS_NAME, 'paginate-container').find_elements(By.CLASS_NAME, 'pagination'):
                break
            else:
                links = self.browser.find_element(By.CLASS_NAME, 'pagination').find_elements(By.TAG_NAME, 'a')
                if len(links) == 1:
                    if links[0].text == "Next":
                        links[0].click()
                        time.sleep(1)
                        self.load_followers()
                        
                    else:
                        break
                else:
                    for link in links:
                        if link.text == "Next":
                            link.click()
                            time.sleep(1)
                            self.load_followers()
                        
                        else:
                            continue

    def load_following(self):
        items = self.browser.find_elements(By.CSS_SELECTOR, ".d-table.table-fixed")

        for name in items:
             self.following.append(name.find_element(By.CSS_SELECTOR, ".Link--secondary").text)

    def get_following(self):
        self.browser.get(f"https://github.com/{self.username}?tab=following")
        time.sleep(2)
        
        self.load_following()
        while True:
            if not self.browser.find_element(By.CLASS_NAME, 'paginate-container').find_elements(By.CLASS_NAME, 'pagination'):
                break
            else:
                links = self.browser.find_element(By.CLASS_NAME, 'pagination').find_elements(By.TAG_NAME, 'a')
                if len(links) == 1:
                    if links[0].text == "Next":
                        links[0].click()
                        time.sleep(1)
                        self.load_following()
                        
                    else:
                        break
                else:
                    for link in links:
                        if link.text == "Next":
                            link.click()
                            time.sleep(1)
                            self.load_following()
                        
                        else:
                            continue

    def load_repository(self):
        items = self.browser.find_elements(By.CSS_SELECTOR, ".col-12.d-flex")

        for repo in items:
             self.repositories.append(repo.find_element(By.TAG_NAME, "a").text)

    def get_repository(self):
        self.browser.get(f"https://github.com/{self.username}?tab=repositories")
        time.sleep(2)
        self.load_repository()

        while True:
            if not self.browser.find_element(By.CLASS_NAME, 'paginate-container').find_elements(By.CLASS_NAME, 'pagination'):
                break
            else:
                links = self.browser.find_element(By.CLASS_NAME, 'paginate-container').find_elements(By.TAG_NAME, 'a')
                if len(links) == 1:
                    if links[0].text == "Next":
                        links[0].click()
                        time.sleep(1)
                        self.load_repository()
                        
                    else:
                        break
                else:
                    for link in links:
                        if link.text == "Next":
                            link.click()
                            time.sleep(1)
                            self.load_repository()
                        
                        else:
                            continue


while True:
    print('Menu'.center(50,'*'))
    option = input('1- Sign In\n2- Get Followers\n3- Get Following\n4- Get Repositories\n5- Exit\nYour Choice: ')
    github = Github(username, password)
    if option == '5':
        break
    else:
        if option == '1':
            github.sign_in()
        elif option == '2':
            github.get_followers()
            print(len(github.followers))
            print(github.followers)
        elif option == '3':
            github.get_following()
            print(len(github.following))
            print(github.following)
        elif option == '4':
            github.get_repository()
            print(len(github.repositories))
            print(github.repositories)
        else: 
            print("Wrong Choice.")
