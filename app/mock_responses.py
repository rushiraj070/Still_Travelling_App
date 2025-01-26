# app/mock_responses.py
import json

def mock_openai_response(prompt, max_tokens=150):
    """
    Mocked function to simulate OpenAI's response.
    In real implementation, this would call the OpenAI API and return a response.
    For testing, we'll simulate a structured response.
    """
    # Simulated response structure for testing
    mock_response = {
        "name": "John Doe",
        "budget": 1500,
        "duration": 7,
        "destination": "Paris",
        "purpose": "Leisure",
        "preferences": "Nature, Museums",
        "dietary_preferences": "Vegetarian",
        "mobility_concerns": "None",
        "accommodation": "Mid-range",
    }
    
    # Return the response as a JSON string for testing
    return json.dumps(mock_response)
