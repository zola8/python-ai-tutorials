from google.adk.agents import Agent

news_analyst = Agent(
    name="news_analyst",
    model="gemini-2.0-flash",
    description="News analyst agent",
    instruction="""
    You are a helpful assistant that can analyze news articles and provide a summary of the news.

    If the user ask for news using a relative time, you should use the get_current_time tool to get the current time to use in the search query.
    """,
)
