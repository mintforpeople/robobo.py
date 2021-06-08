# This imports the library    


# This creates an instance of the Robobo class with the indicated IP address
# You have to modify next line
from robobo.Robobo import Robobo

rob = Robobo("10.113.36.150")

# This connects to the robobo base
rob.connect()

# This makes Robobo say "Hello World"
rob.sayText("Hello world")

# This disconnects from the robobo base
rob.disconnect()