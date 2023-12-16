# Pyfuscator: A Comprehensive Python Code Obfuscation Solution

Pyfuscator is an advanced Python code obfuscation tool, meticulously designed to provide an extra layer of security to your Python code. Utilizing the capabilities of `ast` and `astunparse` libraries, Pyfuscator parses Python code into an Abstract Syntax Tree (AST), modifies the AST, and subsequently unparses it back into Python code. With a commitment to continuous enhancement, Pyfuscator is your go-to solution for robust and reliable code obfuscation.

## Why Choose Pyfuscator?

- **User-Friendly**: Pyfuscator is designed with a user-friendly interface, making it easy for developers of all skill levels to use.
- **Highly Secure**: Pyfuscator provides the most secure obfuscation available for free, protecting your Python code from reverse engineering.
- **Frequent Updates**: Pyfuscator is actively maintained and updated frequently, ensuring you always have access to the latest obfuscation techniques and improvements.
- **Free and Open Source**: Pyfuscator is free to use and open source, making it accessible to everyone.

## Core Features

- **Sophisticated Variable and Function Name Obfuscation**: Pyfuscator intelligently replaces all variable and function names with randomized strings, significantly increasing the complexity of the original code.
- **Advanced String Obfuscation with Custom Cryptography**: Pyfuscator encrypts all string literals using a custom encryption algorithm, providing an additional layer of obfuscation.
- **Intricate Control Flow Obfuscation**: Pyfuscator intricately wraps `If` and `For` statements in additional control flow structures, further obfuscating the code logic.
- **Strategic Dead Code Injection**: Pyfuscator strategically injects dead code into function definitions, creating diversions for anyone attempting to decipher the code.
- **Advanced Anti-Debugging**: Pyfuscator now includes an anti-debugging feature, which makes it harder for others to reverse engineer your code by using a debugger. This feature uses various techniques to detect the presence of a debugger and alters the program's behavior to thwart debugging attempts. This feature is implemented in the [`generate_anti_debugger_code`](obfuscator.py) function in the [`obfuscator.py`](obfuscator.py) file.
- **Opaque Predicates Obfuscation**: Pyfuscator includes a feature for obfuscating code with opaque predicates. This feature adds an additional layer of complexity to the obfuscated code, making it harder for others to understand the original logic.
- **Encrypted Strings Obfuscation with Custom Cryptography**: Pyfuscator includes a feature for obfuscating code with encrypted strings using a custom encryption algorithm. This feature adds an additional layer of complexity to the obfuscated code, making it harder for others to understand the original logic.
- **Anti-Memory Dumping**: Pyfuscator now includes an anti-memory dumping feature, which prevents other programs from creating a memory dump of your Python process. This feature is implemented in the `main` function in the [`obfuscator.py`](obfuscator.py) file.
- **Support for Latest Python Versions**: Pyfuscator has been updated to support the latest Python versions. For instance, the `ast.Str` has been replaced with `ast.Constant` to be compatible with Python 3.14 and later.
- **Enhanced Logging**: Pyfuscator now includes enhanced logging capabilities, providing more detailed and useful information about the obfuscation process. This feature is implemented in the [`modules.console`](modules/console.py) file.
- **Anti-Virtual Machine (VM) Techniques**: Pyfuscator now includes anti-VM techniques, which detect if the code is being run inside a virtual machine and alters the program's behavior to thwart reverse engineering attempts. This feature is implemented in the `main` function in the [`obfuscator.py`](obfuscator.py) file.

## Installation

1. Clone the Pyfuscator repository to your local machine using `git clone https://github.com/user319183/pyfuscator.git`.
2. Navigate to the cloned repository using `cd pyfuscator`.
3. If necessary, set up your environment. For example, you might use a virtual environment: `python3 -m venv env` and activate it with `source env/bin/activate`.

## Usage Guidelines

1. Execute the `obfuscator.py` script, providing the Python code you wish to obfuscate in `main.py`: `python obfuscator.py`.
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