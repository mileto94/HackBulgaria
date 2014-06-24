import requests
from p import password, user_name
import zipfile


def make_request(link):
    d = requests.get(link, auth=(user_name, password))
    info = d.json()
    return info


def main():
    user_name = input("Enter user name -> ")
    info = make_request('https://api.github.com/users/' + user_name)
    # print(info)
    repos = make_request(info["repos_url"])
    print(repos)
    repo = input("Enter a repo -> ")
    download_link = "https://api.github.com/users/" + user_name + "/" + repo + "/archive/master.zip"
    r = str(make_request(download_link))
    with zipfile.ZipFile(user_name + repo + '.zip', 'w') as myzip:
        myzip.write(r)


if __name__ == '__main__':
    main()
