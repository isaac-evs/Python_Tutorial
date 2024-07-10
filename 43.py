# Eval + Exec
# Warning! be very careful when using Exec and Eval

print(eval("'test'.upper()"))

exec("if True:print('test')")

exec("a = 10")

print(a)

################################

my_list = ["upper", "title", "lower", "casefold"]
my_string = "test"

for i in my_list:
    print(eval(f"my_string.{i}()"))
