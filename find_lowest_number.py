import sys

input_filename = sys.argv[1]
output_filename = sys.argv[2]

number_found = False

with open(input_filename, 'r') as input_file:
    for line in input_file:
        if number_found == False:
            try:
                lowest_number = float(line)
                number_found = True
            except ValueError:
                break
        else:
            if float(line) < lowest_number:
                lowest_number = float(line)

with open(output_filename, 'w') as output_file:
    if number_found:
        if lowest_number.is_integer():
            output_file.write(f"{int(lowest_number)}\n")
        else:
            output_file.write(f"{lowest_number}\n")
    else:
        output_file.write("No numbers found in file\n")
