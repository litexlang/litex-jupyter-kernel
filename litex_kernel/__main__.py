from ipykernel.kernelapp import IPKernelApp
from .kernel import LitexKernel
IPKernelApp.launch_instance(kernel_class=LitexKernel)