from typing import (
    Dict,
    List,
)


def get_sort_options() -> List[Dict[str, str]]:
    return {
        "sort_options": [
            {
                "field": "task__a",
                "description": "По длине ребра куба",
            },
            {
                "field": "task__h",
                "description": "По высоте цилиндра",
            },
            {
                "field": "task__r",
                "description": "По радиусу основания цилиндра",
            },
            {
                "field": "task__m",
                "description": "По объему жидкости",
            },
        ],
    }
