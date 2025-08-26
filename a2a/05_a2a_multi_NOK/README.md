https://www.youtube.com/watch?v=mFkw3p5qSuA
https://github.com/bhancockio/agent2agent/tree/main/a2a_friend_scheduling

TODO:
- separate projects / requirements.txt
- wrong push notification -> doesn't schedule / run


# Host agent

### prompts

- core instructions
- available agents

### tools

- list field availabilities
- book field
- send_message

### steps

- create host agent and pass the remote agents' url
- agent creation: for each url, get AgentCard and save info to self.agents
- (Google) ADK agent: pass self.agents and root instructions
- send message (connect to agent, greet by name, send message via a2a protocol)


ValueError: No root_agent found for 'host_agent_adk'. Searched in 'host_agent_adk.agent.root_agent', 'host_agent_adk.root_agent' and 'host_agent_adk/root_agent.yaml'. Ensure 'C:\DEV\python\python-ai-tutorials\a2a\05_a2a_multi/host_agent_adk' is structured correctly, an .env file can be loaded if present, and a root_agent is exposed.
