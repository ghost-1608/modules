import traceback
import sys
import math


class DimensionalError(Exception):
    pass


class matrix:
    def __init__(self, argument, rep=None):
        if argument.__class__.__name__ == 'int' and rep is not None:
            if argument == 0:
                self.__l = [[0 for _ in range(rep)] for _ in range(rep)]
            elif abs(argument) == 1:
                self.__l = [[0 for _ in range(rep)] for _ in range(rep)]

                for i in range(len(self.__l)):
                    self.__l[i][i] = math.copysign(self.__l[i][i], argument)
        else:
            if rep is not None:
                try:
                    raise TypeError("matrix construction using iterable expects at most 1 argument, got 2")
                except TypeError:
                    print(traceback.format_exc().splitlines(keepends=True)[0] + ''.join(traceback.format_stack()[:-1]) +
                          traceback.format_exc().splitlines()[-1], file=sys.stderr)
                    sys.exit(1)

            self.__l = [[_ for _ in i] for i in argument]

            if 'list' not in str(type(self.__l)) and 'tuple' not in str(type(self.__l)) and 'set' not in str(type(self.__l)):
                try:
                    raise TypeError("'list', 'tuple', 'set', or 'range' object expected")
                except TypeError:
                    print(traceback.format_exc().splitlines(keepends=True)[0] + ''.join(traceback.format_stack()[:-1]) +
                          traceback.format_exc().splitlines()[-1], file=sys.stderr)

            for i in self.__l:
                if 'list' not in str(type(i)) and 'tuple' not in str(type(i)) and 'set' not in str(
                        type(i)) and 'range' not in str(type(i)):
                    try:
                        raise TypeError("'list', 'tuple', 'set', or 'range' object expected as rows")
                    except TypeError:
                        print(traceback.format_exc().splitlines(keepends=True)[0] + ''.join(traceback.format_stack()[:-1]) +
                              traceback.format_exc().splitlines()[-1], file=sys.stderr)

            for i in self.__l:
                for j in i:
                    if 'int' not in str(type(j)) and 'float' not in str(type(j)):
                        try:
                            raise TypeError("'int' or 'float' objects expected as elements")
                        except TypeError:
                            print(traceback.format_exc().splitlines(keepends=True)[0] + ''.join(
                                traceback.format_stack()[:-1]) +
                                  traceback.format_exc().splitlines()[-1], file=sys.stderr)

            for i in self.__l:
                if len(i) != len(self.__l[0]):
                    try:
                        raise ValueError('number of columns must be uniform')
                    except ValueError:
                        print(traceback.format_exc().splitlines(keepends=True)[0] + ''.join(traceback.format_stack()[:-1]) +
                              traceback.format_exc().splitlines()[-1], file=sys.stderr)

    def __dir__(self):
        return ['__module__', '__init__', '__str__', '__repr__', '__getitem__', 'rows', 'columns', '__setitem__',
                '__len__', 'degree', '__neg__', '__invert__', 'transpose', 'minor', 'cofactor', 'adjoint', 'inverse',
                '__add__', '__sub__', '__mul__', '__rmul__', '__dict__', '__weakref__', '__doc__', '__hash__',
                '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__',
                '__ge__', '__new__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__',
                '__format__', '__sizeof__', '__dir__', '__class__']

    def __str__(self):
        M = '['

        for i in range(len(self.__l)):
            M += '[' + ' '.join([str(_) for _ in self.__l[i]]) + ']'
            if i < len(self.__l) - 1:
                M += ' '
        M += ']'

        return M

    def __repr__(self):
        M = '['

        for i in range(len(self.__l)):
            M += '[' + ' '.join([str(_) for _ in self.__l[i]]) + ']'
            if i < len(self.__l) - 1:
                M += ' '
        M += ']'

        return M

    def __getitem__(self, item):
        c = False

        try:
            iter(item)
        except TypeError:
            c = ~c

        if c:
            try:
                raise TypeError("'" + item.__class__.__name__ + "' object is not iterable")
            except TypeError:
                print(traceback.format_exc().splitlines(keepends=True)[0] + ''.join(traceback.format_stack()[:-1]) +
                      traceback.format_exc().splitlines()[-1], file=sys.stderr)

        i, j = item

        if i >= len(self.__l) or j >= len(self.__l[0]):
            try:
                raise IndexError('matrix index out of range')
            except IndexError:
                print(traceback.format_exc().splitlines(keepends=True)[0] + ''.join(traceback.format_stack()[:-1]) +
                      traceback.format_exc().splitlines()[-1], file=sys.stderr)

        return self.__l[i][j]

    def rows(self):
        return self.__l

    def columns(self):
        return [[i[_] for i in self.__l] for _ in range(len(self.__l))]

    def __setitem__(self, key, value):
        c = False

        try:
            iter(key)
        except TypeError:
            c = ~c

        if c:
            try:
                raise TypeError("'" + key.__class__.__name__ + "' object is not iterable")
            except TypeError:
                print(traceback.format_exc().splitlines(keepends=True)[0] + ''.join(traceback.format_stack()[:-1]) +
                      traceback.format_exc().splitlines()[-1], file=sys.stderr)

        if len(key) != 2:
            try:
                raise ValueError('expected row, column')
            except ValueError:
                print(traceback.format_exc().splitlines(keepends=True)[0] + ''.join(traceback.format_stack()[:-1]) +
                      traceback.format_exc().splitlines()[-1], file=sys.stderr)

        i, j = key

        if i.__class__.__name__ == j.__class__.__name__ != 'int':
            try:
                raise TypeError('matrix indices must be integers')
            except TypeError:
                print(traceback.format_exc().splitlines(keepends=True)[0] + ''.join(traceback.format_stack()[:-1]) +
                      traceback.format_exc().splitlines()[-1], file=sys.stderr)

        if i >= len(self.__l) or j >= len(self.__l[0]):
            try:
                raise IndexError('matrix index out of range')
            except IndexError:
                print(traceback.format_exc().splitlines(keepends=True)[0] + ''.join(traceback.format_stack()[:-1]) +
                      traceback.format_exc().splitlines()[-1], file=sys.stderr)

        if value.__class__.__name__ != 'int' and value.__class__.__name__ != 'float':
            try:
                raise TypeError("'int' or 'float' object expected as values")
            except TypeError:
                print(traceback.format_exc().splitlines(keepends=True)[0] + ''.join(traceback.format_stack()[:-1]) +
                      traceback.format_exc().splitlines()[-1], file=sys.stderr)

        self.__l[i][j] = value

    def __len__(self):
        return len(self.__l) * len(self.__l[0])

    def degree(self):
        return str(len(self.__l)) + 'x' + str(len(self.__l[0]))

    def __neg__(self):
        return self.__mul__(-1)

    def transpose(self):
        M = [[0 for _ in range(len(self.__l[0]))] for _ in range(len(self.__l))]

        for i in range(len(self.__l)):
            for j in range(len(self.__l[0])):
                M[i][j] = [k[i] for k in self.__l][j]

        for i in range(len(M)):
            for j in range(len(M[i])):
                while True:
                    if 'list' in str(type(M[i][j])):
                        M[i][j] = M[i][j][0]
                    else:
                        break

        return matrix(M)

    def minor(self, i, j):
        return matrix([[l for l in list(k[:j]) + list(k[j + 1:])] for k in list(self.__l[:i]) + list(self.__l[i + 1:])])

    def cofactor(self, i, j):
        C = None

        if i >= len(self.__l) or j >= len(self.__l[0]):
            try:
                raise IndexError('matrix index out of range')
            except TypeError:
                print(traceback.format_exc().splitlines(keepends=True)[0] + ''.join(traceback.format_stack()[:-1]) +
                      traceback.format_exc().splitlines()[-1], file=sys.stderr)

        if len(self.__l) == len(self.__l[0]):
            C = self.minor(i, j)

            if len(eval(str(C))[0]) != 1:
                C = determinant(C)
            else:
                C = eval(str(C))[0][0]
            C *= (-1) ** (i + j)

        return C

    def inverse(self):
        M = None

        if determinant(matrix(self.__l)) is not None:
            M = 1 / determinant(matrix(self.__l)) * adjoint(matrix(self.__l))

        return M

    def __add__(self, other):
        M = [[0 for _ in range(len(self.__l[0]))] for _ in range(len(self.__l))]

        if not isinstance(other, matrix):
            try:
                raise TypeError("unsupported operand type(s) for +: 'matrix' and '" + other.__class__.__name__ + "'")
            except TypeError:
                print(traceback.format_exc().splitlines(keepends=True)[0] + ''.join(traceback.format_stack()[:-1]) +
                      traceback.format_exc().splitlines()[-1], file=sys.stderr)

        if len(other.rows()) != len(self.__l) or len(other.columns()) != len(self.__l[0]):
            try:
                raise DimensionalError('unsupported operation between different dimensions for +')
            except DimensionalError:
                print(traceback.format_exc().splitlines(keepends=True)[0] + ''.join(traceback.format_stack()[:-1]) +
                      traceback.format_exc().splitlines()[-1], file=sys.stderr)

        for i in range(len(M)):
            for j in range(len(M)):
                M[i][j] = self.__l[i][j] + other[i, j]

        return matrix(M)

    def __sub__(self, other):
        M = [[0 for _ in range(len(self.__l[0]))] for _ in range(len(self.__l))]

        if not isinstance(other, matrix):
            try:
                raise TypeError("unsupported operand type(s) for -: 'matrix' and '" + other.__class__.__name__ + "'")
            except TypeError:
                print(traceback.format_exc().splitlines(keepends=True)[0] + ''.join(traceback.format_stack()[:-1]) +
                      traceback.format_exc().splitlines()[-1], file=sys.stderr)

        if len(other.rows()) != len(self.__l) or len(other.columns()) != len(self.__l[0]):
            try:
                raise DimensionalError('unsupported operation between different dimensions for -')
            except DimensionalError:
                print(traceback.format_exc().splitlines(keepends=True)[0] + ''.join(traceback.format_stack()[:-1]) +
                      traceback.format_exc().splitlines()[-1], file=sys.stderr)

        for i in range(len(M)):
            for j in range(len(M)):
                M[i][j] = self.__l[i][j] - other[i, j]

        return matrix(M)

    def __mul__(self, other):
        M = None

        if other.__class__.__name__ == 'int' or other.__class__.__name__ == 'float':
            M = self.__l
            for i in range(len(M)):
                for j in range(len(M[i])):
                    M[i][j] *= other
            M = matrix(M)
        else:
            if ismultipliable(matrix(self.__l), other):
                l1, l2 = len(self.__l), len(other.rows())

                M = [[0 for _ in range(l2)] for _ in range(l1)]

                for j in range(l1):
                    for k in range(l2):
                        for n in range(l2):
                            M[j][k] += self.__l[j][n] * other[n, k]
                M = matrix(M)

        return M

    def __rmul__(self, other):
        M = None

        if other.__class__.__name__ == 'int' or other.__class__.__name__ == 'float':
            M = self.__l
            for i in range(len(M)):
                for j in range(len(M[i])):
                    M[i][j] *= other
            M = matrix(M)
        else:
            if ismultipliable(other, matrix(self.__l)):
                l1, l2 = len(other.rows()), len(self.__l)

                M = [[0 for _ in range(l2)] for _ in range(l1)]

                for j in range(l1):
                    for k in range(l2):
                        for n in range(l2):
                            M[j][k] += self.__l[j][n] * other[n, k]
                M = matrix(M)

        return M

    def __pow__(self, other):
        M = self

        if other.__class__.__name__ != 'int':
            try:
                raise TypeError(
                    "unsupported operand type(s) for ** or pow(): 'matrix' and '" + other.__class__.__name__ + "'")
            except TypeError:
                print(traceback.format_exc().splitlines(keepends=True)[0] + ''.join(traceback.format_stack()[:-1]) +
                      traceback.format_exc().splitlines()[-1], file=sys.stderr)

        for i in range(other):
            M *= self

        return M


