"""
Simple try of the agent.

@dev You need to add GROQ_API_KEY to your environment variables.
"""

import os
import sys
import asyncio
import traceback
import logging

# Enable detailed logging
logging.basicConfig(level=logging.DEBUG)

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_groq import ChatGroq
from browser_use import Agent

try:
    llm = ChatGroq(model="llama-3.3-70b-versatile",api_key=os.getenv("GROQ_API_KEY"))
    

    agent = Agent(
        task='Go to amazon.com, search for laptop, sort by best rating, and give me the price of the first result',
        llm=llm,
    )

    async def main():
        try:
            await agent.run(max_steps=10)
        except Exception as e:
            logging.error("❌ Error during agent execution:", exc_info=True)
            traceback.print_exc()

        input('Press Enter to continue...')

    asyncio.run(main())

except Exception as e:
    logging.error("❌ Error Occurred:", exc_info=True)
    traceback.print_exc()
