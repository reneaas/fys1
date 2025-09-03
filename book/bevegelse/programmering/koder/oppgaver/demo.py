import plotmath


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return -0.25 * (x + 1) ** 2 * (x - 3)

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=False,
        xmin=-0.5,
        xmax=3.5,
        ymin=-0.2,
        ymax=3,
        ticks=True,
        xstep=0.5,
        ystep=0.2,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=(0, 3),
        fontsize=30,
        figsize=None,
        xlabel="$t / \\mathrm{s}$",
        ylabel="$v / (\\mathrm{m/s})$",
    )

    # NOTE: Select an appropriate `dirname` to save the figure.
    # The directory `dirname` will be created automatically if it does not exist already.
    if save:
        fname = __file__.split("/")[-1].replace(".py", ".svg")
        plotmath.savefig(
            dirname=dirname, fname=fname
        )  # Lagrer figuren i `dirname`-directory

    if not save:

        plotmath.show()


if __name__ == "__main__":

    import pathlib

    # Get the directory where the script is located
    current_dir = str(pathlib.Path(__file__).resolve().parent)

    parts = current_dir.split("/")
    for i in range(len(parts)):
        if parts[~i] == "koder":
            parts[~i] = "figurer"
            break

    dirname = "/".join(parts)

    # NOTE: Set `save=True` to save figure. `save=False` to display figure.
    main(dirname=dirname, save=False)
