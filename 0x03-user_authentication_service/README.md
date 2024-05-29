# Declaring API Routes in a Flask App
In a Flask application, API routes are defined using the @app.route decorator. This decorator binds a URL endpoint to a function, which is called when a request to that URL is made.

Here's a basic example:


from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!")

if __name__ == '__main__':
    app.run(debug=True)

In this example:

The @app.route('/api/hello', methods=['GET']) line declares a route /api/hello that accepts GET requests.
The hello function is called when the /api/hello endpoint is accessed, and it returns a JSON response with a message.
# Getting and Setting Cookies
Setting Cookies
To set a cookie in a Flask response, use the set_cookie method of the response object.


from flask import Flask, jsonify, make_response

app = Flask(__name__)

@app.route('/set_cookie')
def set_cookie():
    response = make_response(jsonify(message="Cookie Set"))
    response.set_cookie('username', 'john_doe')
    return response

if __name__ == '__main__':
    app.run(debug=True)

In this example:

The set_cookie function creates a response object using make_response.
The response.set_cookie('username', 'john_doe') line sets a cookie named 'username' with the value 'john_doe'.

# Getting Cookies

To retrieve cookies from a request, use the request.cookies dictionary.


from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get_cookie')
def get_cookie():
    username = request.cookies.get('username')
    return jsonify(username=username)

if __name__ == '__main__':
    app.run(debug=True)
In this example:

The get_cookie function retrieves the value of the 'username' cookie from the request.
Retrieving Request Form Data
To retrieve form data sent in a POST request, use the request.form dictionary.


from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    email = request.form.get('email')
    return jsonify(username=username, email=email)

if __name__ == '__main__':
    app.run(debug=True)
In this example:

The submit function retrieves the 'username' and 'email' fields from the form data of a POST request.
Returning Various HTTP Status Codes
To return different HTTP status codes in a Flask response, you can pass the status code as an argument to the jsonify function or use the make_response function.

Using jsonify with a status code


from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/success')
def success():
    return jsonify(message="Success"), 200

@app.route('/not_found')
def not_found():
    return jsonify(error="Not Found"), 404

if __name__ == '__main__':
    app.run(debug=True)
In this example:

The success route returns a 200 OK status code.
The not_found route returns a 404 Not Found status code.
Using make_response


from flask import Flask, jsonify, make_response

app = Flask(__name__)

@app.route('/unauthorized')
def unauthorized():
    response = make_response(jsonify(error="Unauthorized"), 401)
    return response

if __name__ == '__main__':
    app.run(debug=True)
In this example:

The unauthorized route creates a response object with a 401 Unauthorized status code using make_response.

# Summary
Declaring API Routes: Use the @app.route decorator to define endpoints and HTTP methods.
Setting Cookies: Use the set_cookie method of the response object.
Getting Cookies: Access cookies from the request.cookies dictionary.
Retrieving Form Data: Use the request.form dictionary to get form fields.
Returning HTTP Status Codes: Use jsonify with a status code or make_response to return responses with specific status codes.