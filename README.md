# Pyfuscator: A Comprehensive Python Code Obfuscation Solution

Pyfuscator is an advanced Python code obfuscation tool, meticulously designed to provide an extra layer of security to your Python code. Utilizing the capabilities of `ast` and `astunparse` libraries, Pyfuscator parses Python code into an Abstract Syntax Tree (AST), modifies the AST, and subsequently unparses it back into Python code. With a commitment to continuous enhancement, Pyfuscator is your go-to solution for robust and reliable code obfuscation.

## Core Features

- **Sophisticated Variable and Function Name Obfuscation**: Pyfuscator intelligently replaces all variable and function names with randomized strings, significantly increasing the complexity of the original code.
- **Advanced String Obfuscation**: Pyfuscator encrypts all string literals, providing an additional layer of obfuscation.
- **Intricate Control Flow Obfuscation**: Pyfuscator intricately wraps `If` and `For` statements in additional control flow structures, further obfuscating the code logic.
- **Strategic Dead Code Injection**: Pyfuscator strategically injects dead code into function definitions, creating diversions for anyone attempting to decipher the code.

## Installation

1. Clone the Pyfuscator repository to your local machine using `git clone https://github.com/user319183/pyfuscator.git`.
2. Navigate to the cloned repository using `cd pyfuscator`.
3. If necessary, set up your environment. For example, you might use a virtual environment: `python3 -m venv env` and activate it with `source env/bin/activate`.

## Usage Guidelines

1. Execute the `obfuscator.py` script, providing the Python code file you wish to obfuscate as the input: `python obfuscator.py yourfile.py`.
2. The obfuscated code will be generated and saved to `obfuscated_main.py`.

**Disclaimer**: Pyfuscator is designed for use with Python 3.6 and later versions. It is currently in a development phase and may contain certain limitations in the obfuscation process. We are actively working on addressing these issues. Additionally, there are known issues with unit tests failing. We recommend using Pyfuscator in a testing environment until these issues are resolved. Your patience and understanding are appreciated.

## Dependencies

Pyfuscator is built upon the following Python libraries:

- `ast`
- `astunparse`
- `hashlib`
- `random`
- `string`
- `Crypto.Cipher`
- `Crypto.Random`
- `base64`

## Contributing

We welcome contributions from the community. If you wish to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes in your branch.
4. Submit a pull request with your changes.

Please ensure your code adheres to our coding standards and that the unit tests still pass before submitting your pull request.

## Future Roadmap

We are dedicated to the continuous improvement of Pyfuscator, with plans to incorporate more advanced obfuscation techniques and performance optimizations. Stay connected for future updates.

## Licensing

Pyfuscator is licensed under the MIT License. For more details, please refer to the LICENSE file in the repository.

## Support and Contact

For any inquiries, support requests, or feedback, please open an issue on the Pyfuscator GitHub repository. Our team is always ready to assist.
