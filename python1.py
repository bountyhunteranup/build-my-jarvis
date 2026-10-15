import hashlib
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set

# Supported audio formats (lowercase)
AUDIO_EXTENSIONS: Set[str] = {'.mp3', '.flac', '.wav', '.m4a', '.aac', '.ogg', '.wma'}

def get_file_hash(filepath: Path, chunk_size: int = 65536) -> str:
    """
    Computes the SHA-256 hash of a file in chunks to keep memory usage constant,
    even for massive lossless audio files.
    """
    hasher = hashlib.sha256()
    try:
        with filepath.open('rb') as f:
            while chunk := f.read(chunk_size):
                hasher.update(chunk)
        return hasher.hexdigest()
    except (PermissionError, OSError) as e:
        print(f"[WARN] Could not read {filepath}: {e}")
        return ""

def find_duplicate_music(root_folder: Path) -> Dict[str, List[Path]]:
    """
    Two-stage duplicate finder:
    1. Groups audio files by byte size (instant metadata check).
    2. Hashes only the files that have identical byte sizes.
    """
    size_map: Dict[int, List[Path]] = defaultdict(list)

    print(f"Scanning '{root_folder}' for audio files...")
    for filepath in root_folder.rglob('*'):
        if filepath.is_file() and filepath.suffix.lower() in AUDIO_EXTENSIONS:
            try:
                file_size = filepath.stat().st_size
                # Ignore empty 0-byte corrupted files
                if file_size > 0:
                    size_map[file_size].append(filepath)
            except (PermissionError, OSError):
                continue

    # Filter out unique file sizes
    potential_duplicates = {size: paths for size, paths in size_map.items() if len(paths) > 1}
    print(f"Found {len(potential_duplicates)} size collisions. Computing SHA-256 hashes...")

    hash_map: Dict[str, List[Path]] = defaultdict(list)
    for size, paths in potential_duplicates.items():
        for path in paths:
            file_hash = get_file_hash(path)
            if file_hash:
                hash_map[file_hash].append(path)

    # Return only hashes that have more than one file associated with them
    return {file_hash: paths for file_hash, paths in hash_map.items() if len(paths) > 1}

def remove_duplicates(duplicates: Dict[str, List[Path]], dry_run: bool = True) -> None:
    """
    Removes duplicate files, keeping the file with the shortest path/filename 
    (e.g., keeps 'Song.mp3' and deletes 'Song (1).mp3').
    """
    if not duplicates:
        print("No exact duplicates found!")
        return

    total_freed_bytes = 0
    total_removed_files = 0

    for file_hash, paths in duplicates.items():
        # Sort by path length (shortest path/name kept as original, copies deleted)
        paths.sort(key=lambda p: len(str(p)))
        original = paths[0]
        copies = paths[1:]

        print(f"\n[KEEPING] {original}")
        for copy in copies:
            file_size = copy.stat().st_size
            if dry_run:
                print(f"  [DRY RUN - WOULD DELETE] {copy} ({file_size / (1024*1024):.2f} MB)")
                total_freed_bytes += file_size
                total_removed_files += 1
            else:
                try:
                    copy.unlink()
                    print(f"  [DELETED] {copy} ({file_size / (1024*1024):.2f} MB)")
                    total_freed_bytes += file_size
                    total_removed_files += 1
                except (PermissionError, OSError) as e:
                    print(f"  [ERROR DELETING] {copy}: {e}")

    mode = "Would free" if dry_run else "Freed"
    print("\n" + "="*45)
    print(f"Summary: {mode} {total_freed_bytes / (1024*1024):.2f} MB across {total_removed_files} files.")
    if dry_run:
        print("Set dry_run=False in the script to permanently delete these files.")

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find and remove duplicate audio files.")
    parser.add_argument(
        "path", 
        nargs="?", 
        default=str(Path.home() / "/volumes/Untitled/music"),
        help="Target directory to scan (defaults to ~/Music)"
    )
    parser.add_argument(
        "--delete", 
        action="store_true", 
        help="Permanently delete duplicates (defaults to dry-run mode if omitted)"
    )
    
    args = parser.parse_args()
    target_dir = Path(args.path).expanduser().resolve()

    if not target_dir.exists():
        print(f"Error: Directory '{target_dir}' does not exist.")
    else:
        dupes = find_duplicate_music(target_dir)
        # If --delete is passed, args.delete is True, making dry_run False
        remove_duplicates(dupes, dry_run=not args.delete)