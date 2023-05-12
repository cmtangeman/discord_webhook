import requests
from bs4 import BeautifulSoup
import time

# Store previously scraped divs
previous_divs = set()


def scrape_trades():
    url = ""  # put the website you want to scrape here
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        tbody = soup.find("tbody")

        # Find all the divs within the tbody
        divs = tbody.find_all("div")

        # Check for new divs
        new_divs = []
        for div in divs:
            div_id = div.get("id")  # Check if 'id' attribute exists
            if div_id and div_id not in previous_divs:
                previous_divs.add(div_id)
                new_divs.append(div)

        # Process the new divs
        process_new_divs(new_divs)
    else:
        print("Failed to fetch the website")


def process_new_divs(new_divs):

    for div in new_divs:
        print(div.text)


while True:
    scrape_trades()
    # Adjust the interval based on your needs
    time.sleep(60)  # Scrape every 60 seconds
