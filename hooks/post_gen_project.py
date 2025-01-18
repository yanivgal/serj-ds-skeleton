import os

def remove_placeholders():
    """Recursively removes .gitkeep placeholder files from the generated project."""
    for root, dirs, files in os.walk("."):
        for file in files:
            if file == ".gitkeep":
                os.remove(os.path.join(root, file))

if __name__ == "__main__":
    remove_placeholders()
