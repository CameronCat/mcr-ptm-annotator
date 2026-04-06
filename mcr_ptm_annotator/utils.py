
from __future__ import annotations
from pathlib import Path
from typing import Iterator

AMINO_ACIDS = set("ACDEFGHIKLMNPQRSTVWY")


def parse_fasta(path: str | Path) -> Iterator[tuple[str, str]]:
    path = Path(path)
    current_id: str | None = None
    buffer: list[str] = []

    with path.open() as fh:
        for raw_line in fh:
            line = raw_line.strip()
            if not line or line.startswith(";"):
                continue
            if line.startswith(">"):
                if current_id is not None:
                    yield current_id, "".join(buffer)
                current_id = line[1:].split()[0]
                buffer = []
            else:
                buffer.append(line.upper())

    if current_id is not None:
        yield current_id, "".join(buffer)


DNA_CHARS = set("ATCGNU")


def is_protein_sequence(seq: str) -> bool:
    cleaned = seq.upper().replace(" ", "").replace("\n", "")
    if not cleaned:
        return False
    if all(c in DNA_CHARS for c in cleaned):
        return False
    return all(c in AMINO_ACIDS for c in cleaned)