def ismatrix(List):
    c = False

    if 'list' in str(type(List)) or 'tuple' in str(type(List)) or 'set' in str(type(List)):
        c = True
        for i in List:
            if 'list' not in str(type(i)) and 'tuple' not in str(type(i)) and 'set' not in str(
                    type(i)) and 'range' not in str(type(i)):
                c = False
        if c:
            for i in List:
                for j in i:
                    if 'int' not in str(type(j)) and 'float' not in str(type(j)):
                        c = False
            if c:
                for i in List:
                    if len(i) != len(List[0]):
                        c = False
    return c


def ismultipliable(*args):
    for i in args:
        if not isinstance(i, matrix):
            try:
                raise TypeError("expected 'matrix' object, got '" + i.__class__.__name__ + "' object instead")
            except TypeError:
                print(traceback.format_exc().splitlines(keepends=True)[0] + ''.join(traceback.format_stack()[:-1]) +
                      traceback.format_exc().splitlines()[-1], file=sys.stderr)

    M = len(args[0].rows())

    for i in args:
        if M != len(i.columns()):
            return False
    return True


def determinant(Matrix):
    D = None

    if Matrix.__class__.__name__ != 'matrix':
        try:
            raise TypeError('object of type ' + Matrix.__class__.__name__ + ' has no determinant()')
        except TypeError:
            print(traceback.format_exc().splitlines(keepends=True)[0] + ''.join(traceback.format_stack()[:-1]) +
                  traceback.format_exc().splitlines()[-1], file=sys.stderr)

    if len(Matrix.rows()) == len(Matrix.columns()):
        D = 0
        for j in range(len(Matrix.columns())):
            D += Matrix[0, j] * Matrix.cofactor(0, j)

    return D


