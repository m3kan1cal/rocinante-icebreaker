from flask import Flask, render_template, request, jsonify

from ice_breaker import break_ice

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    name_of_person = request.form["name_of_person"]
    person_info, profile_pic_url = break_ice(name_of_person=name_of_person)

    return jsonify(
        {
            "summary": person_info.summary,
            "interests": person_info.topics_of_interest,
            "facts": person_info.facts,
            "ice_breakers": person_info.ice_breakers,
            "picture_url": profile_pic_url,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
