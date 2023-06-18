import os
import typing

from kor.extraction import create_extraction_chain
from langchain.chat_models import ChatOpenAI

from .schemas import person_schema

if typing.TYPE_CHECKING:
    from langchain import LLMChain


openai_api_key = os.environ["OPENAI_KEY"]

llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0,
    max_tokens=2000,
    openai_api_key=openai_api_key,
)

extractor: "LLMChain" = create_extraction_chain(
    llm, person_schema, encoder_or_encoder_class="json"
)
