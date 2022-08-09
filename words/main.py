#! ../bin/python3

from typing import Optional
import typer
import lib


def main(word: str, limit: Optional[int] = None):
    result = lib.get_request(word)
    if result is None:
        typer.secho(f"{word.title()} not found!",
                    fg=typer.colors.RED,
                    bold=True)
    else:
        format_result = lib.format_output(result, limit)
        typer.echo(format_result)


if __name__ == '__main__':
    typer.run(main)
