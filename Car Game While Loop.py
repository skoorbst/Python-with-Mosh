command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else: 
            started = True
            print("The car has started")
    elif command == "stop":
        if not started :
            print("Car is already stopped")
        else:
            started = False
            print("Car already stopped")
        print("Car has stopped")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
         """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that")