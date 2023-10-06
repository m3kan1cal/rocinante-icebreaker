from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType

from tools.tools import get_profile_url


def lookup(name_of_person: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """Given the full name {name_of_person} I want you to get me a link to their LinkedIn profile page.
               Your answer should contain only a URL."""

    tools_for_agent = [
        Tool(
            name="Crawl Google for LinkedIn profile page",
            func=get_profile_url,
            description="Useful for when you need to get the LinkedIn Page URL.",
        )
    ]

    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )

    linkedin_profile_url = agent.run(
        prompt_template.format_prompt(name_of_person=name_of_person)
    )
    return linkedin_profile_url
