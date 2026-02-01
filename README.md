# Rename Video

A Python CLI tool that batch renames video files based on their creation time, applying a consistent naming pattern.

## Features

- 📁 Batch rename files in a directory
- ⏱️ Sort by creation time
- 🏷️ Custom naming pattern with sequential numbering
- 🔍 Filter files by text in filename
- 📂 Optional output directory
- 🧪 Dry run mode for preview

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
# Basic usage
python renamevideo.py /path/to/videos "NewName"

# With filter
python renamevideo.py /path/to/videos "ProjectA" --filter "clip"

# Output to different directory
python renamevideo.py /path/to/videos "ProjectA" --outdir /path/to/output

# Dry run (preview only)
python renamevideo.py /path/to/videos "ProjectA" --dry_run
```

## Arguments

| Argument | Description |
|----------|-------------|
| `directory` | Directory containing video files |
| `new_name` | New filename pattern |
| `--filter` | Only rename files containing this text |
| `--outdir` | Output directory for renamed files |
| `--dry_run` | Preview changes without renaming |

## Example

```bash
# Before:
# clip001.mp4, clip002.mp4, clip003.mp4

$ python renamevideo.py ./videos "Interview" --dry_run

# Preview output:
# Would rename: clip001.mp4 -> Interview-1.mp4
# Would rename: clip002.mp4 -> Interview-2.mp4
# Would rename: clip003.mp4 -> Interview-3.mp4

# Execute:
$ python renamevideo.py ./videos "Interview"

# After:
# Interview-1.mp4, Interview-2.mp4, Interview-3.mp4
```

## License

MIT License - see [LICENSE](LICENSE) for details.
