from ipykernel.kernelbase import Kernel
from pexpect import replwrap, EOF

from subprocess import check_output

import re

__version__ = "0.1.6.beta"
version_pat = re.compile(r"version (\d+(\.\d+)+)")
litex_path = "litex"


def code_formatter(code):
    litex_indentation = " " * 4
    code_lines = code.splitlines()
    formatted_lines = []
    for index, line in enumerate(code_lines):
        is_last_line = index >= len(code_lines) - 1
        if line.strip() == "":
            continue
        elif line.startswith(litex_indentation) and (
            is_last_line
            or not code_lines[index + 1].rstrip().startswith(litex_indentation)
        ):
            formatted_lines.append(line.rstrip())
            formatted_lines.append("")
        else:
            formatted_lines.append(line.rstrip())
    return "\n".join(formatted_lines)


class LitexKernel(Kernel):
    implementation = "litex_kernel"
    implementation_version = __version__

    @property
    def language_version(self):
        m = version_pat.search(self.banner)
        return m.group(1)

    _banner = None

    @property
    def banner(self):
        if self._banner is None:
            self._banner = check_output([litex_path, "-version"]).decode("utf-8")
        return self._banner

    language_info = {
        "name": "litex",
        "file_extension": ".lix",
    }

    def __init__(self, **kwargs):
        Kernel.__init__(self, **kwargs)
        self._start_litex()

    def _start_litex(self):
        """Start the litex REPL."""
        # Create a unique prompt to avoid conflicts with other REPLs
        prompt = ">>> "
        continuation_prompt = "... "
        self.litexwrapper = replwrap.REPLWrapper(
            litex_path, prompt, None, continuation_prompt=continuation_prompt
        )
        self.litexwrapper.child.delaybeforesend = 0.1

    def do_execute(
        self, code, silent, store_history=True, user_expressions=None, allow_stdin=False
    ):
        self.silent = silent
        interrupted = False
        try:
            output = self.litexwrapper.run_command(code_formatter(code), timeout=None)
            self.send_response(
                self.iopub_socket, "stream", {"name": "stdout", "text": output}
            )
        except KeyboardInterrupt:
            self.litexwrapper.child.sendintr()
            interrupted = True
            self.litexwrapper._expect_prompt()
            output = self.litexwrapper.child.before
            self.send_response(
                self.iopub_socket, "stream", {"name": "stdout", "text": output}
            )
        except EOF:
            output = self.litexwrapper.child.before
            self._start_litex()
            self.send_response(
                self.iopub_socket, "stream", {"name": "stdout", "text": output}
            )

        if interrupted:
            return {"status": "abort", "execution_count": self.execution_count}
        else:
            return {
                "status": "ok",
                "execution_count": self.execution_count,
                "payload": [],
                "user_expressions": {"name": "stdout", "text": output},
            }
