from typing import Tuple

import requests
from fastapi import Request, UploadFile

from ..constants import ENDPOINT, chat_prompt
from ..templates import Prediction
from .openai import extract_skills, llm
from .pdf import parse_pdf


def _get_classification(cv_text: str) -> Tuple[float, str]:
    response = requests.post(
        ENDPOINT,
        json=[cv_text],
    )
    # return response.json()
    return 0.94, "Good"  # Mock data when you need it


def candidate_parse(request: Request, pdf_file: UploadFile, user_type: str):
    cv_text, name, email = parse_pdf(pdf_file.file)

    assurance, category = _get_classification(cv_text)

    # model_response = llm.predict(chat_prompt(category, cv_text))
    model_response = "[Mock, Data, When, You, Need, It]"  # Mock data when you need it

    relevant_skills, missing_skills = extract_skills(model_response)

    return Prediction(
        context={
            "request": request,
            "prediction": category,
            "assurance": f"{assurance:.2f}",
            "name": name,
            "email": email,
            "relevant_skills": relevant_skills,
            "missing_skills": missing_skills,
            "user_type": user_type,
        },
    )


def recruiter_parse(request: Request, pdf_file: UploadFile, user_type):
    cv_text, _, email = parse_pdf(pdf_file.file)

    score, category = _get_classification(cv_text)
    # LLM extraction ...

    return Prediction(
        context={
            "request": request,
            "prediction": category,
            "assurance": f"{score:.2f}",
            "name": _,
            "email": email,
            "user_type": user_type,
        },
    )


analyzer_resolver = {"candidate": candidate_parse, "recruiter": recruiter_parse}
