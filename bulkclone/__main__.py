# -*- encoding :: utf-8 -*-

from .bulkclone import BulkClone
from .cli import parse_arguments
from .utils import UrlUtils, PathUtils, IOUtils, EnvUtils


def main():
    # load command line arguments
    args = parse_arguments()
    urls = IOUtils.read_lines(args.input_file)

    # handle access token if needed
    access_token: str = None
    if args.use_access_token:
        access_token = EnvUtils.get_access_token(args.dotenv_path)

    # makes sure the output directory exists before proceeding
    PathUtils.ensure_dir_exits(args.output_dir)

    # clones each of the urls
    for (user, repo) in [UrlUtils.parse_github_url(url) for url in urls]:
        url = UrlUtils.make_cloning(user, repo, access_token)
        dest = PathUtils.make_destination(args.output_dir,
                                          args.directory_pattern,
                                          user, repo)
        BulkClone.clone(url, dest)


if __name__ == '__main__':
    main()
