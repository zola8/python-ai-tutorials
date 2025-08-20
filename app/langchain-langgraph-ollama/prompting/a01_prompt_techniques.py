# https://www.youtube.com/watch?v=McpAToWNcOg&list=PLgYONms4SxY2b4D4TpwUh6VZOIZLGmG2z&index=5
# https://github.com/ahmadvh/Data-Scenario

# See how prompt techniques and (model choose) change the interpretation

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2", temperature=0.2)
email = (
    "Thanks for finally getting back to me. I had almost forgotten we were working on this."
)


def run_prompt(prompt_text):
    prompt = PromptTemplate.from_template(prompt_text)
    chain = RunnableSequence(prompt | llm)
    return chain.invoke({'email': email})


# zero shot prompt
zero_shot_prompt = """
Classify the tone of the following email as POLITE, NEUTRAL or RUDE.
Email: {email}
Tone:
"""

one_shot_prompt = """
Classify the tone of the following email as POLITE, NEUTRAL or RUDE.

Example:
Email: Could you please send me the report by end of day? Thank you!
Tone: POLITE

Now classify:
Email: {email}
Tone:
"""

few_shot_prompt = """
Classify the tone of the following email as POLITE, NEUTRAL or RUDE.

Examples:
Email: Could you please send me the report by end of day? Thank you!
Tone: POLITE

Email: Where is the report? You were supposed to send it yesterday.
Tone: RUDE

Email: Can you send the file when you get a chance?
Tone: NEUTRAL

Now classify:
Email: {email}
Tone:
"""

if __name__ == "__main__":
    # Run and compare
    outputs = {
        "zero_shot_prompt": run_prompt(zero_shot_prompt),
        "one_shot_prompt": run_prompt(one_shot_prompt),
        "few_shot_prompt": run_prompt(few_shot_prompt)
    }

    # display results
    print("---------")
    print("Email: ", email, "\n")
    print("Model predictions with different techniques:")
    for label, result in outputs.items():
        print(f"------ {label}: {result.content}")

    print("---------")
