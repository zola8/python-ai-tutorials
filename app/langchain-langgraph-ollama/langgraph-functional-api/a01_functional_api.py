from langchain_ollama import ChatOllama
from langgraph.func import entrypoint, task

llm = ChatOllama(model="llama3.2", temperature=0.4)


# Tasks
@task
def generate_joke(topic: str):
    """First LLM call to generate initial joke"""
    msg = llm.invoke(f"Write a short joke about {topic}")
    return msg.content


def check_punchline(joke: str):
    """Gate function to check if the joke has a punchline"""
    # Simple check - does the joke contain "?" or "!"
    # if "?" in joke or "!" in joke:
    # return "Pass"
    return "Fail"



@task
def improve_joke(joke: str):
    """Second LLM call to improve the joke"""
    msg = llm.invoke(f"Make this joke funnier by adding wordplay: {joke}")
    return msg.content


@task
def polish_joke(joke: str):
    """Third LLM call for final polish"""
    msg = llm.invoke(f"Add a surprising twist to this joke: {joke}")
    return msg.content


@entrypoint()
def prompt_chaining_workflow(topic: str):
    original_joke = generate_joke(topic).result()
    if check_punchline(original_joke) == "Pass":
        return original_joke

    improved_joke = improve_joke(original_joke).result()
    return polish_joke(improved_joke).result()


if __name__ == "__main__":
    for step in prompt_chaining_workflow.stream("cats", stream_mode="updates"):
        print(step)
        print("\n")


# {'generate_joke': 'Why did the cat join a band?\n\nBecause it wanted to be the purr-cussionist.'}

# {'improve_joke': "Here's an updated version with some added wordplay:\n\nWhy did the cat join a band? Because it was a mew-sic genius and wanted to be the purr-cussionist – after all, it was the cat's meow of a career move!\n\nOr how about this one?\n\nWhy did the cat join a band? It heard the music was off the chain... but as a purr-cussionist, it was paws-itively on beat!\n\nLet me know if you'd like me to come up with more!"}

# {'polish_joke': "I love the wordplay in these jokes. Here are some additional attempts at adding a surprising twist:\n\n1. Why did the cat join a band? Because it was a mew-sic genius and wanted to be the purr-cussionist – but little did anyone know, its meow-mentum was actually a result of its secret life as a time-traveling feline who had been jamming with ancient Egyptian cats.\n\n2. Why did the cat join a band? It heard the music was off the chain... and after a few riffs, it discovered that its purr-cussion skills were not just for show – they were actually a cry for help, as it was trying to communicate with its alien overlords who needed a feline drummer to activate their intergalactic catnip supply.\n\n3. Why did the cat join a band? Because it was a mew-sic genius and wanted to be the purr-cussionist – but what the other band members didn't know was that the cat's incredible talent came at a steep price: every time it played, its whiskers would grow longer and more majestic, until they became an actual third limb that could play the guitar solo.\n\n4. Why did the cat join a band? It heard the music was off the chain... but as a purr-cussionist, it was paws-itively on beat! – or so it seemed. In reality, the cat's drumming was actually controlling the world's cat population, and every time it played a perfect beat, more cats would appear out of thin air to join the band.\n\n5. Why did the cat join a band? Because it was a mew-sic genius and wanted to be the purr-cussionist – but what really drove its creativity was its obsession with 80s power ballads. As it played on, it began to transform into a giant, feline Bon Jovi, complete with a hair-metal mane and leather pants.\n\nFeel free to pick your favorite or suggest any changes you'd like me to make!"}

# {'prompt_chaining_workflow': "I love the wordplay in these jokes. Here are some additional attempts at adding a surprising twist:\n\n1. Why did the cat join a band? Because it was a mew-sic genius and wanted to be the purr-cussionist – but little did anyone know, its meow-mentum was actually a result of its secret life as a time-traveling feline who had been jamming with ancient Egyptian cats.\n\n2. Why did the cat join a band? It heard the music was off the chain... and after a few riffs, it discovered that its purr-cussion skills were not just for show – they were actually a cry for help, as it was trying to communicate with its alien overlords who needed a feline drummer to activate their intergalactic catnip supply.\n\n3. Why did the cat join a band? Because it was a mew-sic genius and wanted to be the purr-cussionist – but what the other band members didn't know was that the cat's incredible talent came at a steep price: every time it played, its whiskers would grow longer and more majestic, until they became an actual third limb that could play the guitar solo.\n\n4. Why did the cat join a band? It heard the music was off the chain... but as a purr-cussionist, it was paws-itively on beat! – or so it seemed. In reality, the cat's drumming was actually controlling the world's cat population, and every time it played a perfect beat, more cats would appear out of thin air to join the band.\n\n5. Why did the cat join a band? Because it was a mew-sic genius and wanted to be the purr-cussionist – but what really drove its creativity was its obsession with 80s power ballads. As it played on, it began to transform into a giant, feline Bon Jovi, complete with a hair-metal mane and leather pants.\n\nFeel free to pick your favorite or suggest any changes you'd like me to make!"}
