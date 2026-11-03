"""Generate JSON schemas."""

import argparse
from pathlib import Path

from pyaml.validation import SchemaGenerator, SchemaRegistry


def generate_schemas(output_dir: Path) -> None:
    """Generate JSON schemas for registered accelerator configurations."""
    registry = SchemaRegistry()
    registry.discover()

    output_dir.mkdir(parents=True, exist_ok=True)

    SchemaGenerator.save(
        "pyaml.accelerator.Accelerator",
        output_dir / "accelerator.schema.json",
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    generate_schemas(args.output)