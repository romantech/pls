from pathlib import Path
from typing import Any

import yaml


def load_yaml_file(file_path: Path) -> Any:
    """
    Load the YAML file referenced by the given name.

    :param file_path: the path to the YAML file to read and parse
    :return: the parsed contents of the YAML file
    """

    with file_path.open("r", encoding="utf8") as data_file:
        data = yaml.safe_load(data_file)
    return data


def internal_yml_path(file_name: str) -> Path:
    """
    Map the given YAML data file name to the path, assuming that all the data
    files are in the same directory as the file of this function.

    :param file_name: the name of the YAML data file
    :return: the path to the YAML data file
    """

    return Path(__file__).parent.joinpath(file_name)
