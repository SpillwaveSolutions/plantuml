#!/usr/bin/env python3
"""
Extract PlantUML diagrams from markdown files, convert to images, and update markdown with image links.

Usage:
    python extract_and_convert_puml.py <markdown_file> [--format png|svg] [--output-dir images/]
"""

import re
import sys
import subprocess
import os
from pathlib import Path
from typing import List, Tuple

def extract_puml_blocks(markdown_content: str) -> List[Tuple[str, str]]:
    """
    Extract all ```puml code blocks from markdown content.

    Returns:
        List of (block_content, full_match) tuples
    """
    pattern = r'```puml\n(.*?)```'
    matches = re.finditer(pattern, markdown_content, re.DOTALL)
    return [(match.group(1), match.group(0)) for match in matches]

def generate_diagram_name(index: int, content: str) -> str:
    """
    Generate a descriptive name for the diagram based on content.

    Falls back to diagram_{index} if no clear name found.
    """
    # Try to extract diagram type from @start tag
    type_match = re.search(r'@start(\w+)', content)
    if type_match:
        diagram_type = type_match.group(1)
        return f"diagram_{index}_{diagram_type}"

    return f"diagram_{index}"

def convert_puml_to_image(puml_content: str, output_path: str, format: str = 'png') -> bool:
    """
    Convert PlantUML content to an image file using plantuml.jar.

    Args:
        puml_content: PlantUML diagram source code
        output_path: Path to output image (without extension)
        format: 'png' or 'svg'

    Returns:
        True if successful, False otherwise
    """
    # Find plantuml.jar
    plantuml_jar = find_plantuml_jar()
    if not plantuml_jar:
        print("ERROR: plantuml.jar not found. Please download it from https://plantuml.com/download")
        return False

    # Create temp .puml file
    temp_puml = f"{output_path}.puml"
    try:
        with open(temp_puml, 'w', encoding='utf-8') as f:
            f.write(puml_content)

        # Convert to image
        format_flag = '--svg' if format == 'svg' else '--png'
        cmd = ['java', '-jar', plantuml_jar, format_flag, temp_puml]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            print(f"ERROR converting {temp_puml}: {result.stderr}")
            return False

        # Clean up temp .puml file
        os.remove(temp_puml)
        return True

    except Exception as e:
        print(f"ERROR: {e}")
        if os.path.exists(temp_puml):
            os.remove(temp_puml)
        return False

def find_plantuml_jar() -> str:
    """
    Search for plantuml.jar in common locations.

    Returns:
        Path to plantuml.jar or empty string if not found
    """
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

    # Check PATH for plantuml.jar
    plantuml_path = os.environ.get('PLANTUML_JAR')
    if plantuml_path and os.path.exists(plantuml_path):
        return plantuml_path

    return ''

def process_markdown_file(markdown_path: str, output_dir: str = 'images/', format: str = 'png') -> None:
    """
    Extract all PlantUML diagrams from markdown, convert to images, and update markdown.

    Args:
        markdown_path: Path to markdown file
        output_dir: Directory to save images (relative to markdown file)
        format: 'png' or 'svg'
    """
    # Read markdown
    with open(markdown_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract PlantUML blocks
    blocks = extract_puml_blocks(content)

    if not blocks:
        print(f"No PlantUML blocks found in {markdown_path}")
        return

    print(f"Found {len(blocks)} PlantUML diagrams")

    # Create output directory
    md_dir = Path(markdown_path).parent
    img_dir = md_dir / output_dir
    img_dir.mkdir(exist_ok=True)

    # Process each block
    updated_content = content
    for index, (block_content, full_match) in enumerate(blocks, 1):
        # Generate diagram name
        diagram_name = generate_diagram_name(index, block_content)

        # Convert to image
        output_path = img_dir / diagram_name
        print(f"Converting diagram {index}/{len(blocks)}: {diagram_name}")

        success = convert_puml_to_image(block_content, str(output_path), format)

        if success:
            # Generate image link
            ext = 'svg' if format == 'svg' else 'png'
            image_link = f"![{diagram_name}]({output_dir}{diagram_name}.{ext})"

            # Replace code block with image link
            updated_content = updated_content.replace(full_match, image_link, 1)
            print(f"  ✅ Created {diagram_name}.{ext}")
        else:
            print(f"  ❌ Failed to convert diagram {index}")

    # Write updated markdown
    output_path = markdown_path.replace('.md', f'_with_images.md')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print(f"\n✅ Updated markdown saved to: {output_path}")

def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python extract_and_convert_puml.py <markdown_file> [--format png|svg] [--output-dir images/]")
        sys.exit(1)

    markdown_file = sys.argv[1]
    format = 'png'
    output_dir = 'images/'

    # Parse optional arguments
    for i, arg in enumerate(sys.argv[2:], 2):
        if arg == '--format' and i + 1 < len(sys.argv):
            format = sys.argv[i + 1]
        elif arg == '--output-dir' and i + 1 < len(sys.argv):
            output_dir = sys.argv[i + 1]

    if not os.path.exists(markdown_file):
        print(f"ERROR: File not found: {markdown_file}")
        sys.exit(1)

    if format not in ['png', 'svg']:
        print(f"ERROR: Invalid format '{format}'. Use 'png' or 'svg'")
        sys.exit(1)

    process_markdown_file(markdown_file, output_dir, format)

if __name__ == '__main__':
    main()
