# ZX Spectrum BASIC — Bug Fix TODO

## Bugs (gameplay / correctness)

- [ ] **Score not reset between games** (lines 80-90 vs line 810)
  - `SCORE` and `TOTAL` initialised once at startup; `GOTO 290` skips them on replay
  - Fix: add `LET SCORE = 0 : LET TOTAL = 0` just before the quiz loop starts (around line 490)

- [ ] **Answer strings truncated** — `DIM A$(20,4,20)` gives only 20 chars per answer
  - At least 6 answers exceed 20 chars (e.g. "A controlled environment for mushroom growth" = 44)
  - Answers display wrong; comparisons still pass by luck (both sides truncate equally)
  - Fix: increase last dimension to at least 45: `DIM A$(20,4,45)`

- [ ] **Correct-answer strings truncated** — `DIM C$(20,20)` same 20-char limit
  - Same answers stored here; displayed wrong in "WRONG! CORRECT ANSWER:" message
  - Fix: increase to `DIM C$(20,45)`

- [ ] **Explanation strings truncated** — `DIM E$(20,80)` gives 80 chars; 4 explanations are longer
  - E$(6)=92, E$(7)=90, E$(12)=89, E$(13)=84 — all cut off mid-sentence
  - Fix: increase to `DIM E$(20,96)` (next clean boundary)

## Dead code / minor issues

- [ ] **`TOTAL` variable is never displayed** — incremented at line 1408, unused in results
  - Either display it or remove it

- [ ] **Long strings wrap on 32-column display** — questions up to 60 chars, explanations up to 96
  - Not a crash bug, but looks rough; consider breaking long strings across two PRINT statements
  - Worst offenders: Q$(10), Q$(12), and several E$() entries

## Line reference summary

| Line(s)    | Issue                              |
|------------|------------------------------------|
| 80-90, 810 | Score not reset on replay          |
| 110        | `DIM Q$(20,60)` — fine             |
| 120        | `DIM A$(20,4,20)` — too narrow     |
| 130        | `DIM C$(20,20)` — too narrow       |
| 140        | `DIM E$(20,80)` — too narrow       |
| 1408       | `TOTAL` incremented, never used    |
| 1470       | Long E$() wraps on 32-col screen   |
