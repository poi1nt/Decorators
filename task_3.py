import types


def logger(old_function):
    import datetime

    def new_function(*args, **kwargs):
        date_and_time = datetime.datetime.now()
        result = old_function(*args, **kwargs)
        with open('main_task3.log', 'a+', encoding='utf-8') as file:
            text = f'{date_and_time}\n{old_function.__name__}\n{args}, {kwargs}\n{result}\n\n'
            file.write(text)
        return result
    
    return new_function

@logger
def flat_generator(list_of_lists):
    for list_ in list_of_lists:
        for item in list_:
            yield item

@logger
def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()