import os

from src.app import create_app

if __name__ == '__main__':
    env_name = os.getenv('FLASK_ENV') if os.getenv('FLASK_ENV') is not None else 'development'
    app = create_app(env_name)
    app.run()