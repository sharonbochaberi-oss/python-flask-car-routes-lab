from flask import Flask

# Create the Flask application instance
app = Flask(__name__)

# List of valid car models in the fleet
existing_models = ["Corolla", "Civic", "Mustang", "Camry", "Tesla", "Crossroads"]


# Home route (default page)
@app.route('/')
def home():
    # Returns a welcome message when visiting the root URL
    return "Welcome to Flatiron Cars"


# Dynamic route that captures any car model from the URL
@app.route('/<model>')
def car_model(model):

    # Loop through each known car model in the fleet
    for car in existing_models:

        # Compare user input with stored model in a case-insensitive way
        if car.lower() == model.lower():

            # If a match is found, return success message using correct capitalization
            return f"Flatiron {car} is in our fleet!"

    # If no match is found, return failure message using original user input
    return f"No models called {model} exists in our catalog"


# Run the app only if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)