input_file = open("input.txt", "r")
output_file = open("output.txt", "w")
for i, line in enumerate(input_file, 1):
    output_file.write("{}) {}".format(i, line))
input_file.close()
output_file.close()