# -*- encoding :: utf-8 -*-

import os
import re
from typing import List, Optional, Tuple

import dotenv

from .errors import InvalidUrl, MissingAccessToken

GITHUB_BASE_URL = "https://github.com/{user}/{repo}"
GITHUB_AUTHORIZED_URL = "https://{access_token}@github.com/{user}/{repo}"


class UrlUtils:
    """Collection of static methods related to URL operations."""

    @staticmethod
    def parse_github_url(url: str) -> Tuple[str, str]:
        """Extract user and repository name from a Github url.

        Args:
            url (str): Github url

        Returns:
            Tuple[str, str]: (user, repo)
        """
        regexp = re.compile(
            r'(https\:\/\/github.com)\/(.+?)\/([a-z0-9]+(?:[._-][a-z0-9]+)*)')

        matches = re.search(regexp, url)

        if matches is None:
            raise InvalidUrl(url)

        _, username, repository = matches.groups()

        return (username, repository.replace('.git', ''))

    @staticmethod
    def make_cloning(user: str, repo: str, access_token: str = None):
        """Generates a url to be cloned considering the access token if needed"""
        if access_token is not None:
            return GITHUB_AUTHORIZED_URL.format(user=user, repo=repo, access_token=access_token)
        return GITHUB_BASE_URL.format(user=user, repo=repo)


class PathUtils:
    """Collection of static methods related to paths and directories"""
    @staticmethod
    def ensure_dir_exits(path: str):
        """Makes sure the path exists"""
        os.makedirs(path, exist_ok=True)

    @staticmethod
    def normalize(path: str) -> str:
        """Normalize the case and removes double slashes of a given path"""
        normalized = os.path.normpath(path)
        normalized = os.path.normcase(normalized)
        return normalized

    @staticmethod
    def absolute_path(path: str):
        """Ensures the path is well formatted and returns the absolute path.

        Args:
            _path (str): unsafe path

        Returns:
            (str): OS safe absolute path
        """
        normalized = PathUtils.normalize(path)
        absolute_path = os.path.abspath(normalized)
        return absolute_path

    @staticmethod
    def relative_path(path: str):
        """Ensures the path is well formatted and returns the relative path.

        Args:
            _path (str): unsafe path

        Returns:
            (str): OS safe relative path
        """
        normalized = PathUtils.normalize(path)
        relative_path = os.path.relpath(normalized)
        return relative_path

    @staticmethod
    def make_destination(output_dir, pattern, user, repo):
        """Joins the output path and the given pattern, replacing user and 
        repo occurrences by their definitions."""
        relative_path = os.path.join(output_dir, pattern)
        formatted = relative_path.format(user=user, repo=repo)
        return formatted


class IOUtils:
    """Collection of Input/Output static methods"""
    @staticmethod
    def read_file(path: str) -> str:
        """Returns the contents of a file pointed by the input path"""
        with open(path, mode='r', encoding='utf-8') as file:
            return file.read()

    @staticmethod
    def read_lines(path: str) -> List[str]:
        """Loads the file pointed by this path and returns a list of lines.

        Args:
            path (str): file path

        Returns:
            List[str]: a list of non-empty strings
        """
        content = IOUtils.read_file(path)

        # remove leading and trailing empty lines
        content = content.strip()

        def is_empty(line):
            return len(line.strip()) > 0

        lines = filter(is_empty,  content.split('\n'))
        return lines


class EnvUtils:
    """Responsible for loading the GITHUB_ACCESS_TOKEN environment variable"""
    TOKEN_KEY = "GITHUB_ACCESS_TOKEN"

    @staticmethod
    def __get_from_dotenv(env_path: str) -> Optional[str]:
        access_token = dotenv.get_key(env_path, EnvUtils.TOKEN_KEY)
        return access_token

    @staticmethod
    def __get_from_system() -> Optional[str]:
        access_token = os.getenv(EnvUtils.TOKEN_KEY)
        return access_token

    @staticmethod
    def get_access_token(env_path: str) -> str:
        """Loads .env file to get GITHUB_ACCESS_TOKEN environment variable"""
        token = EnvUtils.__get_from_system()

        if token is None:
            token = EnvUtils.__get_from_dotenv(env_path)

        if token is None:
            raise MissingAccessToken(f"Could not get {EnvUtils.TOKEN_KEY} environment variable")

        return token
