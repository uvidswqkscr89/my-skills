#!/usr/bin/env python3
"""
Test Case Markdown to CSV Converter

Converts test case Markdown files to CSV format for import into test management systems.
Requires Python 3.6+ (uses standard library only)
"""

import re
import csv
import sys
import os
from pathlib import Path


def parse_markdown_to_csv(md_file, csv_file):
    """
    Parse test cases from Markdown file and export to CSV.

    Args:
        md_file: Path to input Markdown file
        csv_file: Path to output CSV file
    """
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: Markdown file not found: {md_file}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading Markdown file: {e}", file=sys.stderr)
        sys.exit(1)

    # Split by "### " to get test case chunks
    chunks = re.split(r'\n### ', content)

    test_cases = []

    for chunk in chunks:
        # Only process chunks that start with TC-
        if not chunk.strip().startswith('TC-'):
            continue

        lines = chunk.split('\n')
        header = lines[0].strip()

        # Parse Header: TC-ID: Title [Tags...]
        # Example: TC-001: Create new user [happy_path] [P0]
        # Example: TC-Smoke-001: Verify page loads [Happy Path] [P0]

        id_match = re.match(r'(TC-[\w-]+):\s*(.*)', header)
        if not id_match:
            continue

        tc_id = id_match.group(1)
        rest = id_match.group(2)

        # Extract Priority (P0, P1, P2)
        priority = "P2"  # Default
        p_match = re.search(r'\[(P[0-4])\]', rest)
        if p_match:
            priority = p_match.group(1)
            # Remove from title
            rest = rest.replace(p_match.group(0), '')

        # Extract Type (happy_path, validation, edge_case, negative, etc.)
        tc_type = "Functional"
        # Match [type] or (type) - case insensitive
        t_match = re.search(
            r'[\[\(](happy_path|validation|edge_case|negative|security|functional)[\]\)]',
            rest,
            re.IGNORECASE
        )
        if t_match:
            tc_type = t_match.group(1)
            # Remove from title
            rest = rest.replace(t_match.group(0), '')

        title = rest.strip()

        # Body extraction
        body = '\n'.join(lines[1:])

        # Extract Preconditions
        pre_match = re.search(
            r'\*\*Preconditions?\*\*：?\s*(.*?)\s*(?=\*\*Test Steps?\*\*|$)',
            body,
            re.DOTALL
        )
        preconditions = pre_match.group(1).strip() if pre_match else ""
        # Remove leading dashes from bullet points
        preconditions = re.sub(r'^-\s+', '', preconditions, flags=re.MULTILINE).strip()

        # Extract Test Steps
        steps_match = re.search(
            r'\*\*Test Steps?\*\*：?\s*(.*?)\s*(?=\*\*Expected Results?\*\*|$)',
            body,
            re.DOTALL
        )
        steps = steps_match.group(1).strip() if steps_match else ""

        # Extract Expected Result
        res_match = re.search(
            r'\*\*Expected Results?\*\*：?\s*(.*?)\s*(?=\n---|(?:\n###)|$)',
            body,
            re.DOTALL
        )
        result = res_match.group(1).strip() if res_match else ""
        # Remove leading dashes from bullet points
        result = re.sub(r'^-\s+', '', result, flags=re.MULTILINE).strip()

        test_cases.append({
            'ID': tc_id,
            'Title': title,
            'Type': tc_type,
            'Priority': priority,
            'Preconditions': preconditions,
            'Steps': steps,
            'Expected Result': result
        })

    if not test_cases:
        print(f"Warning: No test cases found in {md_file}", file=sys.stderr)
        return

    # Write to CSV
    keys = ['ID', 'Title', 'Type', 'Priority', 'Preconditions', 'Steps', 'Expected Result']
    try:
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(test_cases)

        print(f"✓ Exported {len(test_cases)} test cases to {csv_file}")
    except Exception as e:
        print(f"Error writing CSV file: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """Main entry point for command-line usage."""
    if len(sys.argv) < 2:
        print("Usage: convert_tc_md_to_csv.py <markdown_file> [csv_file]")
        print("\nExample:")
        print("  convert_tc_md_to_csv.py test_cases.md")
        print("  convert_tc_md_to_csv.py test_cases.md output.csv")
        sys.exit(1)

    md_path = sys.argv[1]

    # Generate CSV filename if not provided
    if len(sys.argv) >= 3:
        csv_path = sys.argv[2]
    else:
        # Replace .md extension with .csv
        csv_path = str(Path(md_path).with_suffix('.csv'))

    parse_markdown_to_csv(md_path, csv_path)


if __name__ == '__main__':
    main()
