__title__ = "Psudo OOP Authentication"
__description__ = "This program creates a user based on given input, "encrypts" the password, and then provides the user with account information."

__author__ = "Foster Reichert"
__version__ = "1.0.0"
__license__ = "MIT"

# define alphabet list
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# define user class
# used to store and return information about the user
class User:
	def __init__(self, email, username, password):
		self.email = email
		self.username = username
		self.password = password
	
	def init(self):
    # get length of password
		self.password_length = len(self.password)
    # create a dynamic "*" placeholder
		self.password_placeholder = "*" * self.password_length
    # "encrypt" password using ord() and the abc list
		temp = self.password
		self.password = ""
		for i in range(len(temp)):
			self.password += str(ord(temp[i]))
		temp = self.password
		self.password = ""
		for i in range(len(temp)):
			self.password += abc[int(temp[i])]
			
def get_email():
	email = input("What is your email? ")
	if email == "" or None:
		print("Missing required field (email)")
		print("Program will now exit.")
		exit()
	else:
		return email

def get_username():
	username = input("Please enter a username: ")
	if username == "" or None:
		print("Missing required field (username)")
		print("Program will now exit.")
		exit()
	else:
		return username

def get_password():
	password = input("Choose a password: ")
	if password == "" or None:
		print("Missing required field (password)")
		print("Program will now exit.")
		exit()
	else:
		return password

# initilize user variables
user = User(get_email(), get_username(), get_password())
user.init()

bar = "---------------"
for i in range(len(user.email)): bar += "-"

# print user information
print("Connected to: " + user.email)
print(bar)
print("Username: " + user.username)
print("Password: " + user.password_placeholder)
