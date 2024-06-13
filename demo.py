# these is flask code for same project 

from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os
from PIL import Image
import google.generativeai as genai
import io

# Load environment variables from .env file
load_dotenv()

# Configure the generative AI library with the API key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("API key is missing. Please set the GOOGLE_API_KEY in your .env file.")
else:
    genai.configure(api_key=api_key)

app = Flask(__name__)

# Define the generative model
model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input_text, image_bytes):
    try:
        if image_bytes:
            if input_text:
                response = model.generate_content([input_text, image_bytes])
            else:
                response = model.generate_content(image_bytes)
        else:
            response = model.generate_content(input_text)
        return response['generated_text']
    except Exception as e:
        return f"Error generating content: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form.get('input')
        image_file = request.files.get('image')

        image_bytes = None
        if image_file:
            image = Image.open(image_file)
            buf = io.BytesIO()
            image.save(buf, format='JPEG')
            image_bytes = buf.getvalue()

        response = get_gemini_response(input_text, image_bytes)
        return jsonify({'response': response})

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
