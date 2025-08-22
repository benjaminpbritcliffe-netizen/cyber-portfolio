# Copilot Instructions for Cyber Portfolio

This repository is a structured, content-rich knowledge base for cybersecurity,
programming, and ethical hacking. To be productive as an AI coding agent in this
codebase, follow these guidelines:

## Architecture & Structure

- The repo is organized by topic, not by code type. Each top-level folder
  represents a knowledge domain or skill area:
  - `Computer Fundamentals/`: Hardware, OS, and IT basics
  - `Cyber Events Archive/`: Analyses of major cyber incidents
  - `Cyber Laws & Ethics/`: Legal and ethical research
  - `Cyber Security/`: Security notes, projects, and resources
  - `House Of Vokabel/`: Vocabulary and key terms
  - `Images/`: Visual aids (diagrams, screenshots)
  - `Java/`, `Python/`, `Programming Fundamentals/`: Language-specific notes,
    scripts, and projects
  - `Scripts/`, `Tools/`: Automation, security tools, and utilities
  - `Tryhackme/`: Lab write-ups and progress

## Key Patterns & Conventions

- **Notes and Write-ups**: Most content is in Markdown (`.MD`) files. Use clear
  section headings, bullet points, and code blocks for clarity.
- **Scripts and Tools**: Place code in the relevant language or tools folder.
  Include a short header comment describing purpose and usage.
- **Case Studies**: For new cyber event analyses, add a new Markdown file in
  `Cyber Events Archive/` with a date and descriptive title.
- **Vocabulary**: Add new terms to `House Of Vokabel/` as individual Markdown
  files or append to existing ones.
- **Images**: Store diagrams/screenshots in `Images/` and reference them in
  notes using relative paths.

## Workflows

- **Adding Content**: Place new notes, scripts, or tools in the correct folder.
  Use descriptive filenames and update any relevant index or summary files.
- **Cross-linking**: When referencing concepts across folders, use relative
  Markdown links for easy navigation.
- **Updating**: When expanding a topic, append to the relevant file or create a
  new one if the topic is distinct.

## Examples

- To document a new cyber incident, create
  `Cyber Events Archive/Incident-Name-Year.md` and summarize the event, impact,
  and lessons learned.
- To add a Python script for password generation, place it in `Python/` with a
  header comment and usage example.
- To expand the vocabulary, add a new Markdown file in `House Of Vokabel/` or
  update an existing one.

## Integration Points

- No external build, test, or deployment systems are present. This is a
  content-first, documentation-driven repository.
- Scripts and tools are for local, educational, or demonstration use only.

For more details, see the main `README.md` and folder-level documentation.
