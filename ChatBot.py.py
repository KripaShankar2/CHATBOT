import google.generativeai as genai
import os
import PIL.Image
def textgenerate(prompt):
    genai.configure(api_key=os.environ["API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text
def imgtext(image_path):
    genai.configure(api_key=os.environ["API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")
    image = PIL.Image.open(image_path)
    response = model.generate_content(["tell me about this", image])
    return response.text
    
while True:
    user_input=input("you:")
    if("show image" in user_input.lower()):
        image_path=input("enter path:")
        # about=input("enter what you ask about img:")
        output=imgtext(image_path)
        print(output)
    elif(user_input=="stop"):
        break
    else:
        output=textgenerate(user_input)
        print(output)
   