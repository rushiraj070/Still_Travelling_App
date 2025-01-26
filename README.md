# **Personalized Travel Itinerary Generator**

This project is a **Personalized Travel Itinerary Generator** that creates a custom travel plan based on user inputs. By gathering information such as budget, destination, duration, dietary preferences, mobility concerns, and accommodation preferences, it generates a detailed itinerary with suggested activities, dining options, and more, tailored to the user's needs and interests.

### **Features**
- **Interactive User Input**: Users are prompted to provide essential details about their trip.
- **Input Refinement**: The app refines user inputs to ask additional questions regarding preferences, dietary restrictions, mobility concerns, and accommodation choices.
- **Personalized Itinerary Generation**: Generates a complete day-by-day itinerary based on user details, including activity suggestions and dining options.
- **Streamlit-based Web Application**: The app is developed using Streamlit, making it easily accessible through a web interface.

### **Tech Stack**
- **Python**
- **Streamlit**
- **OpenAI API (Mocked for Testing)**
- **JSON for Data Structuring**

### **Installation Instructions**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/rushiraj070/Still_Travelling_App.git
   cd Still_Travelling_App
   ```

2. **Install Dependencies**
   Make sure you have Python 3.x installed. Then, install the necessary Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit Application**
   Start the Streamlit app by running the following command:
   ```bash
   streamlit run streamlit_app.py
   ```

4. **Access the Application**
   Once the app is running, open the provided URL in your web browser (usually `http://localhost:8501`).

### **How the Application Works**
1. **User Input**: The app asks users for details about their trip, such as:
   - Name
   - Budget (low, moderate, luxury)
   - Trip Duration (in days)
   - Destination
   - Purpose of travel (e.g., leisure, business)
   - Specific preferences (e.g., nature, museums, adventure)
   - Dietary preferences (e.g., vegetarian, vegan)
   - Mobility concerns (e.g., difficulty walking, wheelchair accessibility)
   - Accommodation preferences (e.g., budget, mid-range, luxury)

2. **Input Refinement**: Once the user provides their details, the app asks for any additional information required (e.g., specific activities, dietary restrictions).

3. **Itinerary Generation**: The app generates a detailed itinerary based on the user’s preferences. It suggests activities and dining options for each day and provides recommendations for accommodations that fit the user’s budget and mobility concerns.

4. **Output**: The app displays the generated itinerary day by day, including the activities, meals, and any additional recommendations.

### **Sample Input and Output**

#### **Sample Input:**

```text
Name: John Doe
Budget: 1500
Duration: 7 days
Destination: Paris
Purpose: Leisure
Preferences: Nature, Museums
Dietary Preferences: Vegetarian
Mobility Concerns: None
Accommodation: Mid-range
```

#### **Sample Output:**

```text
John Doe's Personalized Itinerary for Paris (7 Days)

Trip Purpose: Leisure
Budget: 1500
Dietary Preferences: Vegetarian
Mobility Concerns: None
Accommodation: Mid-range option in a central location for easy access to major attractions.

Detailed Itinerary:

Day 1:
  - Morning: Visit top-rated attractions in Paris like the Eiffel Tower.
  - Afternoon: Explore off-the-beaten-path locations.
  - Lunch at a vegetarian-friendly restaurant.
  - Evening: Relaxing activity with minimal walking, such as a boat tour.

Day 2:
  - Morning: Visit the Louvre Museum.
  - Afternoon: Explore hidden gems in Montmartre.
  - Lunch at a vegetarian-friendly restaurant.
  - Evening: Take a leisurely walk through Luxembourg Gardens.

Day 3:
  - Morning: Explore the Musée d'Orsay.
  - Afternoon: Visit the Musée de l'Orangerie and enjoy the Monet paintings.
  - Dinner at a local vegetarian bistro.

...