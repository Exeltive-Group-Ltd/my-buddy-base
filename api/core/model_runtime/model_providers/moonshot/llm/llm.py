from typing import List, Optional, Union, Generator

from core.model_runtime.entities.llm_entities import LLMResult
from core.model_runtime.entities.message_entities import (PromptMessage, PromptMessageTool)
from core.model_runtime.model_providers.openai_api_compatible.llm.llm import OAIAPICompatLargeLanguageModel


class MoonshotLargeLanguageModel(OAIAPICompatLargeLanguageModel):
    def _invoke(self, model: str, credentials: dict,
                prompt_messages: list[PromptMessage], model_parameters: dict,
                tools: Optional[list[PromptMessageTool]] = None, stop: Optional[List[str]] = None,
                stream: bool = True, user: Optional[str] = None) \
            -> Union[LLMResult, Generator]:
        self._add_custom_parameters(credentials)
        return super()._invoke(model, credentials, prompt_messages, model_parameters, tools, stop, stream, user)

    def validate_credentials(self, model: str, credentials: dict) -> None:
        self._add_custom_parameters(credentials)
        super().validate_credentials(model, credentials)

    @staticmethod
    def _add_custom_parameters(credentials: dict) -> None:
        credentials['mode'] = 'chat'
        credentials['endpoint_url'] = 'https://api.moonshot.cn/v1'
