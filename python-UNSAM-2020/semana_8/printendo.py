# print('''table {
#   font-family: arial, sans-serif;
#   border-collapse: collapse;
#   width: 100%;
# }

# td, th {
#   border: 1px solid #dddddd;
#   text-align: left;
#   padding: 8px;
# }

# tr:nth-child(even) {
#   background-color: #dddddd;
# }''')

import sys

print('This message will be displayed on the screen.')

original_stdout = sys.stdout  # Save a reference to the original standard output
print(str(original_stdout))

with open('filename.txt', 'w') as f:
    sys.stdout = f  # Change the standard output to the file we created.
    print(str(sys.stdout))
    print('This message will be written to a file.')
    sys.stdout = original_stdout  # Reset the standard output to its original value
