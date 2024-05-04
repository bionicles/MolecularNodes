import MDAnalysis as mda
import MDAnalysis.coordinates.base as base
from itertools import islice
import numpy as np


class OXDNAReader(base.ReaderBase):
    def __init__(self, filename, **kwargs):

        super(OXDNAReader, self).__init__(filename, **kwargs)
        oxfile = self._oxdna_file = mda.lib.util.anyopen(filename, 'r')
        self.n_atoms = 0
        self.meta_line_length = 0

        oxfile.seek(0)

        # quickly scan through the first frame and see how many atoms and meta lines there
        # are going to be

        first_meta_lines = True
        for line in oxfile:
            if "=" in line:
                if not first_meta_lines:
                    break
                self.meta_line_length += 1
                continue
            else:
                first_meta_lines = False

            self.n_atoms += 1

    def _read_next_timestep():
        pass

    def _reopen():
        pass

    def _read_frame(self, frame):
        start = (self.n_atoms + 3) * frame + 3
        end = start + self.n_atoms

        self._oxdna_file.seek(0)
        lines = list(islice(self._oxdna_file, start, end))
        arr = np.loadtxt(lines)
        return arr


def main():
    fl = 'C:\\Users\\BradyJohnston\\git\\MolecularNodes\\tests\\data\\oxdna\\holliday.dat'

    traj = OXDNAReader(fl)
    print(traj._read_frame(0))
    print(traj._read_frame(5))


if __name__ == "__main__":
    main()
