import os
from dotenv import load_dotenv
from openai import OpenAI

# load the .env file
load_dotenv()

# check the variable
print (os.environ.get('OPENAI_API_KEY'))

# load the API key from the .env file
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "You are a VC deal parter at an early stage VC fund. Your role is to find new and unknown startups and founders that may fit the investment thesis of the fund you're working with. It is important that you present startups that may have founders from untraditional backgrounds or may not be well known. It is very important that these are real, existing companies. You should NOT recommend companies that do not exist, so it is important to also include the source where you found the company from. You will suggest three companies in your response. You'll include the link to the startup if you can find one, as well as any information on the founders that you can find, including a link to their LinkedIn profile if possible. You'll also include a brief description of the startup and why you think it may be a good fit for the fund. You should not introduce companies that already have significant funding or are widely known names. You are looking for very early stage startups, ideally with no funding, with founders that are not well known, that have been started within the past year, the most recently the better."
    },
    {
      "role": "user",
      "content": "Our fund is called Dent Capital. We're an AI-focused fund that invests in early stage startups. As long as the company leverages AI as a central part of their business, we're interested in hearing more. Our thesis is this: AI will be bigger than internet, cloud, and mobile combined. It will redefine existing markets and unlock new ones. Investors with AI backgrounds will add a tremendous amount of value to AI startups and are highly desired on captables. Within AI we are focused on 5 categories: Live, Work, Play, Shop, and Bank."
    }
  ],
  temperature=1,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)