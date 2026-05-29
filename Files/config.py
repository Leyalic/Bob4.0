"""
All paths and settings for the Bob file-processing pipeline.
Change values here — nowhere else needs to be edited for path/env changes.
"""
import sys
from pathlib import Path

# ── Destination roots ──────────────────────────────────────────────────────
UOSFA_DIR        = Path("O:/UOSFA Reports")
TEST_UOSFA_DIR   = Path("C:/UOSFA Reports/Testing/Destination Folders")

# ── Archive/source roots ───────────────────────────────────────────────────
SYSTEMS_DIR      = Path("O:/Systems")
TEST_SYSTEMS_DIR = Path("C:/Testing Bob")

ACCT_DIR         = Path("O:/ACCT")
TEST_ACCT_DIR    = Path("C:/Testing Bob/ACCT")

DISB_FAIL_DIR    = Path("O:/Disbursement Failure")
TEST_DISB_FAIL   = Path("C:/Testing Bob")           # test disb-failure lives here

# Origination file folders
DL_ORIG_DIR      = SYSTEMS_DIR / "Direct Loans/Origination"
ALT_ORIG_DIR     = SYSTEMS_DIR / "QUERIES/ALT Loans"
TEST_DL_ORIG_DIR = TEST_SYSTEMS_DIR / "Direct Loans/Origination"
TEST_ALT_ORIG_DIR= TEST_SYSTEMS_DIR / "ALT Loans"

# ── Misc ───────────────────────────────────────────────────────────────────
def _app_root() -> Path:
    """Return the root directory for data files regardless of how the app is launched."""
    if getattr(sys, "frozen", False):
        # PyInstaller bundle: use the directory containing the exe
        return Path(sys.executable).parent
    # Development: two levels up from this file (Files/config.py → project root)
    return Path(__file__).parent.parent

_ROOT       = _app_root()
DICT_PATH   = _ROOT / "Files" / "Query_Dictionary.csv"
IGNORE_PATH = _ROOT / "Files" / "Ignore_List.txt"
LOG_DIR     = _ROOT / "logs"

# ── File-filter lists ──────────────────────────────────────────────────────
# Files whose name contains any of these strings are skipped entirely
SKIP_CONTAINS = [".zip", ".lnk", " DL ORIG ", " ALT Loan ORIG ", "idsa", "igsa", "igco", "igsg"]

# Files matching any of these patterns are deleted from the source folder
REMOVE_PATTERNS = [
    "FASTDVER",
    "FINAID_Checklist",
    "ussfa09",
    "USSFA090 Reset",
    "O-A",
    r"uosfa[0-9]+[a-zA-Z]*\.csv",
]
