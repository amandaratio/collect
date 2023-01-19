# collect + export functions via command line

> extracts all functions + import statements from a specific file / collection of files from a directory and exports to another file [^1] . 


[^1]: compatible with only python syntax (next language to be suppported: elixir)


### Parameters
```
from_file : str
      The path to file or directory that the all functions will be extracted from

to_file : str
        The path to file* (ext .py) to insert extracted functions.
        (if file does not exist, the file is created)

overwrite : bool, OPTIONAL (default = False)
        Overwrites the file (which extracted functions are being inserted into)
        (default is False --> appends to end of the file)

regex : str, OPTIONAL
        specific regex pattern that a file must match if the from_path parameter is a directory
        (default is NONE & only collects from files with extention .py)
```
### Command line syntax
    python3 collect.py --from_path "file path or directory path" --to_path "file path"

### Example [^2]
    python3 collect.py --from_path "116/" --to_path "116/math116.py" --regex "HW_[0-9]*.*" --overwrite True

:arrow_lower_right: extracts functions & import statements from files in directory ***"116/"*** with name thats matches regex pattern, `HW_[0-9]*.*`

:arrow_lower_right: inserts into file ***"116/math116.py"*** (via overwriting)

:arrow_lower_right: now able to acces all functions by adding import statement `from math116 import *`

[^2]: see ***'116/math116.py'*** for result and ***'116/HW_0.py', '116/HW_1.py', '116/HW_2.py'*** for original files in this repo




