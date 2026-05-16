from flask import Flask

# Initialize Flask app
app = Flask(__name__)

# Existing car models
existing_models = ["corolla", "civic", "mustang", "camry", "tesla"]


# Default route
@app.route('/')
def home():
    return "Welcome to Flatiron Cars"


# Dynamic route
@app.route('/<model>')
def car_model(model):

    # Convert input to lowercase
    model = model.lower()

    # Check if model exists
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"

    # Model not found
    return f"No models called {model} exists in our catalog"


# Run app
if __name__ == '__main__':
    app.run(debug=True)