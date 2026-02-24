def show(label: str, a, b) -> None:
    print(f"\n{label}")
    print("a:", a, "id(a):", id(a))
    print("b:", b, "id(b):", id(b))
    print("a == b:", a == b)
    print("a is b:", a is b)


show("lists", [1, 2], [1, 2])

x = [1, 2]
y = x
show("same reference", x, y)

show("ints (256)", 256, 256)
show("strings ('hello')", "hello", "hello")
