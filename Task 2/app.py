from flask import Flask, render_template, request, jsonify
from detector import classify_answer

app = Flask(__name__)

# Home Page
@app.route("/", methods=["GET", "POST"])
def home():

    result = ""
    user_answer = ""

    if request.method == "POST":

        user_answer = request.form["answer"]

        result = classify_answer(user_answer)
        
        # Display Result in Terminal
        print("\n===== Detection Result =====")

        print(f"User Answer: {user_answer}")

        print(f"Classification: {result}")

        print("--------------------------------")

    return render_template(
        "index.html",
        result=result,
        answer=user_answer
    )

# API Endpoint
@app.route("/detect", methods=["POST"])
def detect():

    data = request.json

    answer = data["answer"]

    result = classify_answer(answer)

    # Display API result in terminal
    print("\n===== API Detection Result =====")

    print(f"User Answer: {answer}")

    print(f"Classification: {result}")

    print("--------------------------------")

    return jsonify({
        "classification": result
    })

# Run Flask App
if __name__ == "__main__":

    print("\nInvalid Answer Detection Server Running...")

    app.run(debug=False)