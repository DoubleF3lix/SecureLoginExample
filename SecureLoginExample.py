import json
from passlib.context import CryptContext

# Writes to the JSON file with the DIR specified in 'jsonDIR'
def writeData(data):
    with open(jsonDIR, "w") as jsonFile:
        json.dump(data, jsonFile)

# Grabs the data from the JSON file and prints it to the console
def getData():
    with open(jsonDIR, "r") as jsonFile:
        data = json.load(jsonFile)
        return data

# Takes the plaintext password and hashes it and salts it
def encryptPassword(password):
    return pwd_context.hash(password)

# Checks if the encrypted password is equal to a plaintext password
def chkEncryptPassword(password, hashed):
    return pwd_context.verify(password, hashed)

# Allows the part where the password is checked and asked for to loop
def askForPassword(username, data):
    print()
    print("Enter the password for " + username + ":")
    password = input("> ")
    success = chkEncryptPassword(password, data[username]['password'])
    if success:
        print("Access Granted")
    else:
        print("Invalid password!")
        askForPassword(username, data)

# Provides type of encryption and number of iterations
pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)

# Specifies Directory for the getData() and writeData() functions
jsonDIR = "D:\\Documents\\userData.json"

# Loops this code
while True:
    # Assigns the existing JSON data to the 'data' variable
    data = getData()
    
    print("Login:")
    print()
    print("Enter a username:")
    username = input("> ")
    if username in data:
        def askForPassword():
            print()
            print("Enter the password for " + username + ":")
            password = input("> ")
            success = chkEncryptPassword(password, data[username]['password'])
            if success:
                print("Access Granted")
            else:
                print("Invalid password!")
                askForPassword()

        askForPassword()

    else:
        print("User does not exist! Creating it now...")
        print("Enter the password you'd like to assign to " + username + ":")
        password = input("> ")
        password = encryptPassword(password)
        data[username] = {"password": password, "balance": 10}
        writeData(data)

    print()
    print()