city = input("Введите город: ")
import requests 
from bs4 import BeautifulSoup
site  = ("https://www.google.com/search?q=погода+в+"+str(city.split())+"&hl=ru&sxsrf=ALiCzsaDFVg-mJ46G9JY1k2woiVs07EDkw%3A1671210270761&source=hp&ei=HqWcY4jKLOGGwPAP9cKtgAo&iflsig=AJiK0e8AAAAAY5yzLqFF0IHK5muOVlySe3enRck5K4dR&ved=0ahUKEwiI0aC0z_77AhVhAxAIHXVhC6AQ4dUDCAc&uact=5&oq=погода+в+моске&gs_lcp=Cgdnd3Mtd2l6EAMyDQgAEIAEELEDEIMBEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAo6BAgjECc6CwgAEIAEELEDEIMBOgUIABCABDoICAAQsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOgwIIxAnEJ0CEEYQgAI6DggAEIAEELEDEIMBEMkDUABYpBBgzRFoAHAAeACAAeEBiAGvDJIBBTcuNi4xmAEAoAEB&sclient=gws-wiz")
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"}
full_page = requests.get(site, headers=headers)	
soup = BeautifulSoup(full_page.content, 'html.parser')
convert = soup.findAll("span",{"class":"wob_t","class":"q8U8x"})
convert_1 = soup.findAll("span",{ "id":"wob_dc"})
check=0
d = ""
for temperature in convert :
    d+=temperature.getText()+" "
for weah_r in convert_1:
    d+=weah_r.getText()
    check+=1
print("Погода в городе: ",city," ",d)
if  check!= 1:
    print("Ошибка запроса!")