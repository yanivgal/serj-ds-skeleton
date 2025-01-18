import os

def remove_placeholders():
    """Recursively removes .gitkeep placeholder files from the generated project."""
    for root, dirs, files in os.walk("."):
        for file in files:
            if file == ".gitkeep":
                os.remove(os.path.join(root, file))

def rename_gitignore():
    """Renames the gitignore file to .gitignore"""
    if os.path.exists("gitignore"):
        os.rename("gitignore", ".gitignore")


if __name__ == "__main__":
    remove_placeholders()
    rename_gitignore()
