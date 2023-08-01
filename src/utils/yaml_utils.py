import yaml


def read_yaml(yaml_path):
    with open(yaml_path, "r") as ymlfil:
        config_data = yaml.safe_load(ymlfil)
    print(config_data)
    return config_data
