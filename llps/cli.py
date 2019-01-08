
import click

from .project_schema import ProjectSchema


@click.group()
def main():
    pass


@main.command('validate')
@click.argument('filepath')
def cli_validate_schema(filepath):
    """Validate a schema as a valid project schema."""
    ProjectSchema.from_file(filepath)


if __name__ == '__main__':
    main()
