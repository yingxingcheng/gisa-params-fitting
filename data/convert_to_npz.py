#!/usr/bin/env python

import numpy as np
from horton import *

np.set_printoptions(precision=4, suppress=True, linewidth=np.inf)


def to_npz(record):
    weights = record.rgrid.weights
    radii = record.rgrid.radii
    number = record.number
    charge = record.charge
    rho = record.rho
    nelec = number - charge
    data = {
        "weights": weights,
        "radii": radii,
        "number": number,
        "charge": charge,
        "nelec": nelec,
        "rho": rho,
    }
    np.savez(f"../atom_{number}_{int(charge)}.npz", **data)


def main():
    db = ProAtomDB.from_file("atoms.h5")
    db_record_dict = {
        1: [0],
        3: [-2, -1, 0, 1, 2],
        6: [-2, -1, 0, 1, 2, 3],
        7: [-2, -1, 0, 1, 2, 3],
        8: [-2, -1, 0, 1, 2, 3],
        17: [-2, -1, 0, 1, 2, 3],
    }

    for Z, charges in db_record_dict.items():
        for Z, charge in zip([Z] * len(charges), charges):
            record = db.get_record(Z, charge)
            to_npz(record)


main()