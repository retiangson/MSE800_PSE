"""
AI-Powered Travel Itinerary Generator (GPT-4)
Interactive OpenAI API and prompt engineering.
Author: Ron
"""

import json
from openai import OpenAI
from config import OPENAI_API_KEY  # <-- Keep this out of Git

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)


def build_prompt(destination: str, days: int, budget: str, interests: list[str]):
    """Creates a structured prompt for GPT-4."""
    return f"""
You are a professional travel planner.
Create a detailed {days}-day travel itinerary for {destination}.
The traveler's daily budget is {budget} and their interests include: {', '.join(interests)}.
Each day should include:
- Morning, Afternoon, and Evening activities
- Short realistic descriptions
- Estimated daily cost

Respond ONLY in valid JSON format as:
[
  {{
    "day": 1,
    "location": "{destination}",
    "activities": [
      "Morning: ...",
      "Afternoon: ...",
      "Evening: ..."
    ],
    "estimated_cost": 0
  }}
]
Make sure the JSON can be parsed without errors.
"""


def generate_itinerary(destination, days, budget, interests):
    """Sends prompt to GPT-4 and parses the response."""
    prompt = build_prompt(destination, days, budget, interests)

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful AI travel assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=1000,
        top_p=1,
        top_k=0,
        frequency_penalty=0,
        presence_penalty=0,

    )

    result = response.choices[0].message.content.strip()

    try:
        itinerary = json.loads(result)
        return itinerary
    except json.JSONDecodeError:
        print("Could not parse JSON properly. Showing raw output:\n")
        return result


def main():
    print("AI TRAVEL ITINERARY GENERATOR (GPT-4)")
    print("---------------------------------------")

    destination = input("Enter destination: ")
    days = int(input("Number of days: ").strip())
    budget = input("Daily budget (e.g. 150 NZD): ")
    interests = input("Interests (comma-separated): ").split(",")

    print("\nGenerating your itinerary... please wait...\n")

    itinerary = generate_itinerary(destination, days, budget, [i.strip() for i in interests])

    print("Done! Here’s your generated itinerary:\n")
    print(json.dumps(itinerary, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
