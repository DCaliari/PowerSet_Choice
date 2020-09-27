from itertools import chain, combinations
import random


def contains(haystack,needle):
	return haystack.find(needle) != -1


def powerset(iterable):
	"powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
	return list(chain.from_iterable(combinations(iterable, r) for r in range(len(iterable) + 1)))


def shuffle_powerset(lista):
	random.shuffle(lista)
	# create an empty list called new_list.
	new_list = []
	# for the elements of the called list
	for elem in lista:
		elem = list(elem)
		random.shuffle(elem)
		# after we shuffle the elements, we append to the new_list
		new_list.append(elem)
	return new_list


