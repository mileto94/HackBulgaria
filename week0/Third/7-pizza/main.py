from order_pizza import OrderPizza
from deal_with_file import DealWithFiles
import sys
from time import time
from datetime import datetime


def main():
    greeting = "Hi, stranger you can order pizza from here! Let me introduce myself: I'm awesome python script which deals with your orders! My name is Script, so what's your name? -> "
    user_name = input(greeting)
    print("Awesome, now you're a good friend of mine, %s!" % user_name)
    print("You can get help anytime you want by entering <help> :)")
    help_you = """Try one of the following:
take <name> <price>
status
save
list
load <number>
finish"""
    goodbye = "Goodbye, %s" % user_name
    orders = DealWithFiles([])
    temp_result = []
    while(True):
        command = input("Enter command -> ")
        command = command.split()
        if command[0] == "help":
            print(help_you)
        elif command[0] == "take":
            name = command[1]
            price = command[2]
            temp_result = orders.take_order(name, price)
            print("Taking order from %s for %s" % (name, price))
        elif command[0] == "status":
            if len(temp_result) < 1:
                print("Try another command! You don't have any orders :P")
            else:
                print(orders.print_status())
        elif command[0] == "save":
            ts = time()
            filename = "orders_" + datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
            orders.save(filename)
            print("Saved order")
        elif command[0] == "list":
            print(orders.show_lists_with_id())
        # elif command
        elif command[0] == "finish":
            print(goodbye)
            break


if __name__ == '__main__':
    main()
