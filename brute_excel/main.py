# Figure out forgotten password. Code is not perfect and should be improved

import itertools
from string import digits, punctuation, ascii_letters
import win32com.client as client
from datetime import datetime
import time

# symbols = digits + punctuation + ascii_letters
# print(symbols)

def brute_excel_doc():
    print("Hello")

    try:
        password_length = input("Input length of the password. Values from and to (e.g. 3 - 7): ")
        password_length = [int(item) for item in password_length.split("-")]
    except:
        print("Check the correctness of provided length.")

    print("If the password contains only numbers, write: '1'\n"
          "If the password contains only letters, write: '2'\n"
          "If the password contains numbers and letters, write: '3'\n"
          "If the password contains numbers, letters and symbols, write: '4'")
    
    try:
        choice = int(input(": "))
        if choice == 1:
            possible_symbols = digits
        elif choice == 2:
            possible_symbols = ascii_letters
        elif choice == 3:
            possible_symbols = digits + ascii_letters
        elif choice == 4:
            possible_symbols = digits + ascii_letters + punctuation
        else:
            possible_symbols = "The chosen option is not correct."
        print(possible_symbols)
    except:
        print("Something is not correct. Check available options.")

    # brute excel doc
    start_timestamp = time.time()
    print(f"Started at - {datetime.fromtimestamp(time.time()).strftime('%H:%M:%S')}")

    count = 0
    for pass_length in range(password_length[0], password_length[1] + 1):
        # will iterate 10 passwords / second
        for password in itertools.product(possible_symbols, repeat=pass_length):
            password = "".join(password)
            
            opened_doc = client.Dispatch("Excel.Application")
            count += 1

        try:
            opened_doc.Workbooks.Open(
                "C:\Users\PC\Desktop\Проекты Python\brute_excel\Book1.xlsx",
                False,
                True,
                None,
                password
            )

            time.sleep(0.1)
            print(f"Finished at - {datetime.fromtimestamp(time.time()).strftime('%H:%M:%S')}")
            print(f"Password cracking time - {time.time() - start_timestamp}")

            return f"Attempt #{count} Password is: {password}"
        except:
            print(f"Attempt #{count} Incorrect {password}")
            pass

def main():
    brute_excel_doc()

if __name__ == "__main__":
    main()