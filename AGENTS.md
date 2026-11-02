# Contributor Agent Guidance

- Read [the skill policy](README.md#skill-policy) and [CONTRIBUTING.md](CONTRIBUTING.md).
- Keep public user skills in `skills/`; do not edit generated benchmarks, cards,
  or signatures. Request fresh validation after changing signed skill content.
- Preserve third-party notices and actual attribution. Never assign NVIDIA
  copyright to imported material. IP and license rights require maintainer review.
- Match validation to the change under the skill policy; report checks performed
  and limitations. CI results do not replace maintainer assessment of usefulness
  and correctness.
- Run `uv run --no-project --python 3.12 --with reuse==5.1.1 reuse lint`,
  `sha256sum --check .github/license-checksums.sha256`, and
  `uv run --no-project --python 3.12 --with reuse==5.1.1 python -m unittest discover -s tests`.
- Sign off commits with `git commit -s`.
