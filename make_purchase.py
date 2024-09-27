def make_purchase(self, quantity):
        try:
            
            if quantity <= 0:
                raise ValueError("Error: You cannot purchase a negative or zero quantity.")

            if quantity > self.amount:
                
                print(f"Oops! You wanted to buy {quantity}, but we only have {self.amount} {self.name}(s) in stock.")
                return

            total_price = self.get_price(quantity)
            confirmation = input(f"Are you sure you want to purchase {quantity} {self.name}(s) for ${total_price:.2f}? (yes/no): ").strip().lower()
            if confirmation != 'yes':
                print("Purchase canceled. No changes made to stock.")
                return         
            self.amount -= quantity
            print(f"Success! You've purchased {quantity} {self.name}(s) for a total of ${total_price:.2f}.")
            print(f"Remaining stock: {self.amount} {self.name}(s) left.\n")

        except ValueError as e:
            print(e)
product = Product("Laptop", 50, 1000)
product.make_purchase(5)
product.make_purchase(10)
product.make_purchase(40)
product.make_purchase(-5)
product.make_purchase(100)
