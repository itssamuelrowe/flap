
import os
from app import create_app

configuration = os.getenv('FLASK_CONFIGURATION') or 'default'
app = create_app(configuration)

if __name__ == '__main__':
    app.run()
