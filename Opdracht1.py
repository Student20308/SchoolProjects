# When askig for the input, we don't check if the input is the correct DataType or a CorrectValue.

# Style class for text formatting
class style:
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    END = '\033[0m'

# variable that ask input from the user
first_name = input("What is your first name? \n>").capitalize()                 # Ask for first name, the first letter is capitalized using .capitalize()
second_name = input("What is your second name? \n>").title()                    # Ask for second name, the first letter is capitalized using .title()
age = input("How old are you? \n>")                                             # Ask for age
adress_city = input("In what city do you live? \n>").title()                    # Ask for city, the first letter is capitalized using .title()
adress_street_name = input("On what street do you live? \n>").title()           # Ask for street name, the first letter is capitalized using .title()
adress_number = input("On what number do you live? \n>")                        # Ask for street number

# We format the text using f-strings and the style class
message = (
    f"Welcome {first_name} {second_name}!\n"
    f"You are {age} years old.\n"
    f"You live at:\n"
    f"- City: {style.ITALIC + adress_city + style.END}\n"
    f"- Street: {adress_street_name}\n"
    f"- Number: {style.BOLD + adress_number + style.END}"
)

# Print the message
print(message)