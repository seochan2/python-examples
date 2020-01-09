import requests

def main():
    URL = ""

    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Connection": "Keep-Alive"
    }
    
    bsObj = BeautifulSoup(session.get(URL, headers=headers).content, "html.parser")
    
    a_tag_list = bsObj.find_all('a')
    
    for a_tag in a_tag_list:
        print(a_tag)
    
if __name__ == "__main__":
    main()