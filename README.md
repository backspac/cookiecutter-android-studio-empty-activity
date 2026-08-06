# cookiecutter-android-studio-empty-activity

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for a new Empty Activity from Android Studio

## Dependencies

- [gradle](https://github.com/gradle/gradle): A local Gradle should be installed so that the wrapper and other Gradle-related stuff can be generated.

## Contributing

### Generate the template

A basic script is available to generate the template. It assumes a lot of things, but should work for now.

#### Dependencies

- [fish](https://github.com/fish-shell/fish-shell)
- [fd](https://github.com/sharkdp/fd)
- [rg](https://github.com/BurntSushi/ripgrep)

#### Usage

In Android Studio, create a new "Empty Activity" project called "My Application" and place it in `~/AndroidStudioProjects` (this should be the default dir).

Then, run `./generate` from the project root.
