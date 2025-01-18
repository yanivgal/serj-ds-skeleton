import os

def remove_placeholders():
    """Recursively removes .placeholder files from the generated project."""
    for root, dirs, files in os.walk("."):
        for file in files:
            if file == ".placeholder":
                os.remove(os.path.join(root, file))

if __name__ == "__main__":
    remove_placeholders()
