rows = [(2 * a) + 1 | a <- [1..500]]
answer = sum [n^2 | n <- rows] + sum [n^2 - (n - 1) | n <- rows] + sum [n^2 - (2 * (n - 1)) | n <- rows] + sum [n^2 - (3 * (n - 1)) | n <- rows] + 1
