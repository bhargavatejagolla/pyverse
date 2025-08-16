
# Password Generator 

## Overview
A simple Python script that generates secure random passwords of customizable length. The generator creates passwords using a combination of lowercase letters, uppercase letters, digits, and punctuation characters.

## Features 
- Generates strong, random passwords
- Customizable password length
- Includes all major character types for security:
  - Lowercase letters (a-z)
  - Uppercase letters (A-Z)
  - Digits (0-9)
  - Punctuation/special characters
- Simple command-line interface

## How to Use 
1. Run the Python script
2. When prompted, enter the desired length for your password
3. The program will generate and display a secure random password
4. Copy the generated password for your use

## Code Structure 
```python
import random
import string

# Character pool containing all possible characters
char_pool = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

# Get password length from user
password_length = int(input("Enter password length: "))

# Generate password
password = "".join(random.choice(char_pool) for _ in range(password_length))

print("Your random password is:", password)
```
## Requirements
- Python 3.x

- random module (included in Python standard library)

- string module (included in Python standard library)
## Installation & Usage 
# Clone the repository (if applicable)
git clone https://github.com/bhargavatejagolla/password-generator.git


## Run the script
python password_generator.py
## Example Output
<pre>
Enter password length: 12
Your random password is: 7x$Kq9@Lp2!Y
</pre>
## Security Considerations
- The generated passwords are cryptographically strong (using random.choice)

- For highly sensitive applications, consider using secrets module instead of random

- Always store generated passwords securely

- Never share generated passwords through insecure channels
## License
## License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for full details.
---
**Golla Bhargava Teja**  

* 🌐 [LinkedIn](https://www.linkedin.com/in/golla-bhargava-teja/)  
* 💻 [GitHub](https://github.com/bhargavatejagolla)
