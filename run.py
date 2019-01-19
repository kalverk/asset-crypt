import os

from src.app import create_app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    env_name = os.getenv('FLASK_ENV') if os.getenv('FLASK_ENV') is not None else 'development'
    app = create_app(env_name)
    app.run(host='0.0.0.0', port=port)
