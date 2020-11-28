"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """HANMATEK Power Supplies (HM305, HM310, HM310p, RS605p)."""


if __name__ == "__main__":
    main(prog_name="hanmatek-cli")  # pragma: no cover
