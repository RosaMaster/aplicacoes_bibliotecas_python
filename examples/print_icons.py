"""Exemplos de como imprimir ícones/emoji no terminal com Python.

- Unicode direto
- Biblioteca `emoji` (aliases)
- Biblioteca `rich` para saída colorida e emoji

Instruções (Windows PowerShell):
  py -3 examples\print_icons.py
  # Se houver problemas com emoji, force UTF-8 no PowerShell antes:
  # [Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Instale libs (opcional):
  pip install emoji rich
"""

from __future__ import annotations
import sys
import os

# Ajuste de encoding para Windows (try/except para compatibilidade)
if os.name == "nt":
    try:
        # Python 3.7+ supports reconfigure on stdout/stderr
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        # Fallback: change Windows console code page (may require permission)
        try:
            import ctypes
            ctypes.windll.kernel32.SetConsoleOutputCP(65001)
        except Exception:
            pass


def unicode_examples() -> None:
    print("-- Unicode / Emoji simples --")
    print("Positivo: ✅  OK: ✔️")
    print("Negativo: ❌  X: ✖")
    print("Seta: ➡️  Info: ℹ️  Atenção: ⚠️")
    print()


def emoji_library_example() -> None:
    print("-- Usando a biblioteca 'emoji' (aliases) --")
    try:
        import emoji
    except ImportError:
        print("Biblioteca 'emoji' não instalada. Instale com: pip install emoji")
        print()
        return

    # Alguns aliases comuns: :white_check_mark:, :x:, :rocket:
    print(emoji.emojize(":white_check_mark: Positivo", language="alias"))
    print(emoji.emojize(":x: Negativo", language="alias"))
    print(emoji.emojize(":rocket: Vamos!", language="alias"))
    print()


def rich_example() -> None:
    print("-- Usando 'rich' para saída colorida e emoji --")
    try:
        from rich import print as rprint
    except Exception:
        print("Biblioteca 'rich' não instalada. Instale com: pip install rich")
        print()
        return

    rprint("[green]✅ Positivo[/] [bold red]❌ Negativo[/]")
    rprint(":rocket: [cyan]Iniciando processo...[/]")
    print()


def ascii_fallback() -> None:
    print("-- Fallback ASCII (quando terminal não suporta emoji) --")
    print("Positivo: [OK]  Negativo: [X]  Info: (i)")
    print()


def main() -> None:
    unicode_examples()
    emoji_library_example()
    rich_example()
    ascii_fallback()


if __name__ == "__main__":
    main()
