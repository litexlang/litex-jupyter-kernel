# A jupyter kernel for litex

## installation(macOS support only for now)

This reuqires Litex core and Python3, you could install litex core firstly with following command.

```bash
# install litex from homebrew
brew install litexlang/tap/litex
```

After litex core installation, we could install litex_kernel for your jupyter

```bash
# change your env to which your jupyter lab using firstly
# then run following commands
pip install litex_kernel
python -m litex_kernel.install
```

To use it, run:

```bash
jupyter lab
```