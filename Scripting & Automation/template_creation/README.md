# Template Creation Tool for THM Challenge Documentation

This project provides an interactive Python CLI tool to automate the creation of structured markdown documentation for TryHackMe (THM) cybersecurity challenges. It’s designed to streamline and standardize your challenge write-ups — perfect for building a clear, organized cybersecurity portfolio.

## Features

- Interactive input prompts for challenge metadata (name, date, category, difficulty, etc.)
- Dynamic markdown template generation
- Auto-generation of task sections
- Directory selection for saving files
- Automatic creation of a `screenshots/` subfolder
- Extendable and customizable template structure

## Project Structure

```
cybersecurity-portfolio/
├── Scripting & Automation/
│   └── template_creation/
│       ├── base_template.md
│       ├── create_template_thm_challenge.py
│       └── README.md
├── SOC-Analyst/
│   └── ...
├── General notes & cheatsheets/
│   └── ...
├── ...
└── README.md
```

---

## Example: Template vs. Generated Output

Below is a comparison between the base template (before running the script) and an example of the generated output (after execution with sample inputs):

### Base Template

```markdown
# !challenge_name!

> **Date**: !completion_date!<br>
> !category!
> **Difficulty**: !difficulty!<br>
> **Reference**: !reference!<br>

--- 

## Summary
_TODO: Briefly describe the challenge objective and context

---

## Tasks
_TODO: A challenge usually consists of several tasks. A subheading is created for each task, which consists of the task and approach.<br>
!tasks!

---

## Tools and commands used
_TODO: List tools
```

---

### Example Output

```markdown
# Snort Challenge - The Basics

> **Date**: 2025-05-29<br>
> **Categories**: SOC | Tool | Sniffing | Analyzing<br>
> **Difficulty**: ~~Unknown~~ | ~~Easy~~ | Medium | ~~Hard~~ <br>
> **Reference**: https://tryhackme.com/room/snortchallenges1<br>

--- 

## Summary
_TODO: Briefly describe the challenge objective and context

---

## Tasks
_TODO: A challenge usually consists of several tasks. A subheading is created for each task, which consists of the task and approach.<br>

### Writing IDS Rules (HTTP)  
#### Approach

### Writing IDS Rules (FTP)  
#### Approach

### Writing IDS Rules(PNG)  
#### Approach

### Writing IDS Rules (Torrent Metafile)  
#### Approach

### Troubleshooting Rule Syntax Errors  
#### Approach

### Using External Rules (MS17-010)  
#### Approach

### Using External Rules (Log4j)  
#### Approach

---

## Tools and commands used
_TODO: List tools
```

---

## Notes

- All template placeholders (e.g., `!challenge_name!`, `!tasks!`) are dynamically replaced based on your inputs.
- The generated `.md` file is saved to the selected directory, alongside a `screenshots/` folder for image assets.
- Feel free to further customize the base template to suit your documentation style.

---

## License

MIT – feel free to use, adapt, and contribute.
