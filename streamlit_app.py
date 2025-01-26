import streamlit as st
from app.input_refinement import get_user_input, refine_user_input
from app.itinerary_generation import generate_itinerary

# Streamlit app
def main():
    st.title("Personalized Travel Planner")

    # Get user input via Streamlit widgets
    user_context = get_user_input()

    # Button to refine input and generate itinerary
    if st.button("Generate Itinerary"):
        if all(user_context.values()):
            # Refine user input based on initial details
            refined_context = refine_user_input(user_context)

            # Define activities (mock data, can be dynamic in the future)
            activities = [
                "Visit the Louvre Museum",
                "Explore the Eiffel Tower",
                "Stroll through Luxembourg Gardens",
                "Take a Seine river cruise"
            ]

            # Generate the itinerary
            itinerary = generate_itinerary(refined_context, activities)

            # Display the refined user context and generated itinerary
            st.write("Refined User Details:")
            st.json(refined_context)

            st.write("Generated Itinerary:")
            st.text(itinerary)

        else:
            st.warning("Please fill in all the fields!")

if __name__ == "__main__":
    main()
