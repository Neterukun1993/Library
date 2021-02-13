---
title: ウェーブレット行列
documentation_of: //DataStructure/Wavelet/WaveletMatrix.py
---
## 使い方
`CompressedWaveletMatrix(array: Sequence[int])`  
`array` から座標圧縮した Wavelet Matrix を構築する。計算量 $O(n \log n)$

- `access(i: int) -> int`  
`i` 番目 (0-indexed) の要素を返す。計算量 $O(\log n)$

- `rank(l: int, r: int, val: int) -> int`  
`array[l:r]` 内の `val` の個数を返す。計算量 $O(\log n)$

- `kth_smallest(l: int, r: int, k: int)`  
`array[l:r]` 内の `k` 番目 (0-indexed) に小さい要素を返す。計算量 $O(\log n)$

- `kth_largest(l: int, r: int, k: int)`  
`array[l:r]` 内の `k` 番目 (0-indexed) に大きい要素を返す。計算量 $O(\log n)$ 

- `range_freq(l: int, r: int, upper: int)`  
`array[l:r]` 内の `upper` よりも小さい要素の個数を返す。計算量 $O(\log n)$

- `prev_val(l: int, r: int, upper: int)`  
`array[l:r]` 内の `upper` よりも小さい最大の要素を返す。そのような要素が存在しない場合は `None` を返す。計算量 $O(\log n)$

- `next_val(l: int, r: int, lower: int) -> int`  
`array[l:r]` 内の `lower` 以上の最小の要素を返す。そのような要素が存在しない場合は `None` を返す。計算量 $O(\log n)$
