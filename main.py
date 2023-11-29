import json
import hashlib

# Function to get the hash string from input string
def generateHash(inputString):
    hashObject = hashlib.sha256()
    hashObject.update(inputString.encode('utf-8'))
    hashValue = hashObject.hexdigest()
    return hashValue


def main():
    # Reading and loading json file ("wifi.json")
    file = open('wifi.json')
    data = json.load(file)

    print("Brute force attack enabled\nWait for sometime...\n")
    # Brut force attack to get password
    for wifiSSID in data:
        passwordHash = data[wifiSSID]

        # Reading the wordlist to perfrom Dictionary Attack
        wordListFile = open('wordlist.txt', 'r', errors='ignore')
        body = wordListFile.read().lower()
        words = body.split('\n')

        print("Searching the Password of " + wifiSSID + "\n")
        # Iterate the loop on words list to get the valid password
        for i in range(len(words)):
            word = words[i]
            # Generate the word hash
            wordHash = generateHash(word)
            # Match the word hash with the password hash
            if (wordHash == passwordHash):
                print("WiFi SSID : ", wifiSSID)
                print("Word hash: ", wordHash)
                print("Password hash: ", passwordHash)
                print("Decrypted WiFi Password: ", word)
                print("=" * 100, "\n")
                break


main()
