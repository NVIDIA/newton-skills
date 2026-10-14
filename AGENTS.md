# Contributor Agent Guidance

- Read [the skill policy](README.md#skill-policy) and [CONTRIBUTING.md](CONTRIBUTING.md).
- Keep public user skills in `skills/`; do not edit generated benchmarks, cards,
  or signatures. Request fresh validation after changing signed skill content.
- Preserve third-party notices and register each new file's actual attribution.
  Do not apply NVIDIA copyright to third-party material.
- Run `uv run --no-project --python 3.12 --with reuse==6.2.0 reuse lint`,
  `sha256sum --check .github/license-checksums.sha256`, and
  `uv run --no-project --python 3.12 --with reuse==6.2.0 python -m unittest discover -s tests`.
- Sign off commits with `git commit -s`. Check a commit range with
  `uv run --no-project --python 3.12 python scripts/check_dco.py BASE HEAD`.
