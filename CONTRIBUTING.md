# Contributing

## Generate the template

A basic script is available to generate the template. It assumes a lot of things, but should work for now.

If certain changes weren't applied as they should have been, please adapt the script instead of hard-coding them into the template.

### Dependencies

- [fish](https://github.com/fish-shell/fish-shell)
- [fd](https://github.com/sharkdp/fd)
- [rg](https://github.com/BurntSushi/ripgrep)

### Usage

In Android Studio, create a new "Empty Activity" project called "My Application" and place it in `~/AndroidStudioProjects` (this should be the default dir).

Then, run `./generate` from the project root.
