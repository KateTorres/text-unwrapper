# Changelog

All notable changes to this project will be documented in this file.

## \[1.2.0] - 2025-07-05

### Added

* **Bracket number removal utility (`utils/bracket_number_remover.py`)**

  * Deletes bracketed tokens that are purely digits (e.g. `[3]`, `[007]`).
  * preserves paragraph breaks while joining lines that were split only by numeric references.
  * Removes `[n]`and adjacent whitespace.
  * Collapses single new‑lines to a space, but keeps true blank‑line boundaries (two or more consecutive `\n`).
  * Prevents “squished” output when the user selects *Remove numeric \[n] brackets only*.

* **Operation menu** allowing users to select between paragraph unwrapping, bracket removal, or both.

### Changed

* `main.py` updated to integrate the new utility and menu.

---

*Earlier releases existed but were not recorded in this log.*