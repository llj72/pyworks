#raise -> 에러 미뤄둔다. 사용하는 쪽에서 발생하도록 함.
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly()