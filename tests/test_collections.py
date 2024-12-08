import pytest

from solutions.collections import Matrix


class TestMatrix:

    @pytest.fixture
    def matrix(self):
        return Matrix(matrix=[["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]])

    def test_all_cols_as_str(self, matrix: Matrix) -> None:
        expected = ["adg", "beh", "cfi"]
        cols = matrix.all_cols_as_str()
        assert cols == expected

    def test_all_rows_as_str(self, matrix: Matrix) -> None:
        expected = ["abc", "def", "ghi"]
        cols = matrix.all_rows_as_str()
        assert cols == expected

    def test_all_diagonals_as_str(self, matrix: Matrix) -> None:
        expected = [
            "g",
            "dh",
            "aei",
            "bf",
            "c",
            "i",
            "fh",
            "ceg",
            "bd",
            "a",
        ]
        diagonals = matrix.all_diagonals_as_str()
        assert len(diagonals) == 10
        assert set(diagonals) == set(expected)

    def test_at(self, matrix: Matrix):
        assert matrix.at(y=0, x=0).value == "g"
        assert matrix.at(y=2, x=2).value == "c"
        assert matrix.at(y=100, x=100).value == ""

    def test_iter(self, matrix: Matrix):
        points = [point.value for point in matrix.each_point()]
        assert "".join(points) == "ghidefabc"
