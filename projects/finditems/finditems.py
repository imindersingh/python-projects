class FindItems:
    def index_all(self, input_list, value):
        index_list = []
        for i, lst in enumerate(input_list):
            if input_list[i] == value:
                index_list.append([i])
            elif isinstance(input_list[i], list):
                for index in FindItems.index_all(self, input_list[i], value):
                    index_list.append([i] + index)
        return index_list
