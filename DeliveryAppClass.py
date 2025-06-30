
from tkinter import *

class DeliveryApp:
    #new-menu
        def __init__(self):
            self.window = Tk()
            self.window.geometry("420x420")  
            self.window.title("Food Delivery System")

            self.label = Label(self.window, text="Hello, welcome to the Food Delivery System!")
            self.label.pack()

            self.button1 = Button(self.window, text="Place Order", command=self.create_order_window,
                                font=("Arial", 20), fg="#00FF00", bg="black")
            self.button1.pack(pady=10)

            

            self.button2 = Button(self.window, text="Track order", command=self.create_track_window,
                                font=("Arial", 20), fg="#00FF00", bg="black")
            
            self.button2.pack(pady=10)
            
            
            self.button3 = Button(self.window, text="something else", command=self.create_customer_window,
                                font=("Arial", 20), fg="#00FF00", bg="black")
            
        
            self.button3.pack(pady=10)
            



            self.window.mainloop() 

        def create_order_window(self):
            print("Thank you for ordering")
            def close_window():
                order_window.destroy() 
            
            
            
            order_window = Tk()
            order_window.title("Place order")
            order_window.geometry("300x300")
            label = Label(order_window, text="Place your order here!", font=("Arial", 14))
            label.pack(pady=20)
            button = Tk.Button(order_window, text="Close", command=close_window)
            button.pack()



        def create_track_window(self):
            order_window = Tk()
            order_window.title("Track order")
            order_window.geometry("300x300")
            label = Label(order_window, text="Track your order here!", font=("Arial", 14))
            label.pack(pady=20)
            

        def create_customer_window(self):
            order_window = Tk()
            order_window.title("Customer Service")
            order_window.geometry("300x300")
            label = Label(order_window, text="For customer service ----->", font=("Arial", 14))
            label.pack(pady=20)

        def create():

            # Label
            label = Label(self.new_window, text="Choose a food item:", font=("Arial", 14))
            label.pack(pady=10)

            # Listbox
            self.listbox = Listbox(self.new_window, font=("Arial", 12), selectmode=MULTIPLE)
            self.listbox.pack(pady=20)

            food_items = [
                "Pizza - £12.99", "Burger - £8.99", "Pasta - £10.99", "Sushi - £15.99",
                "Tacos - £7.99", "Steak - £18.99", "Salmon - £16.50", "Fried Chicken - £9.99",
            
                
            ]
            for item in food_items:
                self.listbox.insert(END, item)

            self.listbox.config(height=self.listbox.size())

            # Entry Box for adding custom items
            self.entryBox = Entry(self.new_window, font=("Arial", 12))
            self.entryBox.pack(pady=5)

            # Add Button
            self.addButton = Button(self.new_window, text="Any Alergies?", command=self.allergy)
            self.addButton.pack(pady=5)

            # Submit Button
            self.submitButton = Button(self.new_window, text="Submit Order", command=self.submit)
            self.submitButton.pack(pady=10)

        def allergy(self):
            print("Your allergies have been considered. ")

        def submit(self):
            """Displays selected food items in the console."""
            selected_items = [self.listbox.get(i) for i in self.listbox.curselection()]
            if selected_items:
                print("You have ordered:")
                for item in selected_items:
                    print(item)
            else:
                print("No items selected!")


if __name__ == "__main__":
    app = DeliveryApp()
