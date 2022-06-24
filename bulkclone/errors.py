# -*- encoding :: utf-8 -*-


class InvalidUrl(BaseException):
    """InvalidUrl exception is raised when a url does not match the
    pattern. Expected patterns: 

    `https://github.com/{user}/{repo}`

    `https://github.com/{user}/{repo}.git`

    `https://github.com/{user}/{repo}/tree/{branch}`

    `https://github.com/{user}/{repo}/blob/{branch}/{file}`
    """

    def __init__(self, url: str) -> None:
        super().__init__(f"Invalid url: '{url}'")


class MissingAccessToken(BaseException):
    """Should be raised when the access token is needed and could not be loaded."""
