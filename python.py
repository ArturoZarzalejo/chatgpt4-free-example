# import os
# import requests
# import openai
# from dotenv import load_dotenv

# load_dotenv()

# openai.api_key = os.environ["OPENAI_API_KEY"]
# openai.organization = "org-7rtiQR7J1pZz7WXjoUvxl6ex"

# completion = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "user", "content": "Hello!"}
#   ]
# )

# print(completion.choices[0].message)

from gpt4free import forefront
# create an account
token = forefront.Account.create(logging=False)
print(token)
# get a response
for response in forefront.StreamingCompletion.create(
	token=token,
	prompt='podrías hacer una función recursiva para resolver fibonacci?',
	model='gpt-4'
):
    print(response.choices[0].text, end='')
print("")

