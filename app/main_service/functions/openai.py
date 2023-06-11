from langchain.chat_models import ChatOpenAI

openai_api_key = "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"


llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0,
    max_tokens=2000,
    openai_api_key=openai_api_key,
)


def extract_skills(model_response):
    # Extract relevant skills and missing skills from model response
    start_index = model_response.find("[") + 1
    end_index = model_response.find("]")
    relevant_skills = model_response[start_index:end_index].strip().split(", ")[:5]

    start_index = model_response.find("[", end_index) + 1
    end_index = model_response.find("]", start_index)
    missing_skills = model_response[start_index:end_index].strip().split(", ")[:5]

    return relevant_skills, missing_skills
