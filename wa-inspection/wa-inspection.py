import requests


def main():
    url = ""

    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Connection": "Keep-Alive"
    }
    
    bs_obj = BeautifulSoup(session.get(url, headers=headers).content, "html.parser")
    
    a_tag_list = bs_obj.find_all('a')
    
    file_name = "result.html"
    f = open(file_name, 'w')
    
    for a_tag in a_tag_list:
        print(a_tag.text)
        data = ' '.join([str(a_tag), str('\n')])
        f.write(data)
    
    f.write("----------")
    
    img_tag_list = bs_obj.find_all('img')
    
    for img_tag in img_tag_list:
        print(img_tag.text)
        data = ' '.join([str(img_tag), str('\n')])
        f.write(data)

    f.write("----------")
    
    div_tag_list = bs_obj.find_all('div', {'id' : 'test'})
    
    data = ' '.join('div cnt ::', len(div_tag_list), str('\n')])
    f.write(data)


if __name__ == "__main__":
    main()