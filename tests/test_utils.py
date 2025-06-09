from loan_stress.utils import worst_case_cet1


def test_worst_case_cet1():
    paths = [[10, 9, 7], [10, 11, 12]]
    assert worst_case_cet1(paths) == -3
