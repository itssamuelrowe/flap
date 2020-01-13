# Flap

Flap is a simple utility for bootstrapping Flask projects. In other words, it
is the poor mans equivalent of Create React App for Flask. It requires no
configuration. Further, you are free to customize the script however you see fit.

## Quick Overview

```
python3 flap.py hello
cd hello
./run
```

Flap generates the following layout:
```
hello
|   .gitignore
|   configuration.py
|   manage.py
|   README.md
|   requirements.txt
|   run
|   
+---app
|   |   __init__.py
|   |   
|   +---main
|   |       views.py
|   |       __init__.py
|   |       
|   +---static
|   \---templates
+---migrations
+---tests
\---venv
```

As of this version, Flap supports only Python 3 and Linux. I have personally
tested it on WSL running Ubuntu.

Flap requires Python 3, Pip, and virtualenv. New projects are preconfigured
to use a virtual environment, with Flask installed via Pip, which means you can
focus on coding rather than setting up your project.

Create a project, and you are good to go.

## Contributing

We welcome all contributors.

Flap was created with a vision to help programmers, like you and I, write code
better. With your contributions, we can get there sooner. We appreciate your help!

To contribute, please contact the original author Samuel Rowe (<samuelrowe1999@gmail.com>).

## License

Copyright 2020 Samuel Rowe

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
