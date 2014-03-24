from order_pizza import OrderPizza
import glob


class DealWithFiles(OrderPizza):
    """docstring for DealWithFiles"""
    def __init__(self, order):
        self.order = order

    def save(self, filename):
        file_write = open(filename, "a")
        file_write.write(OrderPizza.print_status(self))
        file_write.close()
        return OrderPizza.print_status(self)

    def match_lists_with_id(self):
        files = glob.glob("orders_*")
        result = []
        for index in range(len(files)):
            result.append((index + 1, files[index]))
        return result

    def show_lists_with_id(self):
        files = self.match_lists_with_id()
        result = ""
        for file in files:
            result += "[" + str(file[0]) + "] - " + file[1]
            if file != files[len(files) - 1]:
                result += "\n"
        return result

    def load_data(self, filename):
        file_read = open(filename, "r")
        file_content = file_read.read().split("\n")
        file_read.close()
        file_content = "\n".join(file_content)
        file_content = file_content.replace(" - ", " ")
        contents = file_content.split("\n")
        result = []
        for content in contents:
            for index in range(len(content)):
                if content[index] == " ":
                    result.append((content[:index], content[index + 1:]))
        return result
