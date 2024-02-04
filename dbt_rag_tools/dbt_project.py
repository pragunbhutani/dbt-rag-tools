import os
import glob
import yaml

from dbt_rag_tools.dbt_model import DbtModel


class DbtProject:
    """
    A class representing a DBT project yaml parser.

    Attributes:
        project_root (str): Absolute path to the root of the dbt project being parsed
    """

    def __init__(self, project_root) -> None:
        """
        Initializes a dbt project parser object.

        Args:
            project_root (str): Root of the dbt prject
        """
        self.__project_root = project_root
        project_file = os.path.join(project_root, "dbt_project.yml")

        if not os.path.isfile(project_file):
            raise Exception("No dbt project found in the specified folder")

        with open(project_file) as f:
            project_config = yaml.safe_load(f)

            if "model-paths" not in project_config:
                raise Exception("No model-paths defined in the dbt project file")

            self.__model_paths = project_config.get("model-paths", ["models"])

        return None

    def get_models(self, models=[], included_folders=[], excluded_folders=[]) -> list[DbtModel]:
        """
        Scan all the YMLs in the specified folders and extract all models into a single list.

        Args:
            models (list[str], optional): A list of model names to include in the search.

            included_folders (list[str], optional): A list of paths to all folders that should be included
                in model search. Paths are relative to dbt project root.

            exclude_folders (list[str], optional): A list of paths to all folders that should be excluded
                in model search. Paths are relative to dbt project root.

        Returns:
            list[DbtModel]: A list of Dbt Model objects for each model found in the included folders
        """
        parsed_models = []
        yaml_files = []

        if included_folders == []:
            included_folders = self.__model_paths

        for folder in included_folders:
            yaml_files.extend(
                glob.glob(
                    os.path.join(self.__project_root, folder, "**", "*.yml"),
                    recursive=True,
                )
            )

        if yaml_files == []:
            raise Exception("No YAML files found in the specified folders")

        for file in yaml_files:
            should_exclude_file = False
            
            for excluded_folder in excluded_folders:
                if excluded_folder in file:
                    should_exclude_file = True
                    continue

            if should_exclude_file:
                continue

            with open(file) as f:
                yaml_contents = yaml.safe_load(f)

                for model in yaml_contents.get("models", []):
                    if (models != []) and (model.get("name") not in models):
                        continue                    
                    parsed_models.append(DbtModel(model))

        if parsed_models == []:
            raise Exception("No model ymls found in the specified folders")

        return parsed_models
