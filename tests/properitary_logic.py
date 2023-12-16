from obfuscator import Obfuscator
from obfuscator import Supremebfuscator
import ast
obfuscator = Supremebfuscator()

# Create an ast.Str node with a string literal
string_node = ast.Str(s="Hello, world!")

# Apply the proprietary_logic method to the string node
encrypted_node = obfuscator.proprietary_logic(string_node)

print(encrypted_node.s)