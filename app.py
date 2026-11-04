from flask import Flask, render_template, request
import joblib
import os


app = Flask(__name__)


# ============================================================
# LOAD TRAINED MODEL
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(
    BASE_DIR,
    "model",
    "iris_model.pkl"
)

model = joblib.load(model_path)


# ============================================================
# HOME PAGE
# ============================================================

@app.route("/")
def home():
    return render_template("index.html")


# ============================================================
# PREDICTION
# ============================================================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Get values from HTML form
        sepal_length = float(request.form["sepal_length"])
        sepal_width = float(request.form["sepal_width"])
        petal_length = float(request.form["petal_length"])
        petal_width = float(request.form["petal_width"])


        # Prepare input
        input_data = [[
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        ]]


        # Prediction
        prediction = model.predict(input_data)[0]


        # Probability
        probabilities = model.predict_proba(input_data)[0]

        max_probability = max(probabilities)

        confidence = round(max_probability * 100, 2)


        return render_template(
            "result.html",
            prediction=prediction,
            confidence=confidence,
            sepal_length=sepal_length,
            sepal_width=sepal_width,
            petal_length=petal_length,
            petal_width=petal_width
        )


    except Exception as error:

        return f"""
        <h2>Prediction Error</h2>
        <p>{error}</p>
        <a href="/">Go Back</a>
        """


# ============================================================
# RUN FLASK
# ============================================================

if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )
