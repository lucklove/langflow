from environs import Env
from langchain.chat_models import AzureChatOpenAI


env = Env()
env.read_env()

class PingChatTestLLM(AzureChatOpenAI):
    def __init__(self, temperature=0):
        super(self, PingChatTestLLM).__init__(
            temperature=temperature,
            openai_api_base=env.str('AZURE_OPENAI_API_BASE'),
            openai_api_version="2023-03-15-preview",
            deployment_name=env.str('AZURE_DEPLOYMENT_NAME'),
            openai_api_key=env.str('AZURE_OPENAI_API_KEY'),
            openai_api_type = "azure",
        )

CUSTOM_LLMS = {
    "PingChatTestLLM": PingChatTestLLM,
}