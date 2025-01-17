import sys
import os
from pathlib import Path


def num_to_alphabet(n) -> str:
    """
    Convert a number to an alphabet string.
    """

    n = int(n)

    if n < 1:
        raise ValueError("n must be greater than 0")

    result = ""
    while 0 < n:
        n -= 1  # 0-based indexにするために1引く
        result = chr(n % 26 + ord("a")) + result
        n //= 26
    return result


if __name__ == "__main__":
    # スクリプトのあるディレクトリを取得
    script_directory = os.path.abspath(Path(__file__).parent)

    print(Path(__file__).parent.resolve())
    print(script_directory)

    # 実行中のカレントディレクトリを取得
    print(Path.cwd())

    if len(sys.argv) == 2:
        print(num_to_alphabet(sys.argv[1]))
    else:
        print("Usage: python convert_task_id.py <number>")
        sys.exit(1)
