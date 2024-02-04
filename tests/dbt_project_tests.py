import unittest

from dbt_rag_tools import DbtProject, DbtModel

VALID_PROJECT_PATH = "/Users/pragunbhutani/Code/sandbox/datarag/tests/test_data/valid_dbt_project"

class DbtProjectTestCase(unittest.TestCase):
    def test_project_root_is_not_dbt_project(self):
        """
        Test for the case when the project root is not a dbt project.
        """
        with self.assertRaises(Exception):
            DbtProject("invalid_path")

    def test_class_constructed_with_valid_project_root(self):
        """
        Test for the case when the class is constructed with a valid project root.
        """
        project = DbtProject(VALID_PROJECT_PATH)

        self.assertIsInstance(project, DbtProject)

    def test_get_models_all_folders(self):
        """
        Test for the case when we want to get all the models in the project.
        """
        project = DbtProject(VALID_PROJECT_PATH)
        models = project.get_models()

        self.assertEqual(len(models), 5)

    def test_get_models_with_included_folders(self):
        """
        Test for the case when we want to get all the models in one/many specific folder(s).
        """
        project = DbtProject(VALID_PROJECT_PATH)
        models = project.get_models(included_folders=["models/staging", "models/intermediate"])

        self.assertEqual(len(models), 3)
        
        for i in range(len(models)):
            self.assertIsInstance(models[i], DbtModel)

        self.assertEqual(models[0].name, "staging_1")
        self.assertEqual(models[1].name, "staging_2")
        self.assertEqual(models[2].name, "intermediate_1")

    def test_get_models_with_excluded_folders(self):
        """
        Test for the case when we want to get all the models in the project, 
        except for those in one/many specific folder(s).
        """
        project = DbtProject(VALID_PROJECT_PATH)
        models = project.get_models(excluded_folders=["models/intermediate"])

        self.assertEqual(len(models), 4)
        for i in range(len(models)):
            self.assertIsInstance(models[i], DbtModel)

    def test_get_models_by_name(self):
        """
        Test for the case when we want to get only specific models by name.
        """
        project = DbtProject(VALID_PROJECT_PATH)
        models = project.get_models(models=["staging_1", "staging_2"])

        self.assertEqual(len(models), 2)
        self.assertEqual(models[0].name, "staging_1")
        self.assertEqual(models[1].name, "staging_2")


if __name__ == "__main__":
    unittest.main()


# self.assertEqual(
#     models,
#     [
#         {
#             "name": "model_1",
#             "description": "model_1_description",
#             "columns": [
#                 {"name": "col_1", "description": "col_1_description"},
#                 {"name": "col_2", "description": "col_2_description"},
#             ],
#         },
#         {
#             "name": "model_2",
#             "description": "model_2_description",
#             "columns": [
#                 {"name": "col_1", "description": "col_1_description"},
#                 {"name": "col_2"},
#             ],
#         },
#         {
#             "name": "staging_1",
#             "columns": [
#                 {"name": "col_1"},
#             ],
#         },
#         {
#             "name": "staging_2",
#             "columns": [
#                 {"name": "col_with_description", "description": "col_with_description_description"},
#                 {"name": "col_witout_description"},
#             ],
#         }
#     ],
# )
