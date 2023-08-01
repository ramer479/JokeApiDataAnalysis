from etl.joke_import_api import JokeApi
from utils import yaml_utils


def main():
    cfg_path = "./config/JokeConf.yaml"
    api_cfg = yaml_utils.read_yaml(yaml_path=cfg_path)
    jokeApi = JokeApi(api_config=api_cfg)
    print(jokeApi.construct_api_url())

if __name__ == "__main__":
    main()