import requests
from bs4 import BeautifulSoup

url="https://www.codechef.com/users/storm100"
url_cf=" https://codeforces.com/api/user.info?handles=daiwik100&checkHistoricHandles=false"
url_lc="https://leetcode.com/u/daiwikpalavarapu755/"
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/124.0.0.0 Safari/537.36"
    }

response = requests.get(url, headers=headers)
res2=requests.get(url_cf)
res2=res2.json()
res3=requests.get(url_lc,headers=headers)
s=BeautifulSoup(res3.text,"html.parser")
r_lc=s.find("div",class_="text-label-1 dark:text-dark-label-1 flex items-center text-2xl")



if response.status_code !=200:
        print("problem here")
        print(response.status_code)

soup=BeautifulSoup(response.text,"html.parser")
rating_tag=soup.find("div",class_="rating-number")
if rating_tag:
            rating = rating_tag.text.strip()
            stars = soup.find("span", class_="rating")
            stars = stars.text.strip() if stars else "N/A"
            print(rating)      
else:
    print("no")

print(res2["result"][0]["rating"])
print(1456)
