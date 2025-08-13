"""Static site generator for GitHub Pages."""

import argparse
import importlib.resources
import shutil
import tomllib
from importlib.metadata import version
from pathlib import Path

from .builder import build_website
from .server import run_server
from . import static


def create_project():
    """Create a new example project."""
    static_dir = importlib.resources.files(static)

    # Copy config file
    shutil.copy(f"{static_dir / 'genja.toml'}", ".")

    # Copy template files
    Path("./_templates").mkdir(exist_ok=True)
    shutil.copy(f"{static_dir / 'index.html'}", "./_templates")
    shutil.copy(f"{static_dir / 'page.html'}", "./_templates")
    shutil.copy(f"{static_dir / 'post.html'}", "./_templates")

    # Copy posts files
    Path("./_posts/fruits").mkdir(parents=True, exist_ok=True)
    shutil.copy(f"{static_dir / 'apple.md'}", "./_posts/fruits")
    shutil.copy(f"{static_dir / 'orange.md'}", "./_posts/fruits")

    Path("./_posts/veggies").mkdir(parents=True, exist_ok=True)
    shutil.copy(f"{static_dir / 'broccoli.md'}", "./_posts/veggies")
    shutil.copy(f"{static_dir / 'spinach.md'}", "./_posts/veggies")

    # Copy pages files
    Path("./_pages").mkdir(exist_ok=True)
    shutil.copy(f"{static_dir / 'about.md'}", "./_pages")
    shutil.copy(f"{static_dir / 'contact.md'}", "./_pages")

    # Copy other files
    Path("./mysite/img").mkdir(parents=True, exist_ok=True)
    shutil.copy(f"{static_dir / 'apple.jpg'}", "./mysite/img")
    shutil.copy(f"{static_dir / 'styles.css'}", "./mysite")


def remove_files(config: dict[str, str]):
    """Remove the generated HTML and JSON feed files."""
    pages_path = Path("_pages")
    posts_path = Path("_posts")
    templates_path = Path("_templates")
    output_path = Path(config["site_output"])
    blog_path = output_path / Path(config["posts_output"])

    # HTML files generated from Markdown files in pages directory
    p = pages_path.glob("**/*.md")
    html_files = [x.name.replace("md", "html") for x in p if x.is_file()]

    # HTML files generated from Markdown files in posts directory
    p = posts_path.glob("**/*.md")
    html_files = html_files + [x.name.replace("md", "html") for x in p if x.is_file()]

    # HTML files generated from templates
    p = templates_path.glob("**/*.html")
    for x in p:
        if x.name != "post.html" and x.name != "page.html" and x.name != "base.html":
            html_files.append(x.name)

    # Remove the generated JSON feed file in the output directory
    print("\nRemoving generated JSON feed file in output directory...")
    json_path = Path(output_path / "feed.json")

    if json_path.exists():
        json_path.unlink()
        print("➔", json_path)

    # Remove the generated HTML files in the output directory
    print("\nRemoving generated HTML files in output directory...")

    for html_path in output_path.glob("**/*.html"):
        if html_path.name in html_files and html_path.parent != templates_path:
            html_path.unlink()
            print("➔", html_path)

    # Remove empty sub-directories
    print("\nRemoving empty sub-directories...")

    for subdir in blog_path.glob("**/*"):
        if subdir.is_dir() and not any(subdir.iterdir()):
            subdir.rmdir()
            print("➔", subdir)

    # Remove empty blog directory
    print("\nRemoving empty posts directory...")
    if blog_path.exists() and blog_path.is_dir() and not any(blog_path.iterdir()):
        blog_path.rmdir()
        print("➔", blog_path)

    print("\nRemoval of generated HTML and JSON files is complete.")


def main():
    """Run the genja program."""
    # Command line arguments
    parser = argparse.ArgumentParser(description="Genja static website generator.")

    choices = ["build", "serve", "clean", "new"]
    parser.add_argument("command", choices=choices, help="genja commands")

    parser.add_argument("-v", "--version", action="version", version=version("genja"))
    args = parser.parse_args()

    # Create an example project
    if args.command == "new":
        create_project()

    # Get configuration from TOML file, requires Python 3.11 or higher
    with open("genja.toml", "rb") as f:
        config = tomllib.load(f)

    print(f"\n{'Genja command ':.<30} {args.command}")
    print(f"{'Base URL ':.<30} {config['base_url']}")
    print(f"{'Posts output directory ':.<30} {config['posts_output']}")
    print(f"{'Site output directory ':.<30} {config['site_output']}")
    print(f"{'Website title ':.<30} {config['title']}")

    # Build the website
    if args.command == "build":
        build_website(config)

    # Build the website then run a local server and open web browser
    if args.command == "serve":
        build_website(config)
        run_server(config)

    # Remove generated files in the output directory
    if args.command == "clean":
        remove_files(config)
