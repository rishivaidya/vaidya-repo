
# help -
# start - to start car
# stop - to stop the car
# quit - to terminate the program

command = ""
started = False
while True:
    command = input(">").lower()

    if command == "start":
        if started:
            print('Car is already running.')
        else:
            print('Car started.')
            started = True

    elif command == "stop":
        if started:
            print('Car stopped.')
        else:
            print('Car is already stopped')

    elif command == "help":
        print(""" 
        Start - to start the car
        Stop - to stop the car
        Quit - to quit """)

    elif command == 'quit':
        break

    else:
        print("Sorry, I don't understand that.")
