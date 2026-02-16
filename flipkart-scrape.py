import requests
from bs4 import BeautifulSoup
import pandas as pd
Product_name = []
Prices = []
Description = []
Reviews = []

for i in range(2,5):
    url = "https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=6a5232aa-548a-43ba-8a79-a0c5d2b33479&page="+str(i)
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div",class_="QSCKDh dLgFEE")

    #Product name fetch
    names = box.find_all("div",class_="RG5Slk")
    for i in names:
        name = i.text
        Product_name.append(name)

    #Product prices fetch
    prices = box.find_all("div",class_="hZ3P6w DeU9vF")
    for i in prices:
        price = i.text
        Prices.append(price)
        

    #Description fetch
    desc = box.find_all("ul", class_="HwRTzP")
    for i in desc:
        description = i.text
        Description.append(description)


    #Review fetch
    review = box.find_all("div", class_="MKiFS6")
    for i in review:
        name = i.text
        Reviews.append(name)


    #dataframe
    df = pd.DataFrame({"Products":Product_name,"Price":Prices,"Description":Description,"Rating":Reviews})
    # print(df)

    df.to_csv("flipkart.csv")
