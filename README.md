Expose required ENV variables

    export FLASK_ENV=development
    
Install the dependencies

    pipenv install
    
Run the example
    
    python run.py
    
Push to heroku

    git push heroku master
    
Endpoints

For encrypting

    POST /encrypt
    {
        file: FILE
        message: "Message to crypt in the file"
    }
    
    Response: crypted file
    
For decrypting

    POST /decrypt
    {
        file: FILE
    }
    
    Response:
    {
        message: "Message retrieved from the file"
    }