import openai
import pdfkit

# Set up OpenAI API credentials
openai.api_key = "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"

# Prompt user for a topic
topic = input("Enter a topic for the article: ")

# Generate content using ChatGPT
model_engine = "text-davinci-002"
prompt = f"Write an article about {topic}."
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    temperature=0.5,
    max_tokens= 2048,  # Increase the max_tokens value
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
content = response.choices[0].text

# Save generated text as a PDF
pdfkit.from_string(content, f"{topic}.pdf")
print(f"Article saved as {topic}.pdf")
