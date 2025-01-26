import json
import streamlit as st
from .mock_responses import mock_openai_response

def get_user_input():
    """
    Collects user input via Streamlit widgets.
    """
    user_input = {
        "name": st.text_input("What's your name?"),
        "budget": st.number_input("What's your budget?", min_value=1),
        "duration": st.number_input("How many days is your trip?", min_value=1, step=1),
        "destination": st.text_input("Where are you going?"),
        "purpose": st.text_input("Why are you traveling?"),
        "preferences": st.text_area("Any specific preferences?"),
        "dietary_preferences": st.selectbox("Dietary preferences:", ["No restrictions", "Vegetarian", "Vegan", "Gluten-free"]),
        "mobility_concerns": st.selectbox("Mobility concerns:", ["None", "Yes"]),
        "accommodation": st.selectbox("Accommodation type:", ["Budget", "Mid-range", "Luxury"])
    }
    
    return user_input

def refine_user_input(user_context):
    """
    Refines user inputs by asking clarifying questions.
    """
    refined_context = {
        "name": user_context["name"],
        "budget": user_context["budget"],
        "duration": user_context["duration"],
        "destination": user_context["destination"],
        "purpose": user_context["purpose"],
        "preferences": user_context["preferences"],
        "dietary_preferences": user_context["dietary_preferences"],
        "mobility_concerns": user_context["mobility_concerns"],
        "accommodation": user_context["accommodation"]
    }
    return refined_context
