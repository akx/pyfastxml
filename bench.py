import gc
import time
import psutil
import sys
from itertools import islice
import m_fastxml, m_sax, m_lxml

fns = {
    "m1": m_sax.m1,
    "m2": m_lxml.m2,
    "m3": m_fastxml.m3,
}

expected_n = 800_000
expected_slice = [
    ("0", {"id": "0", "a": "0"}),
    ("1", {"id": "1", "a": "331"}),
    ("2", {"id": "2", "a": "662"}),
    ("3", {"id": "3", "a": "993"}),
    ("4", {"id": "4", "a": "1324"}),
    ("5", {"id": "5", "a": "1655"}),
    ("6", {"id": "6", "a": "1986"}),
    ("7", {"id": "7", "a": "2317"}),
    ("8", {"id": "8", "a": "2648"}),
    ("9", {"id": "9", "a": "2979"}),
]


def test(m):
    t0 = time.time()
    result = m()
    t = time.time() - t0
    assert len(result) == expected_n
    slice = list(islice(result.items(), 0, 10))
    assert slice == expected_slice
    print(t)
    print(psutil.Process().memory_info())


if __name__ == "__main__":
    name = sys.argv[1]
    print("***", name)
    for x in range(5):
        test(fns[name])
        gc.collect()
