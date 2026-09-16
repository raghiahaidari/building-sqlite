
def main():
    while True:
        print("db > ", end="")
        user_input = input().strip()
        if user_input == ".exit":
            break
        else:
            print("Unrecognized command", user_input, ".\n")

if __name__ == "__main__":
    main()