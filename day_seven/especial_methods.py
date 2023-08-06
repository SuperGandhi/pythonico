class Desktop:
    def __init__(self, keyboard, mouse, monitor, cpu):
        self.keyboard = keyboard
        self.mouse = mouse
        self.monitor = monitor
        self.cpu = cpu
    
    def __del__(self):
        print("Object {cpu} destroyed".format(cpu=self.cpu))
    
    def price(self):
        return f"{self.keyboard} + {self.mouse} + {self.monitor} + {self.cpu}"

# Example usage:
keyboard_price = 50
mouse_price = 20
monitor_price = 200
cpu_price = 500

desktop = Desktop(keyboard_price, mouse_price, monitor_price, cpu_price)
print("Total price:", desktop.price())  # Output: "Total price: 50 + 20 + 200 + 500"

del desktop




    
    