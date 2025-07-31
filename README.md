# A jupyter kernel for litex

This is iPython kernel designed for JupyterLab, which aims to help Litex user to interact with Litex core via Jupyter.

## installation

This reuqires Litex core and Python3, you could install Litex core follow the [README](https://github.com/litexlang/golitex). 

After Litex core installation, you could install litex_kernel for your jupyter:

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