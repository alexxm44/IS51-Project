#basic 10-digit phone number formatting
def phone_format(num):
    new_num = ("(" + num[:3] + ")" + num[3:6] + "-" + num[6:])
    return new_num

#if the supplied phone number is 11 digits add the coutry code +x
def long_phone_format(num):
    new_num = ("+" + num[:1] + "(" + num[1:4] + ")" + num[4:7] + "-" + num[7:])
    return new_num


with open('input_numbers.txt') as infile:
    lines = infile.readlines()
    infile.close()

with open('output_numbers.txt', 'w') as outfile:
    for i in range(len(lines)-1):
        string = str(lines[i])
        if len(string) == 11:
            current = phone_format(string)
            outfile.write(current)
        elif len(string) == 12:
            current = long_phone_format(string)
            outfile.write(current)
        else:
            outfile.write(f"The number supplied in line {i} of the input file is not in the correct format and "
                  f"has not been formatted. Replace this line with a manually formatted entry\n")

