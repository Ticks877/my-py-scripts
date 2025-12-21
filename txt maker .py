import subprocess

MAX_GENERATIONS = 100
GENERATION = 0

def make_copy(gen):
    next_gen = gen + 1
    filename = f"script_{next_gen}.py"

    with open(__file__, "r") as f:
        code = f.read()

    code = code.replace(
        f"GENERATION = {gen}",
        f"GENERATION = {next_gen}"
    )

    with open(filename, "w") as f:
        f.write(code)

    print(f"Created {filename}")

    # Run the next script immediately
    subprocess.run(["python", filename])

if __name__ == "__main__":
    print(f"Running generation {GENERATION}")

    if GENERATION < MAX_GENERATIONS:
        make_copy(GENERATION)
    else:
        print("Max generations reached. Stopping.")
     