class multifilter:
    def judge_half(pos, neg):
        return pos >= neg
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(pos, neg):
        return pos >= 1
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(pos, neg):
        return neg == 0
        # допускает элемент, если его допускают все функции (neg == 0)

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    # iterable - исходная последовательность
    # funcs - допускающие функции
    # judge - решающая функция

    def __iter__(self):
        for i in self.iterable:
            pos = 0
            neg = 0

            for func in self.funcs:
                if func(i):
                    pos += 1
                else:
                    neg += 1

            if self.judge(pos, neg):
                yield i
    # возвращает итератор по результирующей последовательности
