from typing import Tuple

from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent
from output_parsers import person_intel_parser, PersonIntel
from third_parties.linkedin import scrape_linkedin_profile
from third_parties.twitter import scrape_user_tweets


def break_ice(name_of_person: str) -> Tuple[PersonIntel, str]:
    linkedin_profile_url = linkedin_lookup_agent(name_of_person=name_of_person)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)

    twitter_username = twitter_lookup_agent(name_of_person=name_of_person)
    tweets = scrape_user_tweets(username=twitter_username, num_tweets=10)

    summary_template = """
            Given the LinkedIn information {linkedin_information} and Twitter {twitter_information} about a person, 
            I want you to create:
            1. A short summary
            2. Two interesting facts about them
            3. A question you would ask them if you met them
            4. Two creative ice breakers to open a conversation with them
            \n{format_instructions}
        """

    summary_prompt_template = PromptTemplate(
        input_variables=["linkedin_information", "twitter_information"],
        template=summary_template,
        partial_variables={
            "format_instructions": person_intel_parser.get_format_instructions()
        },
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    chain_result = chain.run(
        linkedin_information=linkedin_data, twitter_information=tweets
    )

    return person_intel_parser.parse(chain_result), linkedin_data.get("profile_pic_url")


if __name__ == "__main__":
    print("Hellow LangChain!")
    result = break_ice("Daniel Day-Lewis")
    print(result)
