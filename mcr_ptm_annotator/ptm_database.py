
from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class KnownPTM:
    name: str
    residue_type: str
    position_marburgensis: int
    modification: str
    pdb_code: str
    references: tuple
    notes: str = ""


KNOWN_PTMS: tuple[KnownPTM, ...] = (

    KnownPTM(
        name="thioglycine",
        residue_type="G",
        position_marburgensis=445,
        modification="Thioamidation: backbone carbonyl oxygen replaced by sulfur",
        pdb_code="GL3",
        references=(
            "Ermler et al. (1997) Science 278:1457",
            "Nayak et al. (2017) eLife 6:e29218",
            "Nayak et al. (2020) PLoS Biol 18:e3000507",
        ),
        notes=(
            "Installed by YcaO/TfuA (ycaO-tfuA locus, Nayak 2017). "
            "In M. acetivorans this corresponds to Gly465. "
            "Loss causes severe growth defects on low-energy substrates "
            "and at elevated temperature (39-45°C, Nayak 2017). "
            "Conserved in all methanogens examined (Kahnt 2007)."
        ),
    ),

    KnownPTM(
        name="didehydroaspartate",
        residue_type="D",
        position_marburgensis=446,
        modification="Dehydration of aspartate: alpha-beta unsaturated amino acid",
        pdb_code="",
        references=(
            "Wagner et al. (2016) Angew Chem Int Ed Engl 55:10630",
            "Nayak et al. (2017) eLife 6:e29218",
        ),
        notes=(
            "Adjacent to thioglycine (Gly445). Identified in M. marburgensis "
            "MCR I and II and in M. barkeri by mass spectrometry and X-ray "
            "crystallography (PDB 5A0Y, Wagner 2016). "
            "Absent in M. wolfeii — dispensable but may fine-tune catalytic "
            "efficiency (Wagner 2016). "
            "In M. acetivorans, corresponds to Asp470 (Nayak 2017). "
            "NOT present in PDB 1MRO; use PDB 5A0Y as reference for this PTM."
        ),
    ),

    KnownPTM(
        name="1-N-methylhistidine",
        residue_type="H",
        position_marburgensis=257,
        modification="Methylation of the N1 nitrogen of the histidine imidazole ring",
        pdb_code="MHS",
        references=(
            "Ermler et al. (1997) Science 278:1457",
            "Kahnt et al. (2007) FEBS J 274:4913",
        ),
        notes=(
            "Conserved in all methanogens examined (Kahnt 2007). "
            "Biosynthetic enzyme not fully characterised as of 2024. "
            "Proposed to alter pKa and position the imidazole ring "
            "for coenzyme B binding (Grabarse et al. 2000)."
        ),
    ),

    KnownPTM(
        name="5-(S)-methylarginine",
        residue_type="R",
        position_marburgensis=271,
        modification="sp3-C methylation at the C-delta of arginine",
        pdb_code="AGM",
        references=(
            "Ermler et al. (1997) Science 278:1457",
            "Kahnt et al. (2007) FEBS J 274:4913",
            "Deobald et al. (2018) Sci Rep 8:7404",
        ),
        notes=(
            "Installed by the radical SAM methyltransferase encoded by mmpX "
            "(Deobald 2018). Present in all methanogens examined, absent in "
            "ANME-1 (Kahnt 2007). In M. maripaludis, the equivalent residue "
            "is Arg275; loss of methylation profoundly reduces methanogenesis "
            "and growth (Lyu et al. 2020 J Bacteriol 202:e00654-19)."
        ),
    ),

    KnownPTM(
        name="2-(S)-methylglutamine",
        residue_type="Q",
        position_marburgensis=400,
        modification="sp3-C methylation at the C-alpha of glutamine",
        pdb_code="MGN",
        references=(
            "Ermler et al. (1997) Science 278:1457",
            "Kahnt et al. (2007) FEBS J 274:4913",
            "Selmer et al. (2000) J Biol Chem 275:3755",
        ),
        notes=(
            "Absent in Methanosarcina barkeri (Selmer 2000, Lyu et al. 2018). "
            "Biosynthetic enzyme not fully characterised as of 2024."
        ),
    ),

    KnownPTM(
        name="S-methylcysteine",
        residue_type="C",
        position_marburgensis=452,
        modification="S-methylation of the cysteine thiol",
        pdb_code="SMC",
        references=(
            "Ermler et al. (1997) Science 278:1457",
            "Kahnt et al. (2007) FEBS J 274:4913",
            "Selmer et al. (2000) J Biol Chem 275:3755",
        ),
        notes=(
            "Variable: low abundance or absent in many methanogens, "
            "including M. maripaludis (Kahnt 2007). "
            "Present in M. marburgensis (PDB 1MRO). "
            "ANME-1 MCR shows a different PTM pattern at this position "
            "(Shima et al. 2012 Nature 481:98)."
        ),
    ),
)
