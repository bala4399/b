from flask import Flask

app=Flask(__name__)

print("app started")

@app.route("/",methods=["Get"])
def Helo():
    return "hello guys"

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)