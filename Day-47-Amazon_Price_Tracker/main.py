from bs4 import BeautifulSoup
import requests
import smtplib
import os
amazon_endpoint = "https://appbrewery.github.io/instant_pot/"

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

response = requests.get(url=amazon_endpoint)
response.raise_for_status()

soup = BeautifulSoup(response.content, "html.parser")
## MY SOLVE
# price = soup.find(name="span", class_="a-price-whole").text
# price += soup.find(name="span", class_= "a-price-fraction").text
# price = float(price)

# Find the HTML element that contains the price
price = soup.find(class_="a-offscreen").get_text()
# Remove the dollar sign using split
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)


# Get the product title
title = soup.find(id="productTitle").get_text().strip()
print(title)

# Set the price below which you would like to get a notification
BUY_PRICE = 100

if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{amazon_endpoint}".encode("utf-8")
        )
