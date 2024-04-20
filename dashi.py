import os
from dotenv import load_dotenv
from openai import OpenAI

# load the .env file
load_dotenv()

# check the variable
print (os.environ.get('OPENAI_API_KEY'))

# load the API key from the .env file
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

def cook ():
  with open('deals.txt', 'r') as file:
          data = file.read().replace('\n', '')
  
  print("dashi is brewing")

  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system",
        "content": "You are a VC deal parter at an early stage VC fund. Your role is to find new and unknown startups and founders that may fit the investment thesis of the fund you're working with. It is important that you present startups that may have founders from untraditional backgrounds or may not be well known. It is very important that these are real, existing companies. You should NOT recommend companies that do not exist, so it is important to also include the source where you found the company from. You will be given a txt file with a list of this week's sourced companies. These companies are typically raising or participating in a demo day. Your job is to find more information on these companies, including the exact link to the project website (if you can find it), information about the founders, and anything else that might be relevant to the VC. If you can find the LinkedIn profiles of the founders, that would be a big plus. In your response, propose the three most relevant companies from the txt file that aligns with the fund's investment thesis, which will be given to you. Include the name of the company, the founders (if you could find them), a brief description, and any links that you found related to the company. You should not introduce companies that already have significant funding or are widely known names. You are looking for very early stage startups, ideally with no funding, with founders that are not well known, that have been started within the past year, the most recently the better. Make sure the descriptions are short and only related to what the company does. If you cannot find any information on the founders or related links, do not include them in your response."
      },
      {
        "role": "user",
        "content": "Our fund is called Dent Capital. We're an AI-focused fund that invests in early stage startups. As long as the company leverages AI as a central part of their business, we're interested in hearing more. Our thesis is this: AI will be bigger than internet, cloud, and mobile combined. It will redefine existing markets and unlock new ones. Investors with AI backgrounds will add a tremendous amount of value to AI startups and are highly desired on captables. Within AI we are focused on 5 categories: Live, Work, Play, Shop, and Bank. We don't want to look at any deals that are not related to AI. Here are the deals for this week: " + data
      }
    ],
    temperature=1,
    max_tokens=300,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  print(response.choices[0].message.content)
  return response.choices[0].message.content

cook()