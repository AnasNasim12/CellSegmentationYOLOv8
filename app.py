import requests
from flask import Flask,render_template,url_for
from flask import request as req


app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def Index():
    return render_template("index.html")
@app.route("/Summarize", methods=["GET", "POST"])
def Summarize():
    if req.method=="POST":
        headers = {"Authorization": f""}
        API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"
        
        data=req.form["data"]
        
        maxL = req.form.get("maxL")
        if maxL is not None:
            maxL = int(maxL)
            minL = maxL // 4
        else:
            # Handle the case when 'maxL' is not provided
            # For example, set a default value
            maxL = 100
            minL = maxL // 4
            minL=maxL//4
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs":data,
            "parameters":{"min_length":minL,"max_length":maxL},
        })[0]
        
        return render_template("index.html",result=output["summary_text"])
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
