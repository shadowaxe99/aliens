```python
class PremiumFeatures:
    def __init__(self, user_id, subscription_type):
        self.user_id = user_id
        self.subscription_type = subscription_type

    def check_subscription_status(self):
        # Check the subscription status of the user
        # This is a placeholder function, actual implementation would interact with the database
        return True

    def apply_discount(self, product_price):
        # Apply discount based on the subscription type
        if self.subscription_type == 'gold':
            return product_price * 0.9
        elif self.subscription_type == 'silver':
            return product_price * 0.95
        else:
            return product_price

    def early_access(self, product):
        # Provide early access to sales based on the subscription type
        if self.subscription_type in ['gold', 'silver']:
            return True
        else:
            return False

    def upgrade_subscription(self, new_subscription_type):
        # Upgrade the subscription type of the user
        self.subscription_type = new_subscription_type
        # Update the subscription type in the database
        # Placeholder function, actual implementation would interact with the database
        return True
```