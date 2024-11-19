"""Static site generator for GitHub Pages."""

import argparse
import tomllib
import importlib.resources
import shutil
from importlib.metadata import version
from pathlib import Path

from .builder import build_website
from .server import run_server
from . import static


def create_project():
    """Create a new example project."""
    static_dir = importlib.resources.files(static)

    # Copy config file
    shutil.copy(f"{static_dir / 'config.toml'}", ".")

    # Copy template files
    Path("./templates").mkdir(exist_ok=True)
    shutil.copy(f"{static_dir / 'index.html'}", "./templates")
    shutil.copy(f"{static_dir / 'page.html'}", "./templates")
    shutil.copy(f"{static_dir / 'post.html'}", "./templates")

    # Copy posts files
    Path("./posts/fruits").mkdir(parents=True, exist_ok=True)
    shutil.copy(f"{static_dir / 'apple.md'}", "./posts/fruits")
    shutil.copy(f"{static_dir / 'orange.md'}", "./posts/fruits")

    Path("./posts/veggies").mkdir(parents=True, exist_ok=True)
    shutil.copy(f"{static_dir / 'broccoli.md'}", "./posts/veggies")
    shutil.copy(f"{static_dir / 'spinach.md'}", "./posts/veggies")

    # Copy pages files
    Path("./pages").mkdir(exist_ok=True)
    shutil.copy(f"{static_dir / 'about.md'}", "./pages")
    shutil.copy(f"{static_dir / 'contact.md'}", "./pages")

    # Copy other files
    Path("./mysite/img").mkdir(parents=True, exist_ok=True)
    shutil.copy(f"{static_dir / 'apple.jpg'}", "./mysite/img")
    shutil.copy(f"{static_dir / 'styles.css'}", "./mysite")


def remove_files(config: dict[str, str]):
    """Remove the generated HTML and JSON feed files."""
    pages_path = Path("pages")
    posts_path = Path("posts")
    templates_path = Path("templates")
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
    json_path = Path(output_path / "feed.json")

    if json_path.exists():
        json_path.unlink()

    # Remove the generated HTML files in the output directory
    for html_path in output_path.glob("**/*.html"):
        if html_path.name in html_files and html_path.parent != templates_path:
            html_path.unlink()

    # Remove empty sub-directories
    for subdir in blog_path.glob("**/*"):
        if subdir.is_dir() and not any(subdir.iterdir()):
            subdir.rmdir()

    # Remove empty blog directory
    if blog_path.exists():
        blog_path.rmdir()

    print(f"\nRemoved generated HTML files and JSON feed file in `{output_path}` directory.")


def main():
    """Run the genja program."""
    # Command line arguments
    parser = argparse.ArgumentParser(description="Genja static site generator for GitHub Pages")

    choices = ["build", "serve", "clean", "new"]
    parser.add_argument("command", choices=choices, help="genja commands")

    parser.add_argument("-v", "--version", action="version", version=version("genja"))
    args = parser.parse_args()

    # Create an example project
    if args.command == "new":
        create_project()

    # Get configuration from TOML file, requires Python 3.11 or higher
    with open("config.toml", "rb") as f:
        config = tomllib.load(f)

    print(f'\n{"Genja command ":.<30} {args.command}')
    print(f'{"Base URL ":.<30} {config["base_url"]}')
    print(f'{"Posts output directory ":.<30} {config["posts_output"]}')
    print(f'{"Site output directory ":.<30} {config["site_output"]}')
    print(f'{"Website title ":.<30} {config["title"]}')

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
