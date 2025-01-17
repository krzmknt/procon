# Procon tools

## Dependencies

It has been verified in the following environment.

```txt
$ sw_vers
ProductName:            macOS
ProductVersion:         15.0.1
BuildVersion:           24A348

$ bash --version
GNU bash, version 5.2.26(1)-release (aarch64-apple-darwin23.2.0)
Copyright (C) 2022 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>

This is free software; you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

$ mise -v
              _                                        __
   ____ ___  (_)_______        ___  ____        ____  / /___ _________
  / __ `__ \/ / ___/ _ \______/ _ \/ __ \______/ __ \/ / __ `/ ___/ _ \
 / / / / / / (__  )  __/_____/  __/ / / /_____/ /_/ / / /_/ / /__/  __/
/_/ /_/ /_/_/____/\___/      \___/_/ /_/     / .___/_/\__,_/\___/\___/
                                            /_/
2025.1.0 macos-arm64 (ef6936a 2025-01-01)
```

## Initial Setup

After cloning this repository, run the following command. It will synchronize dependencies specified in `mise.toml`, install npm and pip libraries, and initialize atcoder-cli.

When setting up atcoder-cli for the first time, the `.config/acc` directory is symlinked to `~/Library/Preferences/atcoder-cli-nodejs`. Keep in mind that this action will impact files outside of this repository.

```bash
./install
```

## Download a Contest

To download the tasks for contest ABC123, simply run the following command:

```bash
./script/init abc123
```

## Testing

To _test_ the code for task A of contest ABC123, run:

```bash
./script/test abc123 a
```

## Submitting

To _submit_ the code for task A of contest ABC123, run:

```bash
./script/submit abc123 a
```

## For neovim users

If you use neovim, it is reccommened to use [krzmknt/procon-utils.nvim](https://github.com/krzmknt/procon-utils.nvim) for neovim integration.
