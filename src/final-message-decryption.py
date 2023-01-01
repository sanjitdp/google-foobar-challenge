from base64 import b64decode

encrypted_message = """CEYdHwoXAUBFF1NbTk0OBgFSQhdfQUkJBhgIVldXBgRJSlNUQ1ZFRBYEAw8NU0gTEVUVBwEYHQdD EwwQVAgACRsRAFpUXBZGQkpOFQdbX1UFBAMPBwBDEwwQVBQABgYXD1ZSF19BSRgIFgZaQkNUQVRK TgcFVVMXX0FJDAYbQxMMEFQWBwRIUxk="""

key = "sanjitd360"

output = ""
for i, c in enumerate(b64decode(encrypted_message)):
    output += chr(c ^ ord(key[i % len(key)]))

print(output)
