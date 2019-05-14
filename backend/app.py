from flask import Flask,render_template,jsonify,make_response
app= Flask(__name__)

@app.route("/api/pokemon",methods=["GET"])
def json():
    response_body = {
        "pokemon": [
            "bulbasaur", 
            "charmander", 
            "squirtle"  
        ]
    }
    res = make_response(jsonify(response_body), 200)
    return res

if __name__ == '__main__':
    app.run(host='localhost', port=8006, debug=True)
