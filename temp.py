import google.generativeai as genai

# Replace with your actual API key
genai.configure(api_key="AIzaSyDKGpCtS2BY34zqSzp0bGDjWu7pfnS4cqc")

try:
    models = genai.list_models()
    for model in models:
        print(f"Model Name: {model.name}")
        print(f"Supported Methods: {model.supported_generation_methods}")
        print("-" * 20)
except Exception as e:
    print(f"An error occurred: {e}")
