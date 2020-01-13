# Copyright 2020 Samuel Rowe
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import subprocess
import sys

configuration = {
    'virtualEnvironmentName' : 'venv',
    'pythonVersion' : 'python3'
}

GIT_IGNORE_CONTENT = \
'''
venv/

*.pyc
__pycache__/

instance/

.pytest_cache/
.coverage
htmlcov/

dist/
build/
*.egg-info/
'''

RUN_CONTENT = \
'''
python manage.py
# Alternatively
# flask run --extra-files app
'''

CONFIGURATION_CONTENT = \
'''
import os

class Configuration:
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY') or 'EwORLeuMAS503519MANaYDAmAKHsUNaIAS'

class DevelopmentConfiguration(Configuration):

    DEBUG = True

    MAIL_SERVER = os.environ.get('FLASK_MAIL_SERVER_DEV')

    MAIL_PORT = os.environ.get('FLASK_MAIL_SERVER_DEV')

    MAIL_USE_TLS = True

    MAIL_USE_SSL = False

    MAIL_USERNAME = os.environ.get('FLASK_MAIL_USERNAME_DEV')

    MAIL_PASSWORD = os.environ.get('FLASK_MAIL_PASSWORD_DEV')

    DATABASE_URI = os.environ.get('FLASK_DATABASE_URI_DEV')

class TestConfiguration(Configuration):
    TEST = True

    MAIL_SERVER = os.environ.get('FLASK_MAIL_SERVER_TEST')

    MAIL_PORT = os.environ.get('FLASK_MAIL_SERVER_TEST')

    MAIL_USE_TLS = True

    MAIL_USE_SSL = False

    MAIL_USERNAME = os.environ.get('FLASK_MAIL_USERNAME_TEST')

    MAIL_PASSWORD = os.environ.get('FLASK_MAIL_PASSWORD_TEST')

    DATABASE_URI = os.environ.get('FLASK_DATABASE_URI_TEST')

class ProductionConfiguration(Configuration):

    PRODUCTION = True

    MAIL_SERVER = os.environ.get('FLASK_MAIL_SERVER_PRODUCTION')

    MAIL_PORT = os.environ.get('FLASK_MAIL_SERVER_PRODUCTION')

    MAIL_USE_TLS = True

    MAIL_USE_SSL = False

    MAIL_USERNAME = os.environ.get('FLASK_MAIL_USERNAME_PRODUCTION')

    MAIL_PASSWORD = os.environ.get('FLASK_MAIL_PASSWORD_PRODUCTION')

    DATABASE_URI = os.environ.get('FLASK_DATABASE_URI_PRODUCTION')

configuration = {
    'development': DevelopmentConfiguration,
    'test': TestConfiguration,
    'production': ProductionConfiguration,
    'default': DevelopmentConfiguration
}
'''

MANAGE_CONTENT = \
'''
import os
from app import create_app

configuration = os.getenv('FLASK_CONFIGURATION') or 'default'
app = create_app(configuration)

if __name__ == '__main__':
    app.run()
'''

README_CONTENT = \
'''
This project was bootstrapped using Flap.
Click [here](https://www.github.com/itssamuelrowe/flap) to learn more about Flap.

### Run
To run the development server execute the following command in your terminal.

```
./run
```

Open [http://localhost:5000/index](http://localhost:5000/index) in your browser
to see the server in action.
'''

APP_INIT_CONTENT = \
'''
import os
from flask import Flask
from configuration import configuration

def create_app(config_name='default'):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(configuration[config_name])

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
'''

APP_MAIN_INIT_CONTENT = \
'''
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views
'''

APP_MAIN_VIEWS_CONTENT = \
'''
from . import main

@main.route('/index')
def index():
    return 'Hello, world!'
'''

directories = [
    './migrations',
    './app',
    './app/main',
    './app/static',
    './app/templates',
    './tests',
]

files = [
    { 'name' : './.gitignore', 'content' : GIT_IGNORE_CONTENT },
    { 'name' : './configuration.py', 'content' : CONFIGURATION_CONTENT },
    { 'name' : './manage.py', 'content' : MANAGE_CONTENT },
    { 'name' : './run', 'content' : RUN_CONTENT },
    { 'name' : './README.md', 'content' : README_CONTENT },
    { 'name' : './app/__init__.py', 'content' : APP_INIT_CONTENT },
    { 'name' : './app/main/__init__.py', 'content' : APP_MAIN_INIT_CONTENT },
    { 'name' : './app/main/views.py', 'content' : APP_MAIN_VIEWS_CONTENT }
]

def install_virtual_environment():
    virtualEnvironmentName = configuration['virtualEnvironmentName']
    pythonVersion = configuration['pythonVersion']

    print(f'Installing virtual environment \'{virtualEnvironmentName}\'...')
    os.system(f'virtualenv -p {pythonVersion} {virtualEnvironmentName}')

def install_flask():
    virtualEnvironmentName = configuration['virtualEnvironmentName']
    print('Installing flask...')
    os.system(f'./{virtualEnvironmentName}/bin/python -m pip install flask')

def create_directories():
    for directory in directories:
        print(f'Creating directory \'{ directory }\'...')
        os.makedirs(directory)
        # print(f'Successfully created directory \'{ directory }\'')

def create_files():
    for file in files:
        name = file['name']
        content = file['content']
        print(f'Writing \'{ name }\'...')
        output = open(name, 'a+')
        output.write(content)
        # print(f'Successfully generated \'{ name }\'')

def generate_requirements():
    virtualEnvironmentName = configuration['virtualEnvironmentName']
    print(f'Extracing requirements...')
    os.system(f'./{virtualEnvironmentName}/bin/python -m pip freeze > requirements.txt')

def show_tips():
    virtualEnvironmentName = configuration['virtualEnvironmentName']
    print('Successfully bootstrapped!')
    print('Activate your virtual environment using the following command:')
    print(f'source {virtualEnvironmentName}/bin/activate')
    print('Happy hacking!')

def initialize_project():
    projectName = configuration['projectName']
    print(f'Creating project {projectName}...')
    os.makedirs(projectName)
    os.chdir(projectName)

def main():
    if len(sys.argv) != 2:
        print('[error] The specified number of arguments is invalid.')
        print('python3 flap.py [project_name]')
    else:
        configuration['projectName'] = sys.argv[1]
        
        initialize_project()
        
        install_virtual_environment()
        install_flask()
        create_directories()
        create_files()
        generate_requirements()
        show_tips()

if __name__ == '__main__':
    main()