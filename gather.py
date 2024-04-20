import os
from dotenv import load_dotenv
from openai import OpenAI

# load the .env file
load_dotenv()

# load the API key from the .env file
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))


# this function takes a text file (it would be a scraped version of an email) and passses it to OpenAI. OpenAI will read the file and extract the companies and deals mentioned in the text file. That data should be written to a new file called extracted-data.txt.

def parse():

    client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

    with open('scraped-data.txt', 'r') as file:
        data = file.read().replace('\n', '')

    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {
          "role": "system",
          "content": "You will read the following text and extract the companies and deals mentioned in the text. You will write the extracted data to a new file called extracted-data.txt. In your response, only include the company name and any relevant information that exists in the text itself to give more context on what the company does or the founders. Only include the company name and description. Do NOT return any additional information in your response. Include as many companies and deals as you can find in the entire txt file."
        },
        {
          "role": "user",
          "content": data
        }
      ],
      temperature=1,
      max_tokens=200,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    # Write the extracted data to deals.txt
    with open('deals.txt', 'w') as file:
        file.write(response.choices[0].message.content)

    print("gather did all the chopping and dicing!")

parse()