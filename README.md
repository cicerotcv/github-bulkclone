# Github Bulk Clone

![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)

Clones a list of Github repositories into a commom folder.

### Examples

#### File: _.env_

_(this token is just an example. Don't even try using it.)_

```
GITHUB_ACCESS_TOKEN=ghp_qUiRYTAnBUkxjgFQAwEs3UqUiRYTAnBUkxjg
```

#### File: _repositories.txt_

```
https://github.com/cicerotcv/crowdfunding-smart-contract
https://github.com/cicerotcv/buymeabitcoffee.git
https://github.com/cicerotcv/python-screenshot/tree/master/pyscreenshot
https://github.com/username/repo
```

```sh
# considering you have access to all the repositories
$ python3 -m bulkclone -i repositories.txt -o repos

# considering you need to use the access token to have access
# and it's already set to GITHUB_ACCESS_TOKEN environment variable
# or there is a .env file in the current directory
$ python3 -m bulkclone -i repositories.txt -o repos --use-access-token

# in case you want to use a custom .env path
$ python3 -m bulkclone -i repositories.txt -o repos --use-access-token -e /path/to/.env
```

### Arguments:

```
[-i, --input-file] INPUT_FILE 
    Path of the input file which each line is a Github repository url.

--use-access-token
    Whether should use Github access token or not.

[-e, --env] DOTENV_PATH
    .env file containing GITHUB_ACCESS_TOKEN variable.
    Defaults to ".env"

[-o, --output-dir] OUTPUT_DIR
    Directory in which all the repositories will be cloned inside.
    Defaults to "repositories/"
  
[--pattern] DIRECTORY_PATTERN
    Cloned directory name pattern. Accepts wildcards {user} and {repo}.
    Using "{user}_{repo}" as pattern, this repository would be cloned into "cicerotcv_github-bulkclone".
    Defaults to "{repo}"
```

<center>
  <a href="https://buymeabitcoffee.vercel.app/btc/15NvrWRS8DXNufF9i1xJTMmZAcxRZat8Hi">
    <img src="https://buymeabitcoffee.vercel.app/api/btc?style=for-the-badge" alt="Bitcoin address">
  </a>
  <a href="https://buymeabitcoffee.vercel.app/eth/0xc2f6ac7ddf4df7d1b68908b81f97dd3aa0c36675">
    <img src="https://buymeabitcoffee.vercel.app/api/eth?style=for-the-badge" alt="Ethereum Address">
  </a>
</center>
