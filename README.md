# A jupyter kernel for litex

## installation (support macOS and Ubuntu)

This reuqires Litex core and Python3

On macOS, you could install litex core by following command:

```bash
brew install litexlang/tap/litex
```

On Ubuntu, you should download litex core deb package (litex_{version}_{architecture}.deb) from [here](https://github.com/litexlang/golitex/releases) to your target system and run following command:

```bash
sudo dpkg -i litex_{version}_{architecture}.deb
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