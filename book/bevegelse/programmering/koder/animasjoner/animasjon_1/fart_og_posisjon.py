import os
import plotmath
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from matplotlib.animation import FFMpegWriter


def area(x, v):
    y = np.zeros_like(x)
    dx = x[1] - x[0]
    for i in range(len(x) - 1):
        y[i + 1] = y[i] + v(0.5 * (x[i] + x[i + 1])) * dx
    return y


def main(dirname, save):
    #
    # Define functions
    def v(t):
        return -t * (t - 10)

    xmin = 0
    xmax = 10

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))
    # fig.patch.set_facecolor("none")  # or fig.patch.set_alpha(0)

    for ax in axes:
        ax.spines["left"].set_position("zero")
        ax.spines["right"].set_color("none")
        ax.spines["bottom"].set_position("zero")
        ax.spines["top"].set_color("none")

        ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
        ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

    axes[0].set_xlabel(r"$t / \mathrm{s}$", fontsize=16, loc="right")
    axes[0].set_ylabel(
        r"$v / (\mathrm{m/s})$", fontsize=16, loc="top", rotation="horizontal"
    )

    axes[1].set_xlabel(r"$t / \mathrm{s}$", fontsize=16, loc="right")
    axes[1].set_ylabel(
        r"$s / \textrm{m}$", fontsize=16, loc="top", rotation="horizontal"
    )

    axes[1].set_xlim(-1, 11)
    axes[1].set_ylim(-1, 210)

    # xticks = np.arange(xmin - 1, xmin + 1, 2)
    # xticks = []

    # for ax in axes:
    #     ax.set_xticks(np.arange(0, 12, 2), np.arange(0, 12, 2), fontsize=20)
    #     ax.set_yticks(np.arange(0, 300, 50), np.arange(0, 300, 50), fontsize=20)

    for ax in axes:
        ax.tick_params(axis="both", which="major", labelsize=18)

    # for ax in axes:
    #     ax.set_xticks([])
    #     ax.set_yticks([])

    # Remove the tick at 0 on both axes (example)

    # Data for animation
    x = np.linspace(xmin, xmax, 4096)
    y = v(x)
    s_full = area(x, v)

    # Static velocity curve
    axes[0].plot(x, y, color=plotmath.COLORS.get("blue"), lw=2.5)
    # Moving vertical indicator on velocity as data-space line from y=0 to y(t)
    v_indicator = axes[0].plot(
        [xmin, xmin], [0, 0], color="k", lw=2, ls="--", alpha=0.7
    )[0]
    fill_handle = [None]

    # Progressive position curve and moving point
    (s_line,) = axes[1].plot([], [], color=plotmath.COLORS.get("blue"), lw=2.5)
    s_point = axes[1].plot([], [], "o", color="black", ms=8)[0]
    # Position indicators: vertical from (x_cur, 0) to (x_cur, s(x_cur)) and horizontal from (0, s(x_cur)) to (x_cur, s(x_cur))
    s_v_indicator = axes[1].plot(
        [xmin, xmin], [0, 0], color="k", lw=2, ls="--", alpha=0.7
    )[0]
    s_h_indicator = axes[1].plot([0, 0], [0, 0], color="k", lw=2, ls="--", alpha=0.7)[0]

    # Frame indices (limit frames for performance)
    max_frames = 240
    idxs = np.linspace(2, len(x), min(max_frames, len(x)), dtype=int)

    def init():
        # fig.patch.set_facecolor("none")
        # ax.patch.set_facecolor("none")
        # ax.set_facecolor("none")

        s_line.set_data([], [])
        s_point.set_data([], [])

        v_indicator.set_data([xmin, xmin], [0, 0])
        s_v_indicator.set_data([xmin, xmin], [0, 0])
        s_h_indicator.set_data([0, 0], [0, 0])
        return s_line, s_point, v_indicator, s_v_indicator, s_h_indicator

    def update(frame_idx):
        # fig.patch.set_alpha(0)  # or fig.patch.set_alpha(0)
        # for ax in axes:
        #     ax.patch.set_alpha(0)

        i = idxs[frame_idx]
        xi = x[:i]
        yi = y[:i]
        si = s_full[:i]

        # Update position curve and point
        s_line.set_data(xi, si)
        s_point.set_data([xi[-1]], [si[-1]])
        # Update position indicators to end at current point
        x_cur_s, y_cur_s = xi[-1], si[-1]
        s_v_indicator.set_data([x_cur_s, x_cur_s], [0, y_cur_s])
        s_h_indicator.set_data([0, x_cur_s], [y_cur_s, y_cur_s])

        # Update velocity fill (remove previous and draw new for simplicity)
        if fill_handle[0] is not None:
            try:
                fill_handle[0].remove()
            except Exception:
                pass
        fill_handle[0] = axes[0].fill_between(
            x=xi,
            y1=0,
            y2=yi,
            alpha=0.4,
            color=plotmath.COLORS.get("blue"),
        )
        # Update vertical indicator to reach current velocity value in data coords
        x_cur, y_cur = xi[-1], yi[-1]
        v_indicator.set_data([x_cur, x_cur], [0, y_cur])
        return s_line, s_point, v_indicator, s_v_indicator, s_h_indicator

    anim = animation.FuncAnimation(
        fig,
        update,
        init_func=init,
        frames=len(idxs),
        interval=33,
        blit=True,
        repeat=False,
    )

    plt.tight_layout()

    if save:
        # writer = FFMpegWriter(
        #     fps=20,
        #     codec="libwebp_anim",
        #     extra_args=["-vcodec", "libwebp", "-pix_fmt", "yuva420p"],
        # )
        # anim.save(
        #     f"animation.webp",
        #     writer=writer,
        #     savefig_kwargs={"transparent": True, "facecolor": "none"},
        # )
        anim.save(
            "animation.gif",
            writer="ffmpeg",
            fps=20,
            savefig_kwargs={"transparent": True, "facecolor": "none"},
        )
        anim.save(
            "animation.mp4",
            fps=20,
        )

        # writer = FFMpegWriter(
        #     fps=20,
        #     codec="libwebp",
        #     extra_args=["-pix_fmt", "yuva420p"],
        # )
        # anim.save(
        #     f"animation.webp",
        #     writer=writer,
        #     savefig_kwargs={"transparent": True, "facecolor": "none"},
        # )

        # MP4 with ProRes 4444 for alpha (experimental, large files, limited compatibility)
        writer_prores = FFMpegWriter(
            fps=20,
            codec="prores_ks",
            extra_args=[
                "-profile:v",
                "4",  # 4 = 4444 profile (use "5" for 4444 XQ)
                "-pix_fmt",
                "yuva444p10le",  # 10-bit YUVA (includes alpha)
            ],
        )
        anim.save(
            "animation.mov",
            writer=writer_prores,
            # savefig_kwargs={"transparent": True, "facecolor": "none"},
        )
    else:
        plt.show()


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
