#!/usr/bin/env python3
"""
Simple converter for standalone PlantUML files to PNG or SVG.

Usage:
    python convert_puml.py <file.puml> [--format png|svg] [--output-dir out/]
"""

import sys
import subprocess
import os
from pathlib import Path

def find_plantuml_jar() -> str:
    """Search for plantuml.jar in common locations."""
    common_paths = [
        'plantuml.jar',
        '/usr/local/bin/plantuml.jar',
        '/usr/share/plantuml/plantuml.jar',
        os.path.expanduser('~/plantuml.jar'),
        os.path.expanduser('~/bin/plantuml.jar'),
    ]

    for path in common_paths:
        if os.path.exists(path):
            return path

    # Check environment variable
    plantuml_path = os.environ.get('PLANTUML_JAR')
    if plantuml_path and os.path.exists(plantuml_path):
        return plantuml_path

    return ''

def convert_puml(puml_file: str, format: str = 'png', output_dir: str = None) -> bool:
    """
    Convert a .puml file to image format.

    Args:
        puml_file: Path to .puml file
        format: 'png' or 'svg'
        output_dir: Optional output directory

    Returns:
        True if successful, False otherwise
    """
    plantuml_jar = find_plantuml_jar()
    if not plantuml_jar:
        print("ERROR: plantuml.jar not found. Please download from https://plantuml.com/download")
        print("You can set PLANTUML_JAR environment variable to specify the location.")
        return False

    format_flag = '--svg' if format == 'svg' else '--png'
    cmd = ['java', '-jar', plantuml_jar, format_flag]

    if output_dir:
        Path(output_dir).mkdir(exist_ok=True, parents=True)
        cmd.extend(['--output-dir', output_dir])

    cmd.append(puml_file)

    print(f"Converting {puml_file} to {format.upper()}...")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"ERROR: {result.stderr}")
        return False

    output_name = Path(puml_file).stem + f".{format}"
    if output_dir:
        output_path = Path(output_dir) / output_name
    else:
        output_path = Path(puml_file).parent / output_name

    print(f"✅ Created: {output_path}")
    return True

def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python convert_puml.py <file.puml> [--format png|svg] [--output-dir out/]")
        sys.exit(1)

    puml_file = sys.argv[1]
    format = 'png'
    output_dir = None

    # Parse optional arguments
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == '--format' and i + 1 < len(sys.argv):
            format = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == '--output-dir' and i + 1 < len(sys.argv):
            output_dir = sys.argv[i + 1]
            i += 2
        else:
            i += 1

    if not os.path.exists(puml_file):
        print(f"ERROR: File not found: {puml_file}")
        sys.exit(1)

    if format not in ['png', 'svg']:
        print(f"ERROR: Invalid format '{format}'. Use 'png' or 'svg'")
        sys.exit(1)

    success = convert_puml(puml_file, format, output_dir)
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
