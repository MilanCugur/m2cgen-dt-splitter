import os
import re
import tqdm
import shutil
import argparse
from typing import List, Tuple

import config


class Splitter:
    """
    Split Sklearn's Classification/Regression DT (translated to Java via m2cgen) to subroutines.
    """

    def __init__(self, model_path: os.PathLike, leaf_template: str, inner_template: str, leaf_border: str, verbose: int) -> None:
        """
        Initialize templates for the subroutines generation also the threshold for the leaf function size.
        Additionally, instantiate basic internal resources (id generator and subroutines collector). 

        Use the DFS subroutines naming.
        """
        assert os.path.isfile(model_path) and model_path.endswith(
            '.java'), 'Fatal Error Splitter: invalid path to the DT java file.'
        self.model_path = model_path
        self.leaf_template = leaf_template
        self.inner_template = inner_template
        self.leaf_border = leaf_border
        self.verbose = verbose

        def get_id(verbose: int) -> int:
            """
            Return unique id.
            """
            id = 0
            while True:
                if verbose == 1:
                    print('Setting up subroutine {}..'.format(id))
                yield id
                id += 1
        self.get_id = get_id(self.verbose)
        self.subroutines = []

        self.suffix = '\n'

    def format_leaf(self, lines: List[str]) -> int:
        """
        Format leaf function.
        """
        id = self.get_id.__next__()
        self.subroutines.append(self.leaf_template.format(
            id, ''.join(list(map(lambda t: t.strip()+self.suffix, lines)))))
        return id

    def format_inner(self, lines: List[str]) -> int:
        """
        Format inner function.
        """
        if len(lines) < self.leaf_border:
            return self.format_leaf(lines)
        else:
            head_true, banch_true, head_false, branch_false, if_end = Splitter.split_lines(
                lines)
            id = self.get_id.__next__()
            id_true = self.format_inner(banch_true)
            id_false = self.format_inner(branch_false)
            self.subroutines.append(self.inner_template.format(
                id, head_true.strip(), id_true, head_false.strip(), id_false, if_end.strip()))
            return id

    @staticmethod
    def split_lines(lines: List[str]) -> Tuple[str, str, str, str, str]:
        """
        Split code to:
        * if (condition) {  [head_true]
        *   true branch     [branch_true]
        * } else {          [head_false]
        *   [false branch]  [branch_false]
        * }                 [if_end]
        """
        assert len(
            lines) >= 5, 'Fatal Error split_lines: cannot split the DT, size too small.'
        head_true = lines[0]
        if_end = lines[-1]
        i = Splitter.get_split_index(lines)
        head_false = lines[i]
        branch_true = lines[1:i]
        branch_false = lines[i+1:-1]

        return head_true, branch_true, head_false, branch_false, if_end

    @staticmethod
    def get_split_index(lines: List[str]) -> int:
        """
        Find most outer if-else within the DT.
        """
        assert lines[0].count(
            '{') == 1, 'Fatal Error get_split_index: invalid if_true DT part.'
        opened = 1
        for i in range(1, len(lines)):
            line = lines[i]
            for c in line:
                if c == '{':
                    opened += 1
                if c == '}':
                    opened -= 1
                if opened == 0:
                    return i
        assert False, 'Fatal Error get_split_index: cannot find split index.'

    def run(self) -> None:
        """
        Split code into the subroutines.

        Drop lines: 
              class_header = lines[0]
              method_header = lines[1]
              method_var = lines[2]
              method_return = lines[-3]
              method_footer = lines[-2]
              class_footer = lines[-1]
        Reason to require strict m2cgen file format!
        """
        with open(self.model_path, 'r') as f:
            lines = f.readlines()
            tree = lines[3:-3]
            self.format_inner(tree)

    def dump(self) -> os.PathLike:
        """
        Create output file.
        """
        extension = '.java'
        dump_path = os.sep.join(self.model_path.split(
            os.sep)[:-1]+[self.model_path.split(os.sep)[-1][:-5]+'Splitted'])
        if os.path.exists(dump_path):
            if self.verbose == 1:
                print('Warning: removing directory {}..'.format(dump_path))
            shutil.rmtree(dump_path)
        if self.verbose == 1:
            print('Creating output direcotry {}..'.format(dump_path))
        os.mkdir(dump_path)
        for subroutine in tqdm.tqdm(self.subroutines):
            class_name = re.search('public class ([a-zA-Z0-9]+) {', subroutine)
            assert class_name is not None, 'Fatal Error dump: cannot parse class name from subroutine data.'
            with open(os.path.join(dump_path, class_name.group(1)+extension), 'w') as f:
                f.write(subroutine)
        return os.path.abspath(dump_path)

    def exec(self) -> os.PathLike:
        """
        Split m2cgen created trees into separate sub-classes and sub-functions.
        """

        self.run()
        return self.dump()


if __name__ == '__main__':
    aparser = argparse.ArgumentParser(
        description='Solve Java code too large and too many constants errors.')
    aparser.add_argument('-v', '--version', action='version',
                         version='%(prog)s 0.0.1')
    aparser.add_argument('-model-path', nargs=1, metavar='path',
                         help='Path to the stored java model.')

    args = aparser.parse_args()
    model_path = args.model_path
    assert model_path is not None, 'Fatal Error: not existing model path.'
    model_path = model_path[0]
    assert os.path.isfile(model_path), 'Fatal Error: invalid model path.'

    splt = Splitter(model_path=model_path, leaf_template=config.LEAF_TEMPLATE,
                    inner_template=config.INNER_TEMPLATE, leaf_border=config.LEAF_BORDER,
                    verbose=config.VERBOSE)
    out_model_path = splt.exec()

    print('Splitted model are saved at the: \n{}'.format(
        os.path.abspath(out_model_path)))
