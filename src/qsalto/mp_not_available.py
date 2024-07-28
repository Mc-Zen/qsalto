class mp_error:
    def __getattr__(self, _):
        raise RuntimeError(
            "In order to use the `precise` mode, you need to install the python package mpmath"
        )
