# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
 #   # Use a breakpoint in the code line below to debug your script.
 #   print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

class Message:
    def __init__(self, message: str, sender: int, receiver: int):
        self.message = message


    def __str__(self):
        return str(self.message)

    #def __eq__(self, __o: object):
    def __eq__(self, __o: object):
        return self.message == __o.message

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  message1 = Message("hello", 1,2)
  message2 = Message("Hello World!",3,2)
  message3 = Message("Hello World!", 1, 3)
  print(message1)
  print( message1 == message2)
  print( message2 == message3)

