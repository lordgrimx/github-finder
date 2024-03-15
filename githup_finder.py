from flask import Flask,render_template,request
import requests


app = Flask(__name__)

BASE_URL = "https://api.github.com/users/"
@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        git_name = request.form.get("githubname")
        response = requests.get(BASE_URL + git_name)
        repos = requests.get(BASE_URL + git_name + "/repos")
        repos_info = repos.json()
        user_info = response.json()
        return render_template("index.html",profile = user_info,repos=repos_info)
    else:
        return render_template("index.html")
    

if __name__ == "__main__":
    app.run(debug=True)