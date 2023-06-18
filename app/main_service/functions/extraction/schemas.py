from kor.nodes import Object, Text

from .examples import FULL_RESUME, JOB_EXAMPLE

jobs_schema = Object(
    id="jobs",
    description="Holds the job places and roles",
    attributes=[
        Text(id="job", description="The past jobs of the person", many=True),
        Text(id="role", description="The past roles of the person", many=True),
    ],
    examples=[
        (
            JOB_EXAMPLE,
            [
                {"job": ["DHL", "One Technologies"]},
                {"role": ["Data  Analyst", "Priority  Implementor"]},
            ],
        )
    ],
)

person_schema = Object(
    id="person",
    description="Personal information about a person",
    attributes=[
        Text(
            id="name",
            description="The full name of a person.",
        ),
        jobs_schema,
    ],
    examples=[
        (FULL_RESUME, [{"name": "Bel Amir"}]),
    ],
)
