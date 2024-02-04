import unittest

from dbt_rag_tools import DbtModel

from tests.test_data.model_examples import (
    invalid_model,
    model_with_only_name,
    model_with_name_and_description,
    model_with_name_description_and_columns,
    model_with_only_name_prompt_text,
    model_with_name_and_description_prompt_text,
    model_with_name_description_and_columns_prompt_text,
)


class DbtModelTestCase(unittest.TestCase):
    def test_model_constructed_with_invalid_model(self):
        """
        Test for the case when the model is constructed with an invalid model.
        """
        with self.assertRaises(Exception):
            DbtModel(invalid_model)

    def test_model_constructed_with_only_name(self):
        """
        Test for the case when the model is constructed with only a name.
        """
        model = DbtModel(model_with_only_name)

        self.assertIsInstance(model, DbtModel)
        self.assertEqual(model.as_prompt_text(), model_with_only_name_prompt_text)

    def test_model_constructed_with_name_and_description(self):
        """
        Test for the case when the model is constructed with a name and a description.
        """
        model = DbtModel(model_with_name_and_description)

        self.assertIsInstance(model, DbtModel)
        self.assertEqual(
            model.as_prompt_text(), model_with_name_and_description_prompt_text
        )

    def test_model_constructed_with_name_description_and_columns(self):
        """
        Test for the case when the model is constructed with a name, a description, and columns.
        """
        model = DbtModel(model_with_name_description_and_columns)

        self.assertIsInstance(model, DbtModel)
        self.assertEqual(
            model.as_prompt_text(), model_with_name_description_and_columns_prompt_text
        )
