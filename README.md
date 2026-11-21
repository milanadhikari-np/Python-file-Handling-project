# Python File Handling Project

A simple menu-driven **File Handling System built using Python** that allows users to create, read, update, and delete files through the command line.

This project demonstrates the practical implementation of Python's `pathlib` and `os` modules, file operations, functions, exception handling, and user input.

## Features

The application provides four main file-handling operations:

### 1. Create File
- Create a new file by specifying its name.
- Write content into the newly created file.
- Check whether a file already exists before creating it.

### 2. Read File
- Display the available files and folders.
- Select a file by entering its name.
- Read and display the complete contents of a file.

### 3. Update File
Provides three different options:
- **Rename File:** Change the existing file name.
- **Overwrite Content:** Replace the existing file content with new content.
- **Append Content:** Add new content without removing the existing content.

### 4. Delete File
- Delete an existing file using its name.
- Check whether the specified file exists before deletion.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| pathlib | File and directory path management |
| os | File deletion operations |
| Exception Handling | Handling runtime errors |
| Functions | Organizing program functionality |

## Project Structure

```text
Python-file-Handling-project/
│
├── main.py       # Main Python application
└── README.md     # Project documentation
```

## How to Run the Project

**Step 1: Clone the repository**

```bash
git clone https://github.com/milanadhikari-np/Python-file-Handling-project.git
```

**Step 2: Navigate to the project directory**

```bash
cd Python-file-Handling-project
```

**Step 3: Run the Python application**

```bash
python main.py
```

## Application Menu

When you execute the program, you will see the following menu:

```text
Press 1 for creating a file
Press 2 for reading a file
Press 3 for updating a file
Press 4 for deleting a file

Please tell your response:
```

Enter your preferred option to perform the corresponding file operation.

## Learning Outcomes

Through this project, I practiced and improved my understanding of:

- Python file handling (`open()`, `read()`, `write()`).
- Working with file paths using `pathlib`.
- Using the `os` module for file operations.
- Implementing functions and conditional statements.
- Handling exceptions using `try-except`.
- Understanding file creation, reading, updating, and deletion.

## Future Improvements

- Add a graphical user interface (GUI).
- Implement a continuous menu using a loop.
- Add input validation for user choices.
- Support directory creation and deletion.
- Improve file selection and error handling.

## Author

**Milan Adhikari**

GitHub: [@milanadhikari-np](https://github.com/milanadhikari-np)

---

*This project was developed as a Python programming practice project to strengthen my understanding of file handling and filesystem operations.*
