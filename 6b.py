import heapq
from collections import defaultdict


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]


def huffman_codes(tree, prefix='', codes={}):
    if tree is not None:
        if tree.char is not None:
            codes[tree.char] = prefix
        huffman_codes(tree.left, prefix + '0', codes)
        huffman_codes(tree.right, prefix + '1', codes)
    return codes


frequencies = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
tree = huffman_tree(frequencies)
codes = huffman_codes(tree)
print(codes)  # Output: Huffman codes for each character
