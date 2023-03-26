import sys


def get_braces(chars: str) -> dict[int, int]:
    braces: dict[int, int] = {}
    left_positions: list[int] = []

    for position, char in enumerate(chars):
        if char == '[':
            left_positions.append(position)

        elif char == ']':
            left = left_positions.pop()
            right = position
            braces[left] = right
            braces[right] = left

    return braces


def eval_(code: str):
    env: list[int] = [0]
    index = 0

    braces = get_braces(code)

    code_len = len(code)

    position = 0
    while position < code_len:
        if code[position] == ">":
            index += 1
            if len(env) == index:
                env.append(0)

        elif code[position] == "<":
            index -= 1
            if index < 0:
                raise #TODO

        elif code[position] == "+":
            env[index] += 1

        elif code[position] == "-":
            env[index] -= 1

        elif code[position] == ".":
            sys.stdout.write(chr(env[index] % 256))
            sys.stdout.flush()

        elif code[position] == ",":
            env[index] = ord(input()[0])

        elif code[position] ==  "["\
                and env[index] == 0:
            position = braces[position]

        elif code[position] == "]"\
                and env[index] != 0:
            position = braces[position]

        elif code[position] in ["[", "]"]:
            pass

        else:
            raise
        position += 1


if __name__ == "__main__":
    file_name = sys.argv[1]
    with open(file_name, "r") as file:
        eval_(file.read())
