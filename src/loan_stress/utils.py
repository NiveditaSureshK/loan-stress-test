from collections.abc import Sequence


def worst_case_cet1(paths: Sequence[Sequence[float]]) -> float:
    """
    Return the most negative CET1 delta among provided paths.

    Parameters
    ----------
    paths : Sequence[Sequence[float]]
        Each path is a list/tuple of CET1 values over time.

    Returns
    -------
    float
        Minimum (ending - starting) CET1 across all paths.

    Raises
    ------
    ValueError
        If `paths` is empty.
    """
    if not paths:
        raise ValueError("No CET1 paths provided")

    # Compute delta for each path, then take the smallest (worst) delta
    return min(path[-1] - path[0] for path in paths)
