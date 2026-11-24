MATRIX_STR = """
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%"""


# Step 1: Convert the matrix string into a 2D list (a list of rows).
# Each row becomes a list of characters so we can access items by [row][column].
matrix = [list(row) for row in MATRIX_STR.strip("\n").split("\n")]

# Step 2: Read the matrix column-wise (top to bottom, left to right).
# Use the longest row to avoid skipping characters when rows have different lengths.
decoded_message = ""
found_alpha = False
gap_between_alpha = False
num_columns = max(len(row) for row in matrix)

for col in range(num_columns):
    for row in range(len(matrix)):
        # Step 3: Filter characters while iterating through the matrix.
        # Only keep alphabetic characters; track non-alpha gaps between alpha groups.
        if col >= len(matrix[row]):
            continue

        char = matrix[row][col]
        if char.isalpha():
            # Insert a single space for a non-alpha gap found between alpha characters.
            if found_alpha and gap_between_alpha:
                decoded_message += " "
            decoded_message += char
            found_alpha = True
            gap_between_alpha = False
        else:
            if found_alpha:
                gap_between_alpha = True

# Step 4: Print the decoded secret message.
print(decoded_message)