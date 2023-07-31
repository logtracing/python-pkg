<p align="center">
  <img width="442" height="90" src="https://github.com/logtracing/node-pkg/assets/55886451/a605b6fd-14c8-4d0d-9cfa-c8f0742aa5ec">
</p>

<p align="center">The LogTracing Node.js package is a component of the comprehensive LogTracing suite, dedicated to facilitating error tracking and log management across various applications.</p>


<p align="center">
  <a href="https://github.com/logtracing/python-pkg/actions"><img src="https://github.com/logtracing/python-pkg/actions/workflows/python.yml/badge.svg"></a>
  <a href="https://pypi.org/project/logtracing-python/"><img src="https://img.shields.io/pypi/v/logtracing-python?color=blue"></a>
  <a href="https://github.com/logtracing/python-pkg/blob/main/LICENSE"><img src="https://img.shields.io/pypi/l/logtracing-python?color=blue"></a>
</p>

## :book: Configuration

### :open_file_folder: Creating your database
Before start using this suite, you need to have a MySQL database ready to be used (locally or on a server) and create the required tables.

You can find the migration SQL file here: [SQL for tables](https://github.com/logtracing/node-pkg/blob/main/database.sql)

## :wrench: Initial configuration
You can install logtracing-python using pip:

    ./pip install logtracing --user

Create a `.env` file and add the following properties with your own information, replace `[ENV]` with your environment (`DEV`, `TEST`, or `PROD`):
```properties
MYSQL_USERNAME_[ENV]=
MYSQL_PASSWORD_[ENV]=
MYSQL_DATABASE_[ENV]=
MYSQL_HOST_[ENV]=
MYSQL_PORT_[ENV]=
```
Load your `.env` file using the [python-dotenv module](https://pypi.org/project/python-dotenv/) at the very beginning of your code (before other code runs):
```python
import dotenv
dotenv.load_dotenv()

# or
from dotenv import load_dotenv
load_dotenv()
```

Import the package in your code:
```python
from logtracing import Logger, ExceptionLogger
```

### Usage
### `Logger`
You can write your own logs using the `Logger` class:
```python
from logtracing import Logger

my_logger = Logger('MY APP LOGGER')

trace = my_logger.trace('Example of a trace log message')
debug = my_logger.debug('Example of a debug log message')
info = my_logger.info('Example of an info log message')
warn = my_logger.warn('Example of a warn log message')
error = my_logger.error('Example of an error log message')
fatal = my_logger.fatal('Example of a fatal log message')
```

### `ExceptionLogger`
You can also track the exceptions in your code, to have a big picture of what happened when your application fails. Start tracking your errors:
```python
from logtracing import ExceptionLogger

ex_logger = ExceptionLogger('MY APP EXCEPTION LOGGER')

user = {
  'username': 'admin',
  'email': 'email@admin.com'
}

def foo():
    raise Exception('Foo Error')

def bar():
    foo()

# You can add extra information that could be useful to understand the error
ex_logger.add_extra('User information', {
    'user': user,
})

try:
    bar()
except Exception as err:
    ex_logger.add_extra('More information', 'Handled Error Message')

    # Start to track the error
    ex_logger.track_error(err)

    # When finished, call report() to send all the information to your DB
    ex_logger.report()
```

**After doing this, you'll have in your configured database all the information related to the error that you tracked.**

You'll find more examples in [this folder](https://github.com/logtracing/python-pkg/blob/main/examples).

## :arrow_down: Installation for development purposes
### Getting the code
Clone this project:
```bash
git clone git@github.com:logtracing/node-pkg.git
# Or 
# We recommend you change the name of the folder in your machine
git clone git@github.com:logtracing/node-pkg.git logtracing-nodejs
```

Install dependencies:
```bash
cd python-pkg && pip install -r requirements-dev.txt
```

Create a `.env` file and fill it with the missing information:
```bash
cp .env.example .env
```

Transpile TS files into JS files:
```bash
npm run build
```

Run the tests:
```bash
npm run test
```
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

### Configuring MySQL
This project uses `mysql` as a database provider, so it is important to have a database before starting to make changes.

We have a `docker-compose.yml` file that provides you with a database ready to use; you just need to execute:
```bash
docker compose up
```

Then, when the container is up, you can execute the migrations by running:
```bash
python migrate.py
```

## License
[MIT](https://github.com/logtracing/python-pkg/blob/main/LICENSE)
