#!/usr/bin/env python3
"""
Check PlantUML setup: Java, Graphviz, and plantuml.jar availability.

Usage:
    python check_setup.py
"""

import subprocess
import os
import sys
from pathlib import Path

def check_java() -> bool:
    """Check if Java is installed and accessible."""
    try:
        result = subprocess.run(['java', '-version'], capture_output=True, text=True)
        version_output = result.stderr  # Java outputs version to stderr
        print(f"✅ Java found: {version_output.splitlines()[0]}")
        return True
    except FileNotFoundError:
        print("❌ Java not found. Install from https://www.oracle.com/java/technologies/downloads/")
        return False

def check_graphviz() -> bool:
    """Check if Graphviz is installed and accessible."""
    try:
        result = subprocess.run(['dot', '-V'], capture_output=True, text=True)
        version_output = result.stderr  # dot outputs version to stderr
        print(f"✅ Graphviz found: {version_output.strip()}")
        return True
    except FileNotFoundError:
        print("❌ Graphviz not found. Install from https://graphviz.org/download/")
        return False

def check_plantuml_jar() -> tuple[bool, str]:
    """Check if plantuml.jar is accessible."""
    common_paths = [
        'plantuml.jar',
        '/usr/local/bin/plantuml.jar',
        '/usr/share/plantuml/plantuml.jar',
        os.path.expanduser('~/plantuml.jar'),
        os.path.expanduser('~/bin/plantuml.jar'),
    ]

    # Check environment variable first
    plantuml_path = os.environ.get('PLANTUML_JAR')
    if plantuml_path and os.path.exists(plantuml_path):
        print(f"✅ plantuml.jar found: {plantuml_path} (from PLANTUML_JAR env var)")
        return True, plantuml_path

    # Check common paths
    for path in common_paths:
        if os.path.exists(path):
            print(f"✅ plantuml.jar found: {path}")
            return True, path

    print("❌ plantuml.jar not found. Download from https://plantuml.com/download")
    print("   Common locations to place it:")
    print("   - ./plantuml.jar (current directory)")
    print("   - ~/plantuml.jar (home directory)")
    print("   - /usr/local/bin/plantuml.jar")
    print("   Or set PLANTUML_JAR environment variable")
    return False, ''

def test_plantuml(jar_path: str) -> bool:
    """Test PlantUML with a simple diagram."""
    test_diagram = """@startuml
Alice -> Bob: Test
@enduml"""

    try:
        # Test with pipe
        cmd = ['java', '-jar', jar_path, '-pipe', '--png']
        result = subprocess.run(cmd, input=test_diagram, capture_output=True, text=True)

        if result.returncode == 0:
            print("✅ PlantUML test successful")
            return True
        else:
            print(f"❌ PlantUML test failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ PlantUML test error: {e}")
        return False

def main():
    """Main entry point."""
    print("Checking PlantUML setup...\n")

    java_ok = check_java()
    graphviz_ok = check_graphviz()
    jar_ok, jar_path = check_plantuml_jar()

    print()

    if not java_ok or not jar_ok:
        print("❌ Setup incomplete. Please install missing components.")
        sys.exit(1)

    if not graphviz_ok:
        print("⚠️  Graphviz missing. Some diagrams may not render correctly.")
        print("   Install from https://graphviz.org/download/")

    # Test PlantUML if everything is available
    if java_ok and jar_ok:
        print("\nTesting PlantUML...")
        test_plantuml(jar_path)

    print("\n✅ PlantUML setup complete!")

if __name__ == '__main__':
    main()
