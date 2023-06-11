MAIN_SERVICE = "app/main_service"
ENDPOINT = "https://7e96-34-142-178-226.ngrok.io/predict"


class Folders:
    TEMPLATES = f"{MAIN_SERVICE}/templates"
    STATIC = f"{MAIN_SERVICE}/static"


chat_prompt = lambda category, cv_text: (
    f"Take the following Resume and extract list of the skills that are for this category: {category}:\n"
    f"{cv_text}\n"
    f"and another list of recommended 5 skills for this profession that are not in the first list or in the resume at all.\n"
    f"Return answer in the following format:\n"
    f"[skill1, skill2, skill3, skill4, skill5], [missing_skill1, missing_skill2, missing_skill3, missing_skill4, missing_skill5]\n"
    f"each list and each [] can have up to 5 skills (or less)."
)
