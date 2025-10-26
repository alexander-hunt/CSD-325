# Alexander Hunt - October 26th 2025 -  Module 2.2
# The purpose of this code is to convert miles to kilometers.

def miles_to_kilometers(miles):
    return miles * 1.60934


def main():
    while True:
        try:
            miles = float(input("Enter the number of miles driven: "))
            if miles < 0:
                print("Miles cannot be negative. Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    kilometers = miles_to_kilometers(miles)
    print(f"\nYou entered: {miles:.2f} miles")
    print(f"That is equal to: {kilometers:.2f} kilometers")


if __name__ == "__main__":
    main()