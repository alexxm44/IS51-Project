# basic 10-digit phone number formatting
def phone_format(num):
    num = num.rstrip()
    new_num = ("(" + num[:3] + ")" + num[3:6] + "-" + num[6:])
    return new_num


# if the supplied phone number is 11 digits add the country code +x
def long_phone_format(num):
    num = num.rstrip()
    new_num = ("+" + num[:1] + "(" + num[1:4] + ")" + num[4:7] + "-" + num[7:])
    return new_num


# format data given in a .txt file
def format_from_file():
    with open('input_numbers.txt') as infile:
        lines = infile.readlines()
        infile.close()

    with open('output_numbers.txt', 'w') as outfile:
        for i in range(len(lines)):
            string = str(lines[i])
            if len(string) == 11:
                current = phone_format(string)
                outfile.write(current + "\n")
            elif len(string) == 12:
                current = long_phone_format(string)
                outfile.write(current + "\n")
            else:
                outfile.write(f"The number supplied in line {i} of the input file is not in the correct format and "
                              f"has not been formatted. Replace this line with a manually formatted entry\n")
        print("All numbers have been formatted... Printing to file")


# format data provided by the user
def format_from_user():
    with open('output_numbers.txt', 'w') as outfile:
        numbers = []
        print("begin entering numbers. Type DONE when you are finished")
        for i in range(100):
            entry = input()
            if entry == "done" or entry == "DONE" or entry == "Done":
                break
            numbers.append(entry)
        print("done entering numbers... now formatting and printing to output file")

        for i in range(len(numbers)):
            string = str(numbers[i])
            if len(string) == 10:
                current = phone_format(string)
                outfile.write(current + '\n')
            elif len(string) == 11:
                current = long_phone_format(string)
                outfile.write(current + '\n')
            else:
                outfile.write(f"The number supplied in entry {i + 1} is not in the correct format and "
                              f"has not been formatted. Replace this line with a manually formatted entry\n")

        print("formatting completed")


# Kickstart the program
def main():
    print("This program formats 10 and 11 digit strings to a phone number with a country code if applicable\n\n\n")
    choice = input("Do you want to read from a file or input the numbers manually (type read/input)\n")

    if choice == "read" or choice == "Read":
        format_from_file()

    if choice == "input" or choice == "Input":
        format_from_user()


main()
