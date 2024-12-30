import sys
import os

current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(current_dir)
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)