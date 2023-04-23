<p align="center">
<img src="https://github.com/PsychoRover/ResuMe/blob/2614dc23c36fde5e1aefeeb24a79fa126d11810a/logo.png" />
</p>

# ResuMe

As an AI-powered candidate screening tool, our aim is to reduce the time it takes for HR to screen candidates. Our machine learning algorithms can quickly analyze resumes and job applications, identifying the best candidates for a given job based on specific criteria such as skills


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
- Go to 127.0.0.1:8080 in your browser
## Tech Stack

**Client:** Jinja2, HTML, Bootstrap-4.2.2

**Server:** FastAPI

**Model:** Tensorflow, Keras

**Package Managment:** PDM
## Authors

- [@PsychoRover](https://www.github.com/PsychoRover)
- [@Tlevius](https://github.com/Tlevius) 
- [@HA-22L](https://github.com/HA-22L)

