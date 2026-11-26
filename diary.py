import os
import datetime

filename = "diary.txt"

try:
    # Create the file if it does not exist
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            pass

    entry = input("Enter your diary entry: ")
    timestamp = datetime.datetime.now()
    timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")

    # Append the new diary entry
    with open(filename, "a") as file:
        file.write(timestamp + " - " + entry + "\n")

    # Display all saved entries
    print("\nDiary Entries:")
    with open(filename, "r") as file:
        print(file.read())

except OSError as error:
    print("File error:", error)
