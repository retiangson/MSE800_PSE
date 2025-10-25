"""
AI-Powered Travel Itinerary Generator (GPT-4)
---------------------------------------------
Interactive CLI app demonstrating built-in
positive and negative prompt guidance for
highly structured and realistic outputs.

Author: Ronald Ephraim C. Tiangson
"""

import json
from openai import OpenAI
from config import OPENAI_API_KEY  # <-- Keep this out of Git

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)


# ---------------------------------------------------
# BUILD PROMPT (with embedded positive/negative guidance)
# ---------------------------------------------------
def build_prompt(destination: str, days: int, budget: str, interests: list[str]):
    """
    Creates a structured prompt for GPT-4 with built-in
    positive (what to do) and negative (what to avoid) guidance.

    **Positive prompt (what to do):**
        -Emphasize realistic, 
        -culturally rich,
        -scenic Auckland activities for a 25-year-old traveler. 
        -Highlight iconic landmarks
        -nature escapes, and balanced daily plans blending urban and outdoor experiences.

    **Negative prompt (what to avoid):**
        -Avoid unrealistic travel
        -nightlife or alcohol focus
        -vague phrases
        -and repetitive activities. 
        -Do not include text outside of valid JSON."
    """
    return f"""
            You are a professional travel planner AI.

            Your task:
            Create a detailed {days}-day travel itinerary for {destination}.
            The traveler's daily budget is {budget}, and their interests include:
            {', '.join(interests)}.

            ---
            Emphasize realistic including: 
            -culturally rich and scenic Auckland activities for a 25-year-old traveler. 
            -Highlight iconic landmarks
            -nature escapes, and balanced daily plans blending urban and outdoor experiences.
            ---
            Avoid unrealistic travel including:
            -nightlife or alcohol focus
            -vague phrases
            -and repetitive activities. 
            ---
            -Do not include text outside of valid JSON."

            Return ONLY valid JSON, structured as:
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

            Ensure the JSON parses cleanly without errors.
            """

# ---------------------------------------------------
# GENERATE ITINERARY
# ---------------------------------------------------
def generate_itinerary(destination, days, budget, interests):
    """Sends prompt to GPT-4 and parses the response."""
    prompt = build_prompt(destination, days, budget, interests)

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional and creative AI travel planner. "
                    "Follow the built-in positive and negative instructions strictly. "
                    "Return JSON only — no commentary or text."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=1000,
    )

    result = response.choices[0].message.content.strip()

    try:
        itinerary = json.loads(result)
        return itinerary, prompt
    except json.JSONDecodeError:
        # Return raw response if model didn't format properly
        return result, prompt


def main():
    print("AI TRAVEL ITINERARY GENERATOR (GPT-4)")
    print("----------------------------------------")

    destination = input("Enter destination: ").strip()
    days = int(input("Number of days: ").strip())
    budget = input("Daily budget (e.g. 150 NZD): ").strip()
    interests = input("Interests (comma-separated): ").split(",")

    print("\nGenerating your itinerary... please wait...\n")

    itinerary, used_prompt = generate_itinerary(
        destination,
        days,
        budget,
        [i.strip() for i in interests],
    )

    print("Done!\n")

    print("\nGenerated Itinerary:\n------------------------------")
    print(json.dumps(itinerary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
