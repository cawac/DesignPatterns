from book_proxy import BookProxy


if __name__ == "__main__":
    book_proxy1 = BookProxy(1)
    book_proxy2 = BookProxy(2)
    book_proxy3 = BookProxy(3)

    print("Testing with book 1:")
    print(f"Try access to Book 1 from User 1 content:")
    book_proxy1.get_book(1)
    print(f"Try access to Book 1 from User 2 content:")
    book_proxy2.get_book(1)
    print(f"Try access to Book 1 from User 3 content:")
    book_proxy3.get_book(1)

    print("\nTesting with book 2:")
    print(f"Try access to Book 2 from User 1 content:")
    book_proxy1.get_book(2)
    print(f"Try access to Book 2 from User 2 content:")
    book_proxy2.get_book(2)
    print(f"Try access to Book 2 from User 3 content:")
    book_proxy3.get_book(2)

    print("\nTesting with book 3")
    print(f"Try access to Book 3 from User 1 content:")
    book_proxy1.get_book(3)
    print(f"Try access to Book 3 from User 2 content:")
    book_proxy2.get_book(3)
    print(f"Try access to Book 3 from User 3 content:")
    book_proxy3.get_book(3)