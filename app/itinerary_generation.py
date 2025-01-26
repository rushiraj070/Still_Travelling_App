def generate_itinerary(refined_context, activities):
    """
    Creates a detailed itinerary for Karnataka based on refined user inputs.
    Includes activities, meals (Breakfast, Lunch, Dinner), and specific attractions.
    """
    if not isinstance(refined_context, dict):
        raise TypeError("Expected refined_context to be a dictionary.")

    # Customizing itinerary with Karnataka-specific activities and dishes
    itinerary = f"""
    {refined_context['name']}'s Personalized Itinerary for Karnataka (10 Days)

    Trip Purpose: {refined_context['purpose']}
    Budget: {refined_context['budget']}
    Dietary Preferences: {refined_context['dietary_preferences']}
    Mobility Concerns: {refined_context['mobility_concerns']}
    Accommodation: {refined_context['accommodation']}

    Detailed Itinerary:
    """

    # Activities & Meals for each day (7-day cycle repeating for 10 days)
    days_activities_and_meals = [
        # Day 1 - Day 7 (Cycle)
        {
            "morning_activity": "Visit the iconic Mysore Palace.",
            "noon_activity": "Lunch at RRR, try Mysore Biryani and Raita.",
            "evening_activity": "Take a stroll at Brindavan Gardens, watch the musical fountain.",
            "breakfast": "Dosa with chutney and sambar.",
            "lunch": "Mysore Biryani and Raita.",
            "dinner": "Mysore Pak for dessert, with a light dinner like Rice and Sambar."
        },
        {
            "morning_activity": "Explore Hampi's Virupaksha Temple and Hampi Bazaar.",
            "noon_activity": "Lunch at one of Hampi's local eateries; enjoy Ragi Mudde (finger millet balls) and Sambar.",
            "evening_activity": "Sunset at the Hemakuta Hill.",
            "breakfast": "Idli with coconut chutney.",
            "lunch": "Ragi Mudde with Sambar.",
            "dinner": "Vegetable Biryani with cucumber raita."
        },
        {
            "morning_activity": "Visit the Bannerghatta National Park and enjoy the safari.",
            "noon_activity": "Lunch at the famous MTR restaurant in Bangalore, try the Rava Idli and Masala Dosa.",
            "evening_activity": "Visit Lalbagh Botanical Garden and take a relaxed evening walk.",
            "breakfast": "Rava Idli with coconut chutney.",
            "lunch": "Masala Dosa with sambhar.",
            "dinner": "Bangalore's famous Bisi Bele Bath."
        },
        {
            "morning_activity": "Travel to Coorg and visit the Abbey Falls.",
            "noon_activity": "Lunch at a Coorgi homestay; enjoy Pandi Curry (pork curry) and Noolputtu (rice noodles).",
            "evening_activity": "Relax at the coffee estates of Coorg.",
            "breakfast": "Coorgi-style Puttu with Kadala Curry.",
            "lunch": "Pandi Curry and Noolputtu.",
            "dinner": "Coorgi-style chicken curry with rice."
        },
        {
            "morning_activity": "Visit Chikmagalur's Mullayanagiri Peak.",
            "noon_activity": "Lunch at a local restaurant, enjoy Akki Roti (rice roti) and Sambar.",
            "evening_activity": "Visit the coffee plantations in Chikmagalur.",
            "breakfast": "Akki Roti with coconut chutney.",
            "lunch": "Akki Roti with Sambar.",
            "dinner": "Vegetable Stew with Appam."
        },
        {
            "morning_activity": "Explore the ruins of Bijapur, starting with the Gol Gumbaz.",
            "noon_activity": "Lunch at a local restaurant, try Jolada Rotti (sorghum roti) and Ennegayi (stuffed brinjal).",
            "evening_activity": "Visit the Ibrahim Rauza for a historical tour.",
            "breakfast": "Poha (flattened rice) with tea.",
            "lunch": "Jolada Rotti and Ennegayi.",
            "dinner": "Ragi Ball with Kurma."
        },
        {
            "morning_activity": "Take a day trip to the Nandi Hills for a peaceful morning trek.",
            "noon_activity": "Lunch at a local restaurant near Nandi Hills, try Pesarattu (green gram pancake) and Sambar.",
            "evening_activity": "Visit the Bhoga Nandeeshwara Temple.",
            "breakfast": "Pesarattu with coconut chutney.",
            "lunch": "Pesarattu with Sambar.",
            "dinner": "Vegetarian Biryani with curd raita."
        },
    ]
    
    # Repeat the 7-day cycle to cover the 10 days
    itinerary_days = ""
    for i in range(10):
        day = days_activities_and_meals[i % 7]  # Use modulo to repeat the 7-day cycle
        itinerary_days += f"""
        Day {i + 1}:
          - Morning Activity: {day['morning_activity']}
          - Breakfast: {day['breakfast']}
          - Noon Activity: {day['noon_activity']}
          - Lunch: {day['lunch']}
          - Evening Activity: {day['evening_activity']}
          - Dinner: {day['dinner']}
        """
    
    itinerary += itinerary_days
    return itinerary
