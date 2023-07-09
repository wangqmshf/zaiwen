from typing import Mapping, Optional, List, Any

import requests
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM


class ZaiWenLLM(LLM):
    url: str
    resource = "/message"

    @property
    def _llm_type(self) -> str:
        return "zaiwen"

    def _call(
            self,
            prompt: str,
            stop: Optional[List[str]] = None,
            run_manager: Optional[CallbackManagerForLLMRun] = None,
    ) -> str:
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")

        input_message = {"message": [{"role": "user", "content": prompt}],
                         "mode": "v3.5",
                         "key": None}
        response = requests.post(self.url + self.resource, json=input_message)
        text = response.text
        return text

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"url": self.url}
