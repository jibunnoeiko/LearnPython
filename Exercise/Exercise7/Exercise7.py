# String Error Syntax

# 1. Enter a valid string: bookstore = 'City Lights'

# 2. Now enter an invalid string:
# bookstore = 'City Lights"
# You should get the following output: Figure 1.7: Output with invalid string
# format
# If you start with a single quote, you must end with a single quote. Since
# the string has not been completed, you receive a syntax error.

# 3. Now you need to enter a valid string format again, as in the following
# code snippet: bookstore = "Moe's"
# This is okay. The string starts and ends with double quotes. Anything can be
# inside the quotation marks, except for more quotation marks.

# 4. Now add the invalid string again: bookstore = 'Moe's'
# ------------------------------------------------------------------------------

# 1
bookstore = 'City Lights' # => Okay

# 2
# bookstore = 'City Lights" => SyntaxError: EOL while scanning string literal

# 3
bookstore = 'Moe\'s' # => Okay

# 4
# bookstore = 'Moe's'  => SyntaxError: invalid syntax
