import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generate_caption(topic, platform, tone):

    prompt = f"""
    Generate a social media post.

    Topic: {topic}
    Platform: {platform}
    Tone: {tone}

    Include:
    - engaging caption
    - emojis
    - 5 hashtags
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )

    return response.choices[0].message.content
