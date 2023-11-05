# Pyfuscator

This project contains a basic Python script that obfuscates Python code. It uses the `ast` and `astunparse` libraries to parse the Python code into an abstract syntax tree (AST), modify the AST, and then unparse it back into Python code. This is a basic version and will be updated with more features in the future.

## Features

- Variable and function name obfuscation: All variable and function names are replaced with random strings.
- String obfuscation: All string literals are encrypted.
- Control flow obfuscation: `If` and `For` statements are wrapped in additional control flow structures.
- Dead code injection: Dead code is injected into function definitions.

## Usage

1. Clone the repository.
2. Run the `obfuscator.py` script with the Python code file you want to obfuscate as the input.
3. The obfuscated code will be written to `obfuscated_main.py`.

## Dependencies

- `ast`
- `astunparse`
- `hashlib`
- `random`
- `string`
- `Crypto.Cipher`
- `Crypto.Random`
- `base64`

## Future Updates

This is a basic version of the obfuscator. Future updates will include more advanced obfuscation techniques and improved performance.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries, please open an issue on the GitHub repository.
