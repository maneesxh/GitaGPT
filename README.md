GitaGPT
Welcome to GitaGPT, a project that combines the timeless wisdom of the Bhagavad Gita with modern AI technology to provide insightful responses to your questions and challenges. This application allows users to interact with an AI chatbot inspired by Lord Krishna’s teachings, offering guidance for daily life through a user-friendly web interface.
Project Overview
GitaGPT is a full-stack application with:

A backend built using Python, leveraging a Hugging Face language model to generate responses based on the teachings of the Bhagavad Gita.
A frontend built with React, providing a simple and intuitive interface for users to input queries and receive responses.

Features

AI-Powered Responses: Uses a Hugging Face transformer model to generate answers inspired by the Bhagavad Gita.
User-Friendly Interface: A clean React-based frontend with a text area for input and a button to submit queries.
API Integration: The frontend communicates with the backend via a REST API to fetch AI-generated responses.

Project Structure
GitaGPT/
├── backend/
│   ├── app.py              # Backend server (Flask/FastAPI)
│   ├── requirements.txt    # Python dependencies
│   └── venv/              # Virtual environment (ignored by .gitignore)
├── frontend/
│   ├── public/            # Static assets (e.g., index.html, logos)
│   ├── src/               # React source code (App.js, index.js, index.css)
│   ├── node_modules/      # Node.js dependencies (ignored by .gitignore)
│   └── package.json       # Frontend dependencies
└── .gitignore             # Git ignore file

Setup Instructions
Prerequisites

Python 3.11+: For the backend.
Node.js 18+: For the frontend.
Git: To clone the repository.

Installation

Clone the Repository:
git clone https://github.com/maneesxh/GitaGPT.git
cd GitaGPT


Set Up the Backend:

Navigate to the backend directory:cd backend


Create and activate a virtual environment:python -m venv venv
source venv/Scripts/activate  # On Windows
# source venv/bin/activate  # On macOS/Linux


Install the dependencies:pip install -r requirements.txt


Run the backend server:python app.py

The backend will run on http://localhost:5000.


Set Up the Frontend:

Navigate to the frontend directory:cd ../frontend


Install the dependencies:npm install


Start the React development server:npm start

The frontend will run on http://localhost:3000.


Access the Application:

Open your browser and go to http://localhost:3000.
Enter a query in the text area and click the "Ask Gita" button to receive a response inspired by the Bhagavad Gita.



Libraries Used
Backend

Flask (or FastAPI): For the API server.
transformers (Hugging Face): To load and run the language model for generating responses.
Model: distilbert-base-uncased (or another Hugging Face model specified in app.py).


torch: For running the Hugging Face model (PyTorch backend).
requests: For handling API requests (if needed).

Frontend

React: For building the user interface.
axios: For making API calls to the backend.
Tailwind CSS: For styling the frontend (optional, if used in index.css).

Contributing
We welcome contributions to enhance GitaGPT! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Make your changes and commit them (git commit -m "Add your feature").
Push to your branch (git push origin feature/your-feature).
Open a pull request on GitHub.

Please ensure your code follows the project’s style guidelines and includes appropriate tests.

Feel free to contribute or raise issues!

---

## Author

Maneesh – [LinkedIn](https://www.linkedin.com/in/maneeshthota/) | thotamaneesh@gmail.com
