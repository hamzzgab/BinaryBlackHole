from src.main.arrays.dynamic.resizable_array import DynamicArray


class TestResizableArray:

    @classmethod
    def setup(cls, capacity: int) -> DynamicArray:
        da = DynamicArray(capacity)
        return da

    def test_initialization_should_set_correct_capacity_and_empty_array(self):
        capacity = 3
        da = self.setup(capacity)

        assert da.capacity == capacity
        assert da.arr == [-1, -1, -1]
        assert da.len is 0

    def test_get_should_return_none_when_index_exceeds_capacity(self):
        capacity = 3
        da = self.setup(capacity)

        index = capacity + 1
        act_value = da.get(index)

        assert act_value is None

    def test_get_should_return_value_at_valid_index(self):
        capacity, index = 3, 2
        da = self.setup(capacity)

        da.arr = [1, 2, 3]
        act_value = da.get(index)

        assert act_value is 3

    def test_pushback_should_resize_when_full(self):
        capacity = 3
        da = self.setup(capacity)

        for i in range(1, capacity + 2): da.pushback(i)

        assert da.arr == [1, 2, 3, 4, -1, -1]
        assert da.len == 4

    def test_popback_should_remove_values(self):
        capacity = 3
        da = self.setup(capacity)

        for i in range(1, capacity + 1): da.pushback(i)
        for i in range(capacity, 0, -1): assert da.popback() == i

    def test_popback_should_return_none_when_no_values(self):
        capacity = 3
        da = self.setup(capacity)

        assert da.popback() is None
