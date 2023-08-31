# For each file ending .wav
#   Read the file as a byte array
#   Swap the bytes in each 16-bit sample
#   Write the file back out

import os

suffix = "__FIXED"

files = os.listdir(".")

for filename in files:
    if filename.endswith(".wav") and not filename.endswith(f"{suffix}.wav"):
        print("Processing " + filename)
        # Open the file as a byte array
        with open(filename, "rb") as f:
            data = bytearray(f.read())

        if data[0:4] == b"RIFF":
            print("Already valid .wav file")
            continue

        # Swap every other byte
        for i in range(0, len(data), 2):
            data[i], data[i + 1] = data[i + 1], data[i]

        # Write the file back out
        with open(filename[:-4] + f"{suffix}.wav", "wb") as f:
            f.write(data)
