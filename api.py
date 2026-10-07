from flask import Flask, request, jsonify, render_template
from agents.orchestrator import Orchestrator


app = Flask(__name__)


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/emergency", methods=["POST"])
def emergency():

    data = request.get_json()

    patient_request = data.get("patient_request")

    if not patient_request:

        return jsonify({
            "error": "patient_request is required"
        }), 400

    orchestrator = Orchestrator()

    result = orchestrator.start(
        patient_request
    )

    if result is None:

        return jsonify({
            "error": "Emergency workflow failed"
        }), 500

    return jsonify(result)


@app.route("/health")
def health():

    return jsonify({
        "status": "Emergency AI system is running"
    })


if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )