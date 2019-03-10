
from flaskitemscatalog import app

if __name__ == "__main__":
    # super secure key for flash messaging
    app.secret_key = "super secret key"
    # debug mode
    app.debug = True
    app.run(host="127.0.0.1", port=8000)
    
