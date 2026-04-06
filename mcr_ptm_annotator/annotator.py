
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .ptm_database import KNOWN_PTMS, KnownPTM
from .utils import parse_fasta


_MARBURGENSIS_MCRA_LENGTH = 553

_POSITION_WINDOW = 30


@dataclass
class PTMHit:

    ptm: KnownPTM
    query_position: int
    residue: str
    expected_position: int
    position_delta: int
    confidence: str
    notes: list[str] = field(default_factory=list)

    def __repr__(self) -> str:
        return (
            f"<PTMHit {self.ptm.name} at pos={self.query_position} "
            f"({self.residue}) conf={self.confidence}>"
        )


class McrAPTMAnnotator:

    def __init__(
        self,
        position_window: int = _POSITION_WINDOW,
        require_residue_match: bool = True,
    ) -> None:
        self.position_window = position_window
        self.require_residue_match = require_residue_match


    def annotate_sequence(
        self,
        sequence: str,
        seq_id: str = "input",
    ) -> list[PTMHit]:
        sequence = sequence.upper().strip()
        seq_len = len(sequence)
        hits: list[PTMHit] = []

        for ptm in KNOWN_PTMS:
            expected = self._scale_position(
                ptm.position_marburgensis, seq_len
            )
            candidates = self._find_candidates(sequence, ptm, expected)
            hits.extend(candidates)

        hits.sort(key=lambda h: h.query_position)
        return hits

    def annotate_fasta(
        self,
        fasta_path: str,
    ) -> dict[str, list[PTMHit]]:
        results: dict[str, list[PTMHit]] = {}
        for seq_id, sequence in parse_fasta(fasta_path):
            results[seq_id] = self.annotate_sequence(sequence, seq_id=seq_id)
        return results


    def _scale_position(self, ref_position: int, query_length: int) -> int:
        scaled = round(ref_position * query_length / _MARBURGENSIS_MCRA_LENGTH)
        return max(1, min(scaled, query_length))

    def _find_candidates(
        self,
        sequence: str,
        ptm: KnownPTM,
        expected_pos: int,
    ) -> list[PTMHit]:
        lo = max(0, expected_pos - self.position_window - 1)
        hi = min(len(sequence), expected_pos + self.position_window)
        window_seq = sequence[lo:hi]

        hits: list[PTMHit] = []
        for i, aa in enumerate(window_seq):
            query_pos = lo + i + 1
            if self.require_residue_match and aa != ptm.residue_type:
                continue

            delta = query_pos - expected_pos
            confidence = self._confidence(delta)

            notes = [
                f"Reference position: {ptm.residue_type}{ptm.position_marburgensis} "
                f"in M. marburgensis (PDB 1MRO)",
                f"Scaled expected position in query: {expected_pos}",
            ]
            if abs(delta) > 15:
                notes.append(
                    "Position is >15 residues from expected — verify by "
                    "alignment against PDB 1MRO chain A"
                )

            hits.append(PTMHit(
                ptm=ptm,
                query_position=query_pos,
                residue=aa,
                expected_position=expected_pos,
                position_delta=delta,
                confidence=confidence,
                notes=notes,
            ))

        if len(hits) > 1:
            hits = [min(hits, key=lambda h: abs(h.position_delta))]

        return hits

    def _confidence(self, delta: int) -> str:
        abs_delta = abs(delta)
        if abs_delta <= 10:
            return "high"
        elif abs_delta <= 20:
            return "moderate"
        else:
            return "low"
