# Count Unguarded Cells in the Grid


"""You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and
walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.
A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless
obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.

Return the number of unoccupied cells that are not guarded."""


# Fixed grid size and assignment bug in _cross


class Solution:
    def __init__(self) -> None:
        # initialize instance attributes so linters won't complain
        self.m: int = 0
        self.n: int = 0
        self.grid: list[str] = []

    def _idx(self, r: int, c: int) -> int:
        """Convert (r, c) to linear index in row-major order."""
        return r * self.n + c

    def _cross(self, r: int, c: int) -> int:
        """
        From guard at (r, c), mark visible empty cells as guarded ('V') and
        return how many previously unguarded empty cells got guarded.
        Walls and guards (marked as 'X') block sight.
        """
        d = (0, 1, 0, -1, 0)
        newly_guarded = 0

        for a in range(4):
            di, dj = d[a], d[a + 1]
            i, j = r + di, c + dj
            while 0 <= i < self.m and 0 <= j < self.n:
                pos = self._idx(i, j)
                # 'X' represents wall or guard (blocks sight)
                if self.grid[pos] == "X":
                    break
                # only mark and count previously empty cells
                if self.grid[pos] == " ":
                    newly_guarded += 1
                    # FIX: use assignment, not comparison
                    self.grid[pos] = "V"
                i += di
                j += dj

        return newly_guarded

    def countUnguarded(
        self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]
    ) -> int:
        """
        Return the number of empty cells that are not guarded.
        Empty cells are initialized as ' '. Walls and guards are marked as 'X'.
        Guarded empty cells are marked as 'V'.
        """
        self.m = m
        self.n = n
        # FIX: allocate m * n cells (previously used m + n)
        self.grid = [" "] * (m * n)
        comp = m * n

        # place walls (mark as 'X' and decrement count of unoccupied cells)
        for r, c in walls:
            pos = self._idx(r, c)
            self.grid[pos] = "X"
            comp -= 1

        # place guards (mark as 'X' to act as blockers and decrement count)
        for r, c in guards:
            pos = self._idx(r, c)
            self.grid[pos] = "X"
            comp -= 1

        # for each guard, mark visible empty cells and decrement comp accordingly
        for r, c in guards:
            comp -= self._cross(r, c)

        return comp


if __name__ == "__main__":
    obj = Solution()
    print(
        obj.countUnguarded(
            m=4,
            n=6,
            guards=[[0, 0], [1, 1], [2, 3]],
            walls=[[0, 1], [2, 2], [1, 4]],
        )
    )
