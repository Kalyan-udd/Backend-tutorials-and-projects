from google import genai

prompt = ""
while prompt != "end":
    prompt = str(input("> "))


    client = genai.Client(api_key="AIzaSyB__ga4HVGLkacSiP3To1kEaUr5d2j8LMc")

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents= prompt
    )

    print(f"Gemini: {response.text}")
