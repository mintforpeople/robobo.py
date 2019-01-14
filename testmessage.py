from utils.Message import Message

name = "ASDF"

value = {
    "asdad":1,
    "asasaskf":2
}
id = 1
msg = Message(name,value,id)

print(msg.encode())