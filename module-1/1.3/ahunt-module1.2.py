##Alexander Hunt - October 26th, 2025 - Advanced Python - Module 1.3 Assignment
#The purpose of this code is to sing the beer song

#sing song method
def sing_beer_song(bottles):
    while bottles > 0:
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down, pass it around, {bottles - 1} bottle{'s' if bottles - 1 != 1 else ''} of beer on the wall.\n")
        else:
            print(f"1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall.\n")
        bottles -= 1
    print("Time to buy more beer!")

#invoke method
try:
    num_bottles = int(input("How many bottles of beer are on the wall? "))
    if num_bottles > 0:
        sing_beer_song(num_bottles)
    else:
        print("You need at least one bottle to start the song.")
except ValueError:
    print("Please enter a valid number.")
