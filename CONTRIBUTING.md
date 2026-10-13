# Contributing to Newton Skills

Contributions are welcome, including improvements to skills, documentation,
and evaluation cases. Open an issue to discuss substantial changes, then submit
a pull request from a fork with a focused description and validation results.

## Scope and Validation

Target users of the released Newton wheel and public APIs. Keep stable product
knowledge in Newton's documentation; skills should route agents to it and provide
brief task workflows. Preserve version awareness, keep a source checkout optional,
and refer only to publicly available tools.

Check the skill format against the [Agent Skills specification](https://agentskills.io/specification).
Verify documentation links and example commands against the intended Newton
release. Describe the checks performed and anything not exercised. Changes that
are published to the catalog also need functional evaluation and the required
validation and signing artifacts.

## Licensing and Attribution

By submitting a contribution, you agree to license it under the applicable terms
in [LICENSE](LICENSE): CC-BY-4.0 for documentation, skills, and assets; Apache-2.0
for code-only files. Preserve existing copyright, license, and attribution
notices. Disclose third-party material and its origin, and update
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) with the applicable licenses.

New NVIDIA-authored code-only files use the following header, with the actual
copyright year and appropriate comment syntax:

```python
# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
```

Documentation and Markdown skill files do not need a copyright/license header;
the top-level license and notices apply. Preserve third-party headers verbatim.

## Review and Publication

Maintainers review scope, correctness, validation, licensing, attribution, and
DCO sign-offs. NVIDIA maintainers must complete the required IP review for all
material, including external contributions, before public distribution. A DCO
sign-off does not replace that review. Public release also requires the project's
release approvals; catalog publication requires validation and signing.

Report security vulnerabilities privately using [SECURITY.md](SECURITY.md).
Treat contributors respectfully and keep review discussions constructive.

#### Signing Off Your Work

* We require that all contributors "sign-off" on their commits. This certifies that the contribution is your original work, or you have rights to submit it under the same license, or a compatible license.

  * Any contribution which contains commits that are not Signed-Off will not be accepted.

* To sign off on a commit you simply use the `--signoff` (or `-s`) option when committing your changes:
  ```bash
  $ git commit -s -m "Add cool feature."
  ```
  This will append the following to your commit message:
  ```
  Signed-off-by: Your Name <your@email.com>
  ```

* Full text of the DCO (https://developercertificate.org/):

  ```
    Developer Certificate of Origin
    Version 1.1

    Copyright (C) 2004, 2006 The Linux Foundation and its contributors.

    Everyone is permitted to copy and distribute verbatim copies of this
    license document, but changing it is not allowed.


    Developer's Certificate of Origin 1.1

    By making a contribution to this project, I certify that:

    (a) The contribution was created in whole or in part by me and I
        have the right to submit it under the open source license
        indicated in the file; or

    (b) The contribution is based upon previous work that, to the best
        of my knowledge, is covered under an appropriate open source
        license and I have the right under that license to submit that
        work with modifications, whether created in whole or in part
        by me, under the same open source license (unless I am
        permitted to submit under a different license), as indicated
        in the file; or

    (c) The contribution was provided directly to me by some other
        person who certified (a), (b) or (c) and I have not modified
        it.

    (d) I understand and agree that this project and the contribution
        are public and that a record of the contribution (including all
        personal information I submit with it, including my sign-off) is
        maintained indefinitely and may be redistributed consistent with
        this project or the open source license(s) involved.
  ```
