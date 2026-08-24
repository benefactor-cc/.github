#!/usr/bin/env python3
"""Validate the security-critical Benefactor platform integration policy."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

CAPABILITIES = {"observability", "sync", "authentication", "dependencies"}
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
COORDINATE_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+@\^[0-9]+\.[0-9]+\.[0-9]+$")
RESOLUTION_STATES = {"installable", "pending-public-registry"}


def fail(message: str) -> None:
    raise ValueError(message)


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    path = root / "architecture" / "platform-integrations.json"
    policy = json.loads(path.read_text(encoding="utf-8"))

    if policy.get("$schema") != "./platform-integrations.schema.json":
        fail("platform integration policy must reference its local schema")
    if policy.get("schema_version") != 1:
        fail("unsupported platform integration schema version")
    if policy.get("organization") != "benefactor-cc":
        fail("platform integration policy has the wrong organization")

    capabilities = policy.get("capabilities")
    if not isinstance(capabilities, dict) or set(capabilities) != CAPABILITIES:
        fail("policy must declare exactly the four reviewed capabilities")

    for name, capability in capabilities.items():
        source = capability.get("source", "")
        parsed = urlparse(source)
        if parsed.scheme != "https" or parsed.netloc != "github.com" or len(parsed.path.strip("/").split("/")) != 2:
            fail(f"{name}: source must be an https://github.com/owner/repository URL")
        if not SHA_RE.fullmatch(capability.get("audited_revision", "")):
            fail(f"{name}: audited_revision must be a full immutable Git SHA")
        coordinates = capability.get("package_coordinates")
        if not isinstance(coordinates, list) or not coordinates or len(coordinates) != len(set(coordinates)):
            fail(f"{name}: package_coordinates must be a non-empty unique list")
        if any(not COORDINATE_RE.fullmatch(value) for value in coordinates):
            fail(f"{name}: invalid Zed package coordinate")
        if capability.get("resolution_state") not in RESOLUTION_STATES:
            fail(f"{name}: invalid resolution_state")
        invariants = capability.get("invariants")
        if not isinstance(invariants, list) or not invariants or len(invariants) != len(set(invariants)):
            fail(f"{name}: invariants must be a non-empty unique list")

    role_requirements = policy.get("role_requirements")
    if not isinstance(role_requirements, dict) or not role_requirements:
        fail("role_requirements must not be empty")
    for role, requirements in role_requirements.items():
        if not isinstance(role, str) or not role:
            fail("role names must be non-empty strings")
        if not isinstance(requirements, list) or not requirements:
            fail(f"{role}: requirements must be a non-empty list")
        if len(requirements) != len(set(requirements)) or not set(requirements) <= CAPABILITIES:
            fail(f"{role}: requirements must be unique known capabilities")

    print(f"validated {path.relative_to(root)}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"platform integration validation failed: {error}", file=sys.stderr)
        raise SystemExit(1)