def adjoint(Matrix):
    M = matrix([[0 for _ in range(len(Matrix.columns()))] for _ in range(len(Matrix.rows()))])

    if Matrix.__class__.__name__ != 'matrix':
        try:
            raise TypeError('object of type ' + Matrix.__class__.__name__ + ' has no adjoint()')
        except TypeError:
            print(traceback.format_exc().splitlines(keepends=True)[0] + ''.join(traceback.format_stack()[:-1]) +
                  traceback.format_exc().splitlines()[-1], file=sys.stderr)

    for i in range(len(M.rows())):
        for j in range(len(M.columns())):
            if Matrix.cofactor(i, j) is not None:
                M[i, j] = Matrix.cofactor(i, j)

    M = M.transpose()

    return M


def multiply(*args):
    M, m = None, eval(str(args[0]))

    if ismultipliable(args[0]):
        for i in range(1, len(args)):
            m2 = eval(str(args[i]))
            l1, l2 = len(m), len(m2[0])

            M = [[0 for _ in range(l2)] for _ in range(l1)]

            for j in range(l1):
                for k in range(l2):
                    for n in range(len(m[0])):
                        M[j][k] += m[j][n] * [i[k] for i in m2][n]
            m = M
    return matrix(M)


def multiply_scalar(Scalar, Matrix):
    if 'int' not in str(type(Scalar)) and 'float' not in str(type(Scalar)):
        try:
            raise TypeError("expected an 'int' or 'float' object for the first parameter")
        except TypeError:
            print(traceback.format_exc().splitlines(keepends=True)[0] + ''.join(traceback.format_stack()[:-1]) +
                  traceback.format_exc().splitlines()[-1], file=sys.stderr)

    if 'matrix' not in str(type(Matrix)):
        try:
            raise TypeError("expected a 'matrix' object for the second parameter")
        except TypeError:
            print(traceback.format_exc().splitlines(keepends=True)[0] + ''.join(traceback.format_stack()[:-1]) +
                  traceback.format_exc().splitlines()[-1], file=sys.stderr)

    M = eval(str(Matrix))
    for i in range(len(M)):
        for j in range(len(M[i])):
            M[i][j] *= Scalar
    return matrix(M)


def prettify(Matrix):
    m = Matrix

    for i in range(len(m)):
        for j in range(len(m[i])):
            if int(m[i][j]) == m[i][j]:
                m[i][j] = int(m[i][j])

    M = ''
    for i in range(len(m)):
        for j in range(len(m[i])):
            M += (' ', '')[m[i][j] < 0] + str(m[i][j]) + ('\t', '')[j == len(m[i]) - 1]
        M += ('\n', '')[i == len(m) - 1]
    return M
