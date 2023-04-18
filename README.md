
![Logo](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/th5xamgrr6se0x5ro4g6.png)


# ResuMe

A tool to ...


## Prerequisites

- PyCharm - [Link](https://www.jetbrains.com/pycharm/download/)
- Python ≥ 3.10.10 - [Link](https://www.python.org/downloads/release/python-31010/)
- PDM - [Link](https://pdm.fming.dev/latest/#recommended-installation-method)

## Installation

- Clone the repository
- Download the following model: [Link](https://drive.google.com/file/d/12OhfTBYSXzy_IQ79ONiIOVFZ99ixPO9I/view?usp=share_link)
- Create a folder named `model` in the following path -> `app/model_service`
- Create a folder named `variables` in the following path -> `app/model_service/model`
- Copy the downloaded model files to `app/model_service/model`
- Move `variables.data-00000-of-00001` and `variables.index` into `app/model_service/model/variables`
- Nevigate to `ResuMe` cloned folder and run `pdm sync`
- Run in two seperate terminal sessions:
    - `uvicorn app.main_service.main:app --reload --port 8080`
    - `uvicorn app.model_service.main:app --reload --port 8000`
- Go to 127.0.0.1:8080
## Tech Stack

**Client:** Jinja2, HTML, Bootstrap-4.2.2

**Server:** FastAPI

**Model:** Tensorflow, Keras

**Package Managment:** PDM
## Authors

- [@PsychoRover](https://www.github.com/PsychoRover)

