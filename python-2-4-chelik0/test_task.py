import task as t
import numpy as np
from random import randint, choices


def test_task1():
    assert np.array_equal(t.task1(10, 5), np.array([0, 0, 0, 0, 0, 1, 0, 0, 0, 0]))

    assert np.array_equal(t.task1(10, 0), np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0]))

    assert np.array_equal(t.task1(5, 1), np.array([0, 1, 0, 0, 0]))

    n = randint(1, 1000)
    i = randint(0, n - 1)
    res = [0 for _ in range(n)]
    res[i] = 1
    assert np.array_equal(t.task1(n, i), np.array(res))


def test_task2():
    assert np.array_equal(
        t.task2(10, 20), np.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
    )

    assert np.array_equal(t.task2(10, 15), np.array([10, 11, 12, 13, 14]))

    assert np.array_equal(t.task2(5, 10), np.array([5, 6, 7, 8, 9]))

    a = randint(-100, 100)
    b = a + 1 + randint(0, 100)

    assert np.array_equal(t.task2(a, b), np.array(list(range(a, b))))


def test_task3():
    assert np.array_equal(
        t.task3(3),
        np.array(
            [
                [0, 1, 2],
                [3, 4, 5],
                [6, 7, 8],
            ]
        ),
    )
    assert np.array_equal(
        t.task3(5),
        np.array(
            [
                [0, 1, 2, 3, 4],
                [5, 6, 7, 8, 9],
                [10, 11, 12, 13, 14],
                [15, 16, 17, 18, 19],
                [20, 21, 22, 23, 24],
            ]
        ),
    )
    assert np.array_equal(
        t.task3(6),
        np.array(
            [
                [0, 1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10, 11],
                [12, 13, 14, 15, 16, 17],
                [18, 19, 20, 21, 22, 23],
                [24, 25, 26, 27, 28, 29],
                [30, 31, 32, 33, 34, 35],
            ]
        ),
    )
    n = randint(1, 1000)
    res = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[i][j] = i * n + j
    assert np.array_equal(t.task3(n), np.array(res))


def test_task4():
    assert np.array_equal(
        t.task4(np.array([0, 0, 0, 0, 0, 1, 0, 0, 0, 0]))[0],
        np.array([5]),
    )
    assert np.array_equal(
        t.task4(np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))[0],
        np.array([9]),
    )
    assert np.array_equal(
        t.task4(np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))[0],
        np.array([]),
    )

    arr = choices([0, 1], k=randint(1, 1000))
    res = [i for i in range(len(arr)) if arr[i]]
    assert np.array_equal(
        t.task4(np.array(arr))[0],
        np.array(res),
    )


def test_task5():
    assert t.task5(3).shape == (3, 3, 3)

    assert t.task5(5).shape == (5, 5, 5)

    assert t.task5(6).shape == (6, 6, 6)

    n = randint(1, 100)
    assert t.task5(n).shape == (n, n, n)


def test_task6():
    assert np.array_equal(
        t.task6(np.array([0, 0, 0, 0, 0, 1, 0, 0, 0, 0]), 0, 5),
        np.array([0, 0, 0, 0, 0, -1, 0, 0, 0, 0]),
    )

    assert np.array_equal(
        t.task6(np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 1]), 0, 5),
        np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, -1]),
    )

    assert np.array_equal(
        t.task6(np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 0, 5),
        np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    )

    arr = choices(range(0, 100_000), k=randint(1, 1000))
    a = randint(0, 50_000)
    b = randint(a + 1, 100_000)
    res = [(-i if (a < i < b) else i) for i in arr]
    assert np.array_equal(
        t.task6(np.array(arr).copy(), a, b),
        np.array(res),
    )


def test_task7():
    assert np.array_equal(
        t.task7(np.array([1, 2, 3, 4, 5]), np.array([1, 2, 3, 4, 5])),
        np.array([1, 2, 3, 4, 5]),
    )

    assert np.array_equal(
        t.task7(np.array([1, 2, 3, 4, 5]), np.array([5, 4, 3, 2, 1])),
        np.array([1, 2, 3, 4, 5]),
    )

    assert np.array_equal(
        t.task7(np.array([1, 2, 3, 4, 5]), np.array([6, 7, 8, 9, 10])),
        np.array([]),
    )

    assert np.array_equal(
        t.task7(np.array([1, 2, 3, 4, 5]), np.array([3, 4, 5, 6, 7])),
        np.array([3, 4, 5]),
    )

    arr1 = choices(range(0, 100_000), k=randint(1, 1000))
    arr2 = choices(range(0, 100_000), k=randint(1, 1000))
    res = [i for i in arr1 if i in arr2]
    assert np.array_equal(
        np.sort(t.task7(np.array(arr1), np.array(arr2))),
        np.sort(np.array(res)),
    )


def test_task8():
    assert np.array_equal(
        t.task8(1, 2022),
        np.array(
            [
                "2022-01-01",
                "2022-01-02",
                "2022-01-03",
                "2022-01-04",
                "2022-01-05",
                "2022-01-06",
                "2022-01-07",
                "2022-01-08",
                "2022-01-09",
                "2022-01-10",
                "2022-01-11",
                "2022-01-12",
                "2022-01-13",
                "2022-01-14",
                "2022-01-15",
                "2022-01-16",
                "2022-01-17",
                "2022-01-18",
                "2022-01-19",
                "2022-01-20",
                "2022-01-21",
                "2022-01-22",
                "2022-01-23",
                "2022-01-24",
                "2022-01-25",
                "2022-01-26",
                "2022-01-27",
                "2022-01-28",
                "2022-01-29",
                "2022-01-30",
                "2022-01-31",
            ],
            dtype="datetime64[D]",
        ),
    )

    assert np.array_equal(
        t.task8(2, 2022),
        np.array(
            [
                "2022-02-01",
                "2022-02-02",
                "2022-02-03",
                "2022-02-04",
                "2022-02-05",
                "2022-02-06",
                "2022-02-07",
                "2022-02-08",
                "2022-02-09",
                "2022-02-10",
                "2022-02-11",
                "2022-02-12",
                "2022-02-13",
                "2022-02-14",
                "2022-02-15",
                "2022-02-16",
                "2022-02-17",
                "2022-02-18",
                "2022-02-19",
                "2022-02-20",
                "2022-02-21",
                "2022-02-22",
                "2022-02-23",
                "2022-02-24",
                "2022-02-25",
                "2022-02-26",
                "2022-02-27",
                "2022-02-28",
            ],
            dtype="datetime64[D]",
        ),
    )

    assert np.array_equal(
        t.task8(2, 2024),
        np.array(
            [
                "2024-02-01",
                "2024-02-02",
                "2024-02-03",
                "2024-02-04",
                "2024-02-05",
                "2024-02-06",
                "2024-02-07",
                "2024-02-08",
                "2024-02-09",
                "2024-02-10",
                "2024-02-11",
                "2024-02-12",
                "2024-02-13",
                "2024-02-14",
                "2024-02-15",
                "2024-02-16",
                "2024-02-17",
                "2024-02-18",
                "2024-02-19",
                "2024-02-20",
                "2024-02-21",
                "2024-02-22",
                "2024-02-23",
                "2024-02-24",
                "2024-02-25",
                "2024-02-26",
                "2024-02-27",
                "2024-02-28",
                "2024-02-29",
            ],
            dtype="datetime64[D]",
        ),
    )
