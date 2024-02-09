![Sample Image](/images/hbnb_photo.png)
# AirBnB Clone Project - The Console

### Project Description

The **AirBnB Clone - The Console** is the foundational component of the AirBnB Clone Project. It serves as a command-line interface (CLI) designed for managing AirBnB objects. This console represents the first crucial step in the development of a comprehensive web application, where users can perform essential operations on AirBnB objects.

### Console Features

#### Object Management

- **Creation:** Users can create new AirBnB objects using intuitive commands.
- **Retrieval:** Efficiently retrieve objects from files or databases for further processing.
- **Operations:** Conduct various operations on objects, such as counting and computing statistics.
- **Update:** Modify object attributes to keep information up-to-date.
- **Destruction:** Destroy unwanted objects to maintain a clean and organized dataset.

#### BaseModel Integration

The console integrates a parent class called `BaseModel` to streamline object initialization, serialization, and deserialization. This integration ensures consistency and efficiency in managing AirBnB objects.

### Getting Started

### Usage

Start the command interpreter:

./console.py

#### Use your console.py in interactive mode as usual:

$ ./console.py
(hbnb) help
Documented commands (type help <topic>):

=======================================

EOF  help  quit
(hbnb)


#### In non-interactive mode:

$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):

========================================

EOF  help  quit
(hbnb)

