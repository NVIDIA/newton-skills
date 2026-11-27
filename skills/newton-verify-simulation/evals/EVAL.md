# Evaluating simulation verification

Score the checks the agent selects, the measurements it obtains, and the
claims those measurements support. Credit equivalent methods. Score routing
separately using the expected skill for each case.

The insertion case supplies the same CPU rollout and recorded CSV to both
evaluation arms. The user supplies the travel and endpoint requirements. Run
a numerical check on the trajectory, including intermediate samples. The
expected outcomes and first violating step are recorded in the case assertions.
The fixture models one translation axis. It supplies no contact or hardware
measurements.

To reproduce the recording with the released Newton 1.7.0 wheel, run from
this directory:

```sh
python files/insertion.py /tmp/insertion.csv
diff -u files/insertion.csv /tmp/insertion.csv
```

For claims of improved performance, follow the repository comparison protocol.
Run at least three paired attempts per case on Codex and Claude Code. Keep the
input files and environment identical across arms and record per-case
correctness, elapsed time, total tokens, and variability.
