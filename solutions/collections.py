from pydantic import BaseModel
from typing import Generator, Optional


class Point(BaseModel):
    x: int
    y: int
    value: str


class Matrix(BaseModel):
    matrix: list[list[str]]

    def at(self, x: int, y: int) -> Optional[Point]:
        try:
            _y = self.height() - y - 1
            if _y < 0:
                raise IndexError
            return Point(x=x, y=y, value=self.matrix[_y][x])
        except IndexError:
            return Point(x=x, y=y, value="")

    def each_point(self) -> Generator[Point, None, None]:
        _matrix = self._copy()
        _matrix.reverse()
        row_index = 0
        for row in _matrix:
            col_index = 0
            for col in row:
                yield Point(x=col_index, y=row_index, value=col)
                col_index += 1
            row_index += 1

    def width(self) -> int:
        return len(self.matrix[0])

    def height(self) -> int:
        return len(self.matrix)

    def all_rows_as_str(self) -> list[str]:
        return ["".join(row) for row in self.matrix]

    def all_cols_as_str(self) -> list[str]:
        cols = [""] * self.width()
        for row_index, row in enumerate(self.matrix):
            for col_index, col in enumerate(row):
                cols[col_index] += col
        return cols

    def _copy(self) -> list[list[str]]:
        return [row[:] for row in self.matrix]

    def all_diagonals_as_str(self) -> list[str]:
        # Rotate the matrix 45 degrees to
        # capture all diagonal lines
        copy_right = self._copy()
        copy_left = self._copy()
        left = self.height() - 1
        right = 0

        for index, row in enumerate(copy_right):
            copy_right[index] = ([""] * left) + row + ([""] * right)
            left -= 1
            right += 1

        right = self.height() - 1
        left = 0
        for index, row in enumerate(copy_left):
            copy_left[index] = ([""] * left) + row + ([""] * right)
            right -= 1
            left += 1

        right = Matrix(matrix=copy_right).all_cols_as_str()
        left = Matrix(matrix=copy_left).all_cols_as_str()

        return right + left
