# class TestClass:
#     value:int = 0

#     def test_one(self):
#         self.value = 1
#         assert self.value == 2


class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")     