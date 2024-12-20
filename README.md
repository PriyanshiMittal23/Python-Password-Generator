# Python-Password-Generator

A simple Python application for generating secure, random passwords with customizable length and repetition options. This tool uses the `tkinter` library for the graphical user interface (GUI) and Python's `random` module to generate passwords.

## Features

- Generate random passwords with specified lengths.
- Option to choose between passwords with or without character repetition.
- Easy-to-use graphical user interface (GUI) built with `tkinter`.
- Password contains a mix of upper and lowercase letters, digits, and special characters.
  
## Prerequisites

- Python 3.x
- `tkinter` (usually comes pre-installed with Python)

## Installation

1. **Clone the Repository**:
   Clone the project to your local machine using Git:
   ```bash
   git clone https://github.com/PriyanshiMittal23/Python-Password-Generator.git

2. **Set Up the Virtual Environment (Optional)**:
   It's recommended to use a virtual environment to manage dependencies.
   ```bash
   cd Python-Password-Generator
   python -m venv myenv

3. **Activate the Virtual Environment**:
   For Windows:
       myenv\Scripts\activate
  
   For Mac/Linux:
       source myenv/bin/activate

4. **Install Dependencies**:
   The project doesn't require external dependencies apart from tkinter, which should already be included with Python. If you want to install additional libraries or     dependencies, you can create a requirements.txt file.

   However, if you're using a custom environment or want to list specific dependencies, you can do:

   ```bash
   pip install -r requirements.txt

5. **Run the Program**:
   After setting up the environment, run the program by executing the following:
   ```bash
   python passwordgenerator.py

## Usage

After running the application, you will see the Password Generator GUI window. Here's how to use it:

### 1. Enter Password Length
- In the **"Enter length of password"** field, enter the desired length for the generated password. The length should be a number (e.g., 8, 12, 16, etc.).

### 2. Choose Repetition Option
- In the **"Repetition?"** field, you need to choose:
  - **1**: No repetition of characters. Each character in the password will be unique.
  - **2**: Repetition allowed. Characters can repeat in the generated password.

### 3. Generate the Password
- After entering the password length and choosing the repetition option, click the **"Generate Password"** button.
- The generated password will appear below the button, showing the result in the form **"Generated Password: <password>"**.

### Example
If you want to generate a 12-character password with allowed repetition, the fields will look like this:
- **Password length**: 12
- **Repetition**: 2 (Repetition allowed)
Click on **"Generate Password"**, and the password will appear below.
