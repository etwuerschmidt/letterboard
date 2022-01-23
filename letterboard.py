import collections
import functools
import typing

CharCount = {str: int}
SharedChars = [[str]]

board_shared_counts: SharedChars = [
	["O", "0"],
	[",", "'"]
]

board_char_count: CharCount = {
	"A": 18,
	"B": 6,
	"C": 8,
	"D": 8,
	"E": 22,
	"F": 6,
	"G": 6,
	"H": 8,
	"I": 18,
	"J": 4,
	"K": 4,
	"L": 12,
	"M": 10,
	"N": 14,
	"O": 26,
	"P": 8,
	"Q": 4,
	"R": 14,
	"S": 14,
	"T": 14,
	"U": 12,
	"V": 4,
	"W": 6,
	"X": 4,
	"Y": 6,
	"Z": 4,
	"0": 26,
	"1": 8,
	"2": 6,
	"3": 6,
	"4": 6,
	"5": 6,
	"6": 6,
	"7": 6,
	"8": 6,
	"9": 6,
	"$": 2,
	",": 8,
	".": 6,
	"/": 2,
	"-": 2,
	"@": 2,
	"#": 2,
	"&": 2,
	"*": 2,
	"¢": 2,
	"→": 2,
	"?": 2,
	"'": 8
}

def count_chars(phrase: str) -> CharCount:
	phrase_char_count: CharCount = {}
	phrase_without_spaces: str = phrase.replace(" ", "").upper()
	for char in phrase_without_spaces:
		char_count: int = phrase_char_count.get(char, 0)
		phrase_char_count[char] = char_count + 1

	return phrase_char_count

def validate_char_count(char_count: CharCount) -> bool:
	invalid = False
	shared_chars_addressed: SharedChars = []
	for char in char_count.keys():
		if char not in board_char_count.keys():
			print("INVALID: Don't have char %s" % char)
			return True
		(shared_char, chars_shared_with) = is_char_shared(char)
		if shared_char and not(chars_shared_with in shared_chars_addressed):
			total_shared_chars_needed = sum(map(lambda x: char_count.get(x, 0), chars_shared_with))
			if total_shared_chars_needed > board_char_count[char]:
				invalid = True
				shared_chars_addressed.append(chars_shared_with)
				print("INVALID: Need %d total %ss, have only %d" % (total_shared_chars_needed, chars_shared_with, board_char_count[char]))
		else:
			if char_count[char] > board_char_count[char]:
				invalid = True
				print("INVALID: Need %d %ss, have only %d" % (char_count[char], char, board_char_count[char]))
	return invalid

def is_char_shared(char: chr) -> (bool, [str]):
	for shared_char_count in board_shared_counts:
		if char in shared_char_count:
			return (True, shared_char_count)
	return (False, [])

if __name__ == "__main__":
	phrase = input("Enter phrase: ")
	phrase_char_count = count_chars(phrase)
	if not(validate_char_count(phrase_char_count)):
		ordered_char_count = collections.OrderedDict(sorted(phrase_char_count.items()))
		print("VALID: You'll need %s" % ordered_char_count)

