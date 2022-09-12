class SortStrings:
    def sort(self, value):
        return " ".join(sorted(value.split(" "), key=str.casefold))
