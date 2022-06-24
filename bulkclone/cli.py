# -*- encoding :: utf-8 -*-
import argparse

from .utils import PathUtils


class Arguments:
    def __init__(self, input_file: str, use_access_token: bool,
                 dotenv_path: str,  output_dir: str, directory_pattern: str):
        self.input_file = input_file
        self.use_access_token = use_access_token
        self.dotenv_path = dotenv_path
        self.output_dir = output_dir
        self.directory_pattern = directory_pattern


def parse_arguments() -> Arguments:
    """Parse CLI arguments"""
    args = argparse.ArgumentParser("Github BulkClone")

    args.add_argument("-i", "--input-file",
                      dest="input_file",
                      required=True,
                      type=PathUtils.absolute_path,
                      help="Path of the input file which each line is a Github repository url.")

    args.add_argument("--use-access-token",
                      dest="use_access_token",
                      default=None,
                      action="store_true",
                      help="Whether should use Github access token or not.")

    args.add_argument("-e", "--env",
                      dest="dotenv_path",
                      required=False,
                      default=".env",
                      help=".env file containing GITHUB_ACCESS_TOKEN variable.")

    args.add_argument("-o", "--output-dir",
                      dest='output_dir',
                      required=False,
                      default="./repositories",
                      type=PathUtils.relative_path,
                      help="Directory in which all the repositories will be cloned inside. Defaults to 'repositories/'")

    args.add_argument('--pattern',
                      dest="directory_pattern",
                      default="{repo}",
                      required=False,
                      type=str,
                      help="Cloned directory name pattern. Accepts wildcards {user} and {repo}. Defaults to '{repo}'")

    parsed = args.parse_args()

    return Arguments(**parsed.__dict__)
