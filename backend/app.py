from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = Flask(__name__)
CORS(app)

print("Device set to use cpu")
device = "cpu"

model_name = "yrajm1997/gita-text-generation-gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).to(device)

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")

    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    output = model.generate(
        **inputs,
        max_new_tokens=100,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.95
    )

    response_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(port=5000)
