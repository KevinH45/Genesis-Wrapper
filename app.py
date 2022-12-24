from flask import Flask, request, jsonify
from extensions import driver
from WebDriverUtils import get_grades
app = Flask("dasofihj")

@app.route("/grades")
def grades():
    try:
        data = get_grades(request.args.get("username"), request.args.get("password"))
    except KeyError:
        return {"msg": "Query string is wrong"}, 403
    return jsonify(data), 200

app.run()