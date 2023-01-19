import re
import os
import argparse


def main():
    parser = argparse.ArgumentParser(description="Generate your vaccination QR code.")
    parser.add_argument("-f", "--from_path", type=str, help="Path to file or directory where functions are to be extracted from", required=True)
    parser.add_argument("-t", "--to_path", type=str, help="Path to file where extracted functions will be inserted to", required=True)
    parser.add_argument("-o", "--overwrite", type=bool, help="Flag to overwrite file where extracted functions will inserted into", required=False, default=False)
    parser.add_argument("-r", "--regex", type=str, help="Regex pattern used to collect files that match if in the specified directory (--from_path)", required=False, default=".*")
    args = parser.parse_args()

    collect_functions(args.from_path, args.to_path, OVWR=args.overwrite, r=args.regex)


def collect_functions(from_file, to_file, OVWR=False, r=".*"):
    """
    Extracts functions & imports from a python file and writes them to another python file

    Parameters
    ----------
    from_file : str
        The path to file or directory that the all functions will be extracted from
    to_file : str
        The path to file* (ext .py) to insert extracted functions.
        * if file does not exist, the file is created
    OVWR : bool, OPTIONAL (default = False)
        Overwrites the file (which extracted functions are being inserted into)
        (default is False --> appends to end of the file)
    r : str, OPTIONAL
        specific regex pattern that a file must match if the from_path parameter is a directory
        (default is NONE --> selects files with extention .py)
    
    """
    this = os.path.abspath(__file__)

    def write(from_file, to_file, OVWR=False):
        mode = 'a' if not bool(OVWR) else 'w'
        try:
            with open(from_file, 'r') as f:
                data = f.read()

                with open(to_file, mode) as to:
                    to.write("\n# ************* {} ************* #\n".format(os.path.basename(from_file)))
                    in_func = False
                    for line in data.splitlines():
                        func = re.fullmatch('def\s[a-zA-Z0-9_]+\(.*\):\s*#*.*', line)
                        imprt = (re.fullmatch('import\s[a-zA-Z]+', line) or re.fullmatch('from\s[a-zA-Z]*\simport\s[a-zA-Z]+', line)) and line != "from {} import *".format(to_file)

                        if in_func and (re.fullmatch('\s{4}.*?', line) or re.fullmatch('\s*', line)):
                            to.write(line + "\n")
                        if in_func and re.fullmatch('\S[a-zA-Z0-9]*.*', line):
                            to.write("\n")
                            in_func = False
                        if imprt and not in_func: to.write(line + "\n")
                        if func:
                            to.write("\n\n" + line + "\n")
                            in_func = True

                    to.write("\n")
                    to.close()
            f.close()
        
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise

    if os.path.isdir(from_file):
        if OVWR:
            if os.path.exists(to_file): os.remove(to_file)
        files = [from_file + f for f in os.listdir(from_file) if re.fullmatch(r, f) and f.endswith('.py') and f != to_file and os.path.abspath(f) != this]
        for f in files:
            write(f, to_file)
    elif os.path.isfile(from_file):
        assert from_file.endswith('.py')
        
        write(from_file, to_file, OVWR=OVWR)


if __name__ == '__main__':
    main()