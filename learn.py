# ==============================================================================
# SECTION 1: INTRODUCTION TO COMMENTS AND EXECUTION RULES
# ==============================================================================
# Python uses the # symbol for comments. Comments are used to explain code 
# or to disable specific lines of code without deleting them [1-3].
# Python executes code from top to bottom [4]. 

# Rule: Python is case-sensitive. 'print' is correct; 'PRINT' will fail [5].
print("Starting the Python Master Script...") # Standard print function [6]

# Multiple commands can be on the one line if separated by a semicolon [5].
print("Syntax Rule 1: Order matters"); print("Syntax Rule 2: Case sensitivity")

# ==============================================================================
# SECTION 2: VARIABLES AND DATA TYPES
# ==============================================================================
# Variables act as containers for data that can change based on the user [7].
# Naming rules: Can contain letters and numbers but CANNOT start with a number [8].

user_name = "Abdelrahman"  # String data type [9, 10]
user_age = 25              # Integer data type (used for math) [11]
user_height = 1.75         # Floating point (decimal) [6]
is_qualified = True        # Boolean (True or False) [11]

# Python supports complex data structures which will be covered in depth later [12]:
skills_list = ["Python", "Java", "C++"]     # List [12]
settings_tuple = ("Dark Mode", "Auto-save") # Tuple [12]
user_profile = {"ID": 101, "Role": "Admin"} # Dictionary [12]

# Printing different types [6, 13]:
print("Name:", user_name)
print("Age:", user_age)
print("Qualified Status:", is_qualified)

# ==============================================================================
# SECTION 3: STRING FORMATTING AND ESCAPING
# ==============================================================================
# Strings can use single (') or double (") quotes interchangeably [14, 15].
text_one = 'Single quotes work.'
text_two = "Double quotes work too."

# Using backslash (\) for special purposes:
# 1. Escaping quotes: To include a quote inside a string of the same type [15, 16].
quote_fix = "He said, \"Python is powerful\" and it worked."
print(quote_fix)

# 2. Line continuation: Use \ to continue a single command on a new line [17].
long_statement = "This is a very long string that we are splitting " \
                 "across two lines for readability in the code."
print(long_statement)  # [18]  <--- FIXED: added '#' to make [18] a comment

# 3. Triple Quotes: For multi-line strings exactly as they appear [15, 19].
formatted_text = """
    This text preserves
    its own formatting
    and line breaks automatically.
"""
print(formatted_text)

# ==============================================================================
# SECTION 4: CONCATENATION (LINKING STRINGS)
# ==============================================================================
first = "Ahmed"
last = "Gamal"

# Method A: Using the + sign. This does NOT add a space automatically [20, 21].
full_name = first + last 
print("Full name (no space):", full_name)

# Adding a manual space with + [20].
full_name_spaced = first + " " + last
print("Full name (with space):", full_name_spaced)

# Method B: Using a comma in print(). This ADDS a space automatically [21].
print("User full name is:", first, last)

# IMPORTANT: You cannot concatenate a String and an Integer using '+' [22].
# print("Age: " + user_age) # This would cause an error.
print("Age:", user_age) # This is the safe way to print mixed types.

# ==============================================================================
# SECTION 5: STRING METHODS - CASE MANIPULATION
# ==============================================================================
# .upper() converts all characters to capitals [23, 24].
# .lower() converts all characters to lowercase [23, 24].

raw_email = "User_Account_Name@PROVIDER.Com"
print("Original Email:", raw_email)

# Standardizing an email for a database [24]:
clean_email = raw_email.lower()
print("Standardized (lower):", clean_email)

shouting = "please pay attention".upper()
print("Shouting:", shouting)

# ==============================================================================
# SECTION 6: STRING METHODS - SPLITTING (STRING TO LIST)
# ==============================================================================
# .split() divides a string into a list based on a separator [25].
sentence = "Python is a great language"
words = sentence.split() # Defaults to splitting by space [26]
print("Split sentence into list:", words)

# Splitting by a specific character [26]:
csv_data = "101,Ahmed,Cairo,Admin"
data_list = csv_data.split(",")
print("Parsed CSV Data:", data_list)

# Using maxsplit: Limits the number of splits [27].
# This splits only the first 2 occurrences of the dash.
serial_number = "99-88-77-66-55"
limited_split = serial_number.split("-", 2)
print("Limited Split (2):", limited_split)

# .rsplit(): Starts splitting from the right side [28].
right_split = serial_number.rsplit("-", 1)
print("Right-side Split (1):", right_split)

# ==============================================================================
# SECTION 7: FINAL WRAP-UP
# ==============================================================================
# Combining logic: Standardizing input and then parsing it.
input_data = "  New_User-Data-Record  "
cleaned_data = input_data.strip().upper() # Note: strip() is a common method, sources focus on case and split.
final_result = cleaned_data.split("-")

print("Final Processed Record:", final_result)
print("Program Execution Finished Successfully.") 
# ==============================================================================