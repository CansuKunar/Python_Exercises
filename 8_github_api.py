import requests
import json

class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = '123456789'             #You can obtain it directly from Git-hub. It is put here at randomly.

    def getUser(self, username):
        response = requests.get(self.api_url+'/users/'+username)
        return response.json()
    
    def getRepositories(self, username):
        response = requests.get(self.api_url+'/users/'+ username+'/repos')
        return response.json()
    
    def createRepository(self,name, description):
        response = requests.post(self.api_url+'/user/repos?access_token'+ self.token, json = {
            "name":name,
            "description":description,
            "homepage":"https://github.com",
            "private":False,
            "has_issues":True,
            "has_projects":True,
            "has_wiki":True
        })
        return response.json()

Git_Hub = Github()

while True:
    print('Menu'.center(50,'-'))
    option = input('1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nYour Choice: ')
    if option == '4':
        break
    else:
        if option == '1':
            username = input('User Name: ')
            result = Git_Hub.getUser(username)
            print(f"name: {result['name']}\npublic repos: {result['public_repos']}\nfollower: {result['followers']}")
        elif option == '2':
            username = input('User Name: ')
            result = Git_Hub.getRepositories(username)
            for repo in result:
                print(repo['name'])
        elif option == '3':
            name = input('Repository Name: ')
            description = input('Repository Description: ') # Other features can be added here.
            result = Git_Hub.createRepository(name, description)
            print(result)
        else: 
            print("Wrong Choice.")
