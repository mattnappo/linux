import json
from pprint import pprint
class Reader():
    def __init__(self):
        self.data = json.load(open("commands.json"))
        self.commands = self.data["commands"]
        self.cmd()
    def cmd(self):
        valid_command = False
        x = input("/ ")
        x = x.lower()
        arguments = x.split(" ")
        iCommand = arguments[0]
        for command in self.commands:
            if iCommand == command:
                valid_command = True
                if len(arguments) == self.commands[iCommand]["argument_length"]:
                    exec(self.commands[iCommand]["execode"])
                else:
                    print("Invalid syntax.")
        if valid_command == False:
            print("Invalid command.")
r = Reader()
