invalid_model = {
    "name": None,
}

model_with_only_name = {
    "name": "example_model",
}

model_with_only_name_prompt_text = (
    "The table example_model is described as follows: "
    + "\nThis table contains the following columns:\n"
)

model_with_name_and_description = {
    "name": "example_model",
    "description": "model_description",
}

model_with_name_and_description_prompt_text = (
    "The table example_model is described as follows: model_description"
    + "\nThis table contains the following columns:\n"
)

model_with_name_description_and_columns = {
    "name": "example_model",
    "description": "model_description",
    "columns": [
        {"name": "col_1", "description": "col_1_description"},
        {"name": "col_2", "description": "col_2_description"},
    ],
}

model_with_name_description_and_columns_prompt_text = (
    "The table example_model is described as follows: model_description"
    + "\nThis table contains the following columns:\n"
    + "\n"
    + "- col_1: col_1_description"
    + "\n"
    + "- col_2: col_2_description"
)
