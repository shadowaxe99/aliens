```python
import requests
from bs4 import BeautifulSoup

class PriceComparison:
    def __init__(self, product_id):
        self.product_id = product_id
        self.product_data = self.retrieveData(product_id)

    def retrieveData(self, product_id):
        # This function will interact with the database to retrieve product data
        # For the purpose of this example, we will return a mock data
        return {
            "productName": "Example Product",
            "productPrice": 100,
            "retailerID": "retailer1"
        }

    def comparePrices(self):
        # List of retailers to compare prices
        retailers = ["retailer1", "retailer2", "retailer3"]
        prices = {}

        for retailer in retailers:
            prices[retailer] = self.scrapePrice(retailer)

        return prices

    def scrapePrice(self, retailer):
        # This function will scrape the price of the product from the retailer's website
        # For the purpose of this example, we will return a mock price
        return 100

    def findBestDeal(self):
        prices = self.comparePrices()
        best_deal = min(prices, key=prices.get)
        return best_deal, prices[best_deal]

if __name__ == "__main__":
    product_id = "product1"
    price_comparison = PriceComparison(product_id)
    best_deal, best_price = price_comparison.findBestDeal()
    print(f"The best deal for {price_comparison.product_data['productName']} is at {best_deal} with a price of {best_price}")
```