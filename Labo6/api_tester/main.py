import requests


def main():
    res = requests.get("https://api.github.com/users/github")
    print(f"Status code: {res.status_code}")
    data = res.json()
    print(f"{data['login']} heeft {data['public_repos']} public repositories")


if __name__ == "__main__":
    main()
