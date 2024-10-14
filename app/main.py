import os
from langchain_ollama import ChatOllama
from langchain_community.utilities import SearxSearchWrapper
from langchain_community.tools.searx_search.tool import SearxSearchResults
from langchain.schema.runnable.config import RunnableConfig
from langchain_core.runnables import Runnable

from langgraph.prebuilt import create_react_agent

import chainlit as cl

# from langchain.globals import set_verbose, set_debug
# set_debug(True)
# set_verbose(True)

OLLAMA_API_URL = os.environ.get("OLLAMA_API_URL")
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL")
SEARNGX_URL = os.environ.get("SEARNGX_URL")

def model():
    return ChatOllama(model=OLLAMA_MODEL, base_url=OLLAMA_API_URL)

search = SearxSearchResults(wrapper=SearxSearchWrapper(searx_host=SEARNGX_URL))

tools = [search]

@cl.on_chat_start
async def on_chat_start():
    agent = create_react_agent(model(), tools) #, debug=True)
    cl.user_session.set("agent", agent)


@cl.on_message
async def on_message(message: cl.Message):
    agent: Runnable = cl.user_session.get("agent")
    msg = cl.Message(content="")

    async for chunk in agent.astream_events(
        {"messages": [("user", message.content)]},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
        version="v2"
    ):
        if chunk["event"] == "on_chat_model_stream":
            content = chunk["data"]["chunk"].content
            if content:
                await msg.stream_token(content)

    await msg.send()
