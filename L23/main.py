from google import genai

with open("api_key.txt", "r") as key_file:
    key = key_file.read()
    #print(key)
    client = genai.Client(api_key=key)
    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
    )
    print(response.text)