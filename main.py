#!/usr/bin/env python3
"""Satu kata untuk mantan, ditulis ke sebuah berkas.

Program kecil ini tidak meminta masukan apa pun dan tidak mencetak
apa pun ke layar. Ia hanya menyimpan satu kata pilihan ke dalam
berkas bernama entry.txt, di dalam folder keluaran yang ditentukan
oleh lingkungan. Kata itu sengaja ditulis apa adanya, tanpa baris
baru di ujungnya, supaya berkas hasil akhirnya berisi tepat kata
tersebut dan tidak ada tambahan lain.
"""

import os

WORD = "knockoff"


def main():
    """Tulis kata yang dipilih ke entry.txt di folder keluaran."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    tujuan = os.path.join(folder, "entry.txt")
    with open(tujuan, "w", encoding="utf-8") as berkas:
        berkas.write(WORD)


if __name__ == "__main__":
    main()
