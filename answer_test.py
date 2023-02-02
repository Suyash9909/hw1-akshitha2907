import pytest
import answer

class TestAnswer():

    __correct__ = 0
    __total__ = 0

    @classmethod
    def setup_class(cls):
        print("Before")
        cls.__correct__ = 0
        cls.__total__ = 0

    @classmethod
    def teardown_class(cls):


        print(f"Score:{(cls.__correct__/cls.__total__)*100}%")
    def test_number_x(self):
        TestAnswer.__total__ += 1
        x,y = answer.number()
        assert(x==1024)
        TestAnswer.__correct__ += 1
    def test_number_7(self):
        TestAnswer.__total__ += 1
        x,y = answer.number()
        assert(y==1024/3)
        TestAnswer.__correct__ += 1
    def test_string_stevens(self):
        TestAnswer.__total__ += 1
        stevens, stevens_7, length, great, good = answer.strings()
        assert(stevens=="stevens")
        TestAnswer.__correct__ += 1

    def test_string_stevens_7(self):
        TestAnswer.__total__ += 1
        stevens, stevens_7, length, great, good = answer.strings()
        assert(stevens_7=="stevens"*7)
        TestAnswer.__correct__ += 1

    def test_string_stevens_length(self):
        TestAnswer.__total__ += 1
        stevens, stevens_7, length, great, good = answer.strings()
        assert(length==len(stevens_7))
        TestAnswer.__correct__ += 1

    def test_string_stevens_great(self):
        TestAnswer.__total__ += 1
        stevens, stevens_7, length, great, good = answer.strings()
        assert(great=="stevens is great")
        TestAnswer.__correct__ += 1

    def test_string_stevens_good(self):
        TestAnswer.__total__ += 1
        stevens, stevens_7, length, great, good = answer.strings()
        assert(good=="stevens is good")
        TestAnswer.__correct__ += 1

    def test_list_1D_hoboken(self):
        TestAnswer.__total__ += 1
        hoboken,hoboken_list, hoboken_first_item, l, new_l = answer.list_1D()
        assert(hoboken=="hoboken,is,awesome,i,like,it")
        TestAnswer.__correct__ += 1

    def test_list_1D_hoboken_list(self):
        TestAnswer.__total__ += 1
        hoboken,hoboken_list, hoboken_first_item, l, new_l = answer.list_1D()
        assert(hoboken_list=="hoboken,is,awesome,i,like,it".split(","))
        TestAnswer.__correct__ += 1

    def test_list_1D_hoboken_first_item(self):
        TestAnswer.__total__ += 1
        hoboken,hoboken_list, hoboken_first_item, l, new_l = answer.list_1D()
        assert(hoboken_first_item=="hoboken")
        TestAnswer.__correct__ += 1

    def test_list_1D_l(self):
        TestAnswer.__total__ += 1
        hoboken,hoboken_list, hoboken_first_item, l, new_l = answer.list_1D()
        assert(l==[-6, -2, 0, 0, 1, 2, 3, 4, 5, 6, 9, 10, 12, 13, 15])
        TestAnswer.__correct__ += 1

    def test_list_1D_new_l(self):
        TestAnswer.__total__ += 1
        hoboken,hoboken_list, hoboken_first_item, l, new_l = answer.list_1D()
        assert(new_l==[0, 1, 2, 3, 4, 5, 6])
        TestAnswer.__correct__ += 1

    def test_list_2D_A(self):
        TestAnswer.__total__ += 1
        A,last_column, a, b = answer.list_2D()
        assert (A == [[1, 4, 5],
                    [6, 10, 11],
                    [12, 17, 38]])
        TestAnswer.__correct__ += 1

    def test_list_2D_last_row(self):
        TestAnswer.__total__ += 1
        A,last_column, a, b = answer.list_2D()
        assert (last_column == [5,11,38])
        TestAnswer.__correct__ += 1

    def test_list_2D_a(self):
        TestAnswer.__total__ += 1
        A,last_column, a, b = answer.list_2D()
        assert (a == 38)
        TestAnswer.__correct__ += 1

    def test_list_2D_b(self):
        TestAnswer.__total__ += 1
        A,last_column, a, b = answer.list_2D()
        assert (b == 6)
        TestAnswer.__correct__ += 1

    def test_dictionary_f(self):
        TestAnswer.__total__ += 1
        fruit_dict,f= answer.dictionary()
        assert(f=="apple")
        TestAnswer.__correct__ += 1

    def test_dictionary_quantity(self):
        TestAnswer.__total__ += 1
        fruit_dict, f= answer.dictionary()
        assert(fruit_dict["quantity"]==19)
        TestAnswer.__correct__ += 1

    def test_dictionary_nested_last_name(self):
        TestAnswer.__total__ += 1
        Grace,last_name, job= answer.dictionary_nested()
        assert(last_name=="Hopper")
        TestAnswer.__correct__ += 1

    def test_dictionary_nested_job(self):
        TestAnswer.__total__ += 1
        Grace,last_name, job= answer.dictionary_nested()
        assert(job=="programmer")
        TestAnswer.__correct__ += 1