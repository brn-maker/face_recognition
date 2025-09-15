from flask import Flask, render_template, request, jsonify
import requests
import base64

app = Flask(__name__)

DEEPSEEK_API_KEY = "enter API key here"
DEEPSEEK_URL = "https://api.deepseek.com/face/verify"  # Example endpoint (check actual docs)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verify', methods=['POST'])
def verify_face():
    data = request.json
    image_data = data.get("image")

    # Send the image to DeepSeek for verification (this assumes you have a reference image)
    response = requests.post(
        DEEPSEEK_URL,
        headers={"Authorization": f"Bearer {DEEPSEEK_API_KEY}", "Content-Type": "application/json"},
        json={
            "image1": image_data,   # captured image
            "image2": "base64_of_reference_image"  # replace with saved user face
        }
    )

    if response.status_code == 200:
        result = response.json()
        return jsonify(result)
    else:
        return jsonify({"error": "DeepSeek request failed"}), 500

if __name__ == "__main__":
    from os import getenv
    app.run(host="0.0.0.0", port=int(getenv("PORT", 5000)))

