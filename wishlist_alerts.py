```python
import json
import requests
from user_profile import UserProfile
from product_data import ProductData

class WishlistAlerts:
    def __init__(self, user_id):
        self.user_id = user_id
        self.user_profile = UserProfile(user_id)
        self.product_data = ProductData()

    def add_to_wishlist(self, product_id):
        wishlist = self.user_profile.get_wishlist()
        if product_id not in wishlist:
            wishlist.append(product_id)
            self.user_profile.update_wishlist(wishlist)
            return {"status": "success", "message": "Product added to wishlist"}
        else:
            return {"status": "error", "message": "Product already in wishlist"}

    def remove_from_wishlist(self, product_id):
        wishlist = self.user_profile.get_wishlist()
        if product_id in wishlist:
            wishlist.remove(product_id)
            self.user_profile.update_wishlist(wishlist)
            return {"status": "success", "message": "Product removed from wishlist"}
        else:
            return {"status": "error", "message": "Product not found in wishlist"}

    def check_price_drop(self):
        wishlist = self.user_profile.get_wishlist()
        alerts = []
        for product_id in wishlist:
            product = self.product_data.get_product(product_id)
            if product["price"] < product["previous_price"]:
                alerts.append({"product_id": product_id, "message": "Price dropped"})
        return alerts

    def send_alerts(self):
        alerts = self.check_price_drop()
        for alert in alerts:
            # Send alert to user. This could be an email, push notification, etc.
            # This is a placeholder print statement. Replace with actual alert sending code.
            print(f"Alert for user {self.user_id}: {alert['message']} for product {alert['product_id']}")

if __name__ == "__main__":
    wishlist_alerts = WishlistAlerts("user123")
    wishlist_alerts.add_to_wishlist("product456")
    wishlist_alerts.check_price_drop()
    wishlist_alerts.send_alerts()
```