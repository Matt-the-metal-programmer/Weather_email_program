import requests
from bs4 import BeautifulSoup
from Email_func import Send_email
import time

page = requests.get("https://forecast.weather.gov/MapClick.php?CityName=Harrisonburg&state=VA&site=LWX&textField1=38.4367&textField2=-78.874&e=0#.Xc7rWS3Mzq0")
soup = BeautifulSoup(page.content,'html.parser')
week = soup.find(id='seven-day-forecast-body')
items = week.find_all(class_="tombstone-container")
period_names = []
short_desc = []
temps = []

def main():
    # do stuff
    scrape_data()
    print("Email sent!")
    print("this is a test of the git branch")
def scrape_data():
    for i in range(len(items)):
        period_names.append(items[i].find(class_="period-name").get_text())
        short_desc.append(items[i].find(class_="short-desc").get_text())
        temps.append(items[i].find(class_="temp").get_text())
    message = ""
    for i in range(len(period_names)):
        message += period_names[i].ljust(20) + short_desc[i].ljust(20) + " " + temps[i] + "\n"
    message = message.replace('\xb0', 'degrees ')
    print(message)
    Send_email(message)

main()