Menu = {
    "sandwich": 350,
    "cofee": 35,
    "tee": 30,
    "pizza": 480,
    "burger": 380
}
total = 0
while True:
    user_input = input("Your Order : ")
    if user_input in Menu:
        price = Menu[user_input]
        total += price
        print(f"{user_input} costs is {price} total is {total} ")

    elif user_input not in Menu.keys():
        print("Sorry, we are fresh out of elephant today.")

    if user_input == (""):
        print("Exit")
        break
print(f"your total is {total}")

