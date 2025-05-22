# Importing example python package
import python_example_package

# Import the simple submodules/helpers from the current folder "."
from . import simple_submodule

# Import the subpackage_module
from .complex_submodule import complex_submodule1a, complex_submodule1b


def python_example_application_fun():
    print(f"within: {__file__} - fun()")

    simple_submodule.simple_fun()

    complex_submodule1a.fun()
    complex_submodule1b.fun()

    python_example_package.python_example_package_function()

    return True
