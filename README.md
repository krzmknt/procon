# Procon tool

## Dependencies

- Verified to work with mise (2025.1.0 macos-arm64 (ef6936a 2025-01-01))

## Initial Setup

After cloning this repository, run the following command. This will install the dependencies specified in `mise.toml` via mise synchronization, install the npm libraries, install the pip libraries, and perform initial setup for atcoder-cli.

During atcoder-cli’s initial setup, the contents of the `.config/acc` directory are symlinked to `~/Library/Preferences/atcoder-cli-nodejs`. Note that this operation affects files outside of this repository.

```bash
./install
```

## Download a Contest

For example, to download the problems for a contest called abc123, run:

```bash
./script/init abc123
```

## Testing

To test problem a from contest abc123, run:

```bash
./script/test abc123 a
```

## Submitting

To submit problem a from contest abc123, run:

```bash
./script/submit abc123 a
```
