from itertools import chain, combinations


def powerset(iterable):
	"powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
	return list(chain.from_iterable(combinations(iterable, r) for r in range(len(iterable) + 1)))
