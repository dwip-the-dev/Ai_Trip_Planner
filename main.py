import streamlit as st
from google import genai
import datetime

client = genai.Client(api_key='GOOGLE GEMINI API KEY')

st.title("AI Trip-Planner ✈️")

with st.form("trip_form"):
    starting_point = st.text_input("Starting Point (City or Landmark):")
    destination = st.text_input("Destination (City or Landmark) with coma separated" , placeholder="e.g., Odisha, Ladakh, Goa , Kerala, Rajasthan, Himachal Pradesh, etc.")
    starting_date = st.date_input("Starting Date:" ,min_value=datetime.date.today())
    ending_date = st.date_input("Ending Date:" ,min_value=datetime.date.today())
    num_travelers = st.number_input("Number of Travelers:", min_value=1, value=1)    
    budget = st.number_input("Budget (in INR):", min_value=1000)
    trip_type = st.selectbox("Type of Trip:", ["Adventure", "Relaxation", "Cultural", "Spiritual", "Family", "Solo"])
    interests = st.text_area("Interests (comma separated):", placeholder="e.g., temples, museums, food, beaches, shopping")
    submit_btn = st.form_submit_button("Plan My Trip", type="primary")


if submit_btn:
    if not all([starting_point, destination, starting_date, ending_date, budget, trip_type, interests]):
        st.error("Please fill in all the fields.")
    else:
        with st.spinner("Planning your trip..."):
            prompt = f"""
            Create a detailed daily travel itinerary with the following information:

            Starting from: {starting_point}
            Destinations to visit: {destination}
            Trip start from {starting_date} to {ending_date}
            Number of travelers: num_travelers
            Budget: {budget} INR
            Travel style: {trip_type}
            Please provide a day-by-day itinerary including:
            1. Transportation options between between locations
            2. Recommended accommodations
            3. Key attractions to visit each day
            4. Estimated costs for each major activity
            5. Local cuisine recommendations
            Any practical tips or considerations
            Format the response in a clear, organized manner with sections for each day."""


            response = client.models.generate_content (model="gemini-2.5-flash", contents=prompt) 

            st.write(response.text)
