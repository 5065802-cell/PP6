from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("username")
        role = request.form.get("role") # Untrusted hidden field!
        return f"<h3>Logged in as: {user} | Role from hidden field: {role}</h3>"
    return '''
    <h2>Hidden Field Demo</h2>
    <form method="POST">
      Username: <input type="text" name="username" required><br><br>
      Password: <input type="password" name="password" required><br><br>
      <input type="hidden" name="role" value="user">
      <button type="submit">Login</button>
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
