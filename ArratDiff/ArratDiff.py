import codewars_test as test

def array_diff(a, b):
    # Convert the second list to a set for faster lookups
    b_set = set(b)
    # Use a list comprehension to filter out elements in 'a' that are in 'b'
    return [item for item in a if item not in b_set]

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(array_diff([1, 2], [1]), [2], "a was [1,2], b was [1], expected [2]")
        test.assert_equals(array_diff([1, 2, 2], [1]), [2, 2], "a was [1,2,2], b was [1], expected [2,2]")
        test.assert_equals(array_diff([1, 2, 2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
        test.assert_equals(array_diff([1, 2, 2], []), [1, 2, 2], "a was [1,2,2], b was [], expected [1,2,2]")
        test.assert_equals(array_diff([], [1, 2]), [], "a was [], b was [1,2], expected []")
        test.assert_equals(array_diff([1, 2, 3], [1, 2]), [3], "a was [1,2,3], b was [1, 2], expected [3]")

# If you want to run the tests directly, you can uncomment the following line:
# test.run()