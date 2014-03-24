from deal_with_file import DealWithFiles
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
    command_list = []
    while(True):
        command = input("Enter command -> ")
        command = command.split()
        if command[0] == "help":
            command_list.append("help")
            print(help_you)
        elif command[0] == "take":
            command_list.append("take")
            name = command[1]
            price = command[2]
            temp_result = orders.take_order(name, price)
            print("Taking order from %s for %s" % (name, price))
        elif command[0] == "status":
            command_list.append("status")
            if len(temp_result) < 1:
                print("Try another command! You don't have any orders :P")
            else:
                print(orders.print_status())
        elif command[0] == "save":
            command_list.append("save")
            ts = time()
            filename = "orders_" + datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
            orders.save(filename)
            print("Saved order")
        elif command[0] == "list":
            command_list.append("list")
            print(orders.show_lists_with_id())
        elif command[0] == "load":
            command_list.append("load")
            print(command_list)
            if "list" not in command_list:
                print("Use list command before loading :D")
            elif "save" not in command_list and command_list.count("load") < 2:
                print("You have unsaved orders. If you want to continue, enter <load> again :)")
            elif command_list.count("load") == 2:
                t = orders.load_data(command[1])
                orders = t
                print(orders)
        elif command[0] == "finish":
            command_list.append("finish")
            print(goodbye)
            break


if __name__ == '__main__':
    main()
