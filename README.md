<p align="center">
  <img width="442" height="90" src="https://github.com/logtracing/node-pkg/assets/55886451/a605b6fd-14c8-4d0d-9cfa-c8f0742aa5ec">
</p>

<p align="center">Suite to manage and track errors in your application using your own resources.</p>

<p align="center">
  <img src="https://github.com/logtracing/node-pkg/actions/workflows/node.js.yml/badge.svg">
  <img src="https://img.shields.io/npm/v/@logtracing/node?color=blue">
  <img src="https://img.shields.io/npm/l/@logtracing/node?color=blue">
</p>

## Overview

**Logtracing** is a suite that allows you to track errors that occur in your applications. It also allows you to have full control of how and where to store all the collected information, this means that you need to have your own database where all the information will be stored.

Also, **Logtracing** provides a dashboard to monitoring your errors, but you can use or create your own monitoring dashboard.

Right now is available for the following tech stacks:
- JavaScript (NodeJS)
- Python (In Progress)

**What information does this suite track?**
- Error Stack
- Code lines of each function
- Environment variables
- SO Information

## :wrench: Configuration

### :open_file_folder: Creating your database
Before start using this suite, you need to have a MySQL database ready to be used (locally or in a server) and create the required tables.

You can find the migration SQL file here: [SQL for tables](https://github.com/logtracing/node-pkg/blob/main/prisma/migrations/20230621050013_init/migration.sql)

## Installation
You can install logtracing-python using pip:

    ./pip install logtracing-python --user

## Usage
To start tracking and logging errors in your Python application, follow these steps:

 1. Import the Tracer class from the logtracing module:
  ```python
  from logtracing import Tracer
  ```
 2. Create an instance of the Tracer class:
  ```python
  tracer = Tracer()
  ```
 3. Start logging errors by calling the log_error method on the tracer instance whenever an error occurs in your application:
  ```python
    try:
      # Your code here
    except Exception as e:
      tracer.log_error(e)
  ```

  The log_error method will log the error message, stack trace, and any other relevant information.

Customize the logging behavior (optional):

By default, logtracing-python logs errors to the console. If you want to customize the logging behavior, you can configure the logger used by the Tracer class. You can refer to the Python logging documentation for more information on how to configure the logger to suit your needs.

## Running the Tests
To run the tests for logtracing-python, follow these steps:

Clone the repository:

    git clone https://github.com/your-username/logtracing-python.git

Navigate to the project directory:

    cd logtracing-python

Install the required dependencies:

    pip install -r requirements.txt
Run the tests using pytest:

    pytest
The test suite will be executed, and the results will be displayed in the console.

## Contributing
Contributions are welcome! If you encounter any issues, have suggestions, or want to contribute to the project, please open an issue or submit a pull request on the GitHub repository.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

Feel free to update the placeholders like your-username with the appropriate information based on your GitHub username and project details.

