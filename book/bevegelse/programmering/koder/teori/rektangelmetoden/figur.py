import plotmath
import matplotlib.patches as patches
import matplotlib.pyplot as plt


def main(dirname, save):
    #
    # Define functions
    def f(x):
        return -0.125 * (x + 1) ** 2 * (x - 8)

    # List of functions and their labels.
    functions = [f]

    fig, ax = plotmath.plot(
        functions=functions,
        fn_labels=False,
        xmin=-1,
        xmax=9,
        ymin=-2,
        ymax=16,
        ticks=True,
        xstep=1,
        ystep=2,
        grid=True,
        lw=2.5,
        alpha=None,
        domain=(0, 8),
        fontsize=20,
        figsize=None,
        xlabel=r"$t / \mathrm{s}$",
        ylabel=r"$v / (\mathrm{m/s})$",
    )

    domain = (0, 8)
    n_rektangler = 128
    bredde = (domain[1] - domain[0]) / n_rektangler

    for i in range(n_rektangler):
        x = domain[0] + i * bredde
        y = f(x)
        ax.add_patch(
            patches.Rectangle(
                (x, 0),
                bredde,
                y,
                alpha=0.3,
                facecolor=plotmath.COLORS.get("blue"),
                edgecolor="black",
            )
        )

    plt.tight_layout()

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
    main(dirname=dirname, save=True)
