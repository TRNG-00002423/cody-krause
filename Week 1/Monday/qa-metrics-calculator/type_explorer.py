from types import NoneType

age : int = 28
price : float = 19.99
name : str = "Alice"
is_active : bool = True
result : NoneType = None

print("Variable Exploration:")
print(f"{'age':<12}= {age:<8} (type: {type(age).__name__})")
print(f"{'price':<12}= {price:<8} (type: {type(price).__name__})")
print(f"{'name':<12}= {name:<8} (type: {type(name).__name__})")
print(f"{'is_active':<12}= {is_active:<8} (type: {type(is_active).__name__})")
print(f"{'result':<12}= {"None":<8} (type: {type(result).__name__})")

print("\nOperators Demo:")
print(f"  {'17 // 5':<12}= {17 // 5}")
print(f"  {'17 / 5':<12}= {17 / 5}")
print(f"  {'"QA " * 3':<12}= {'QA ' * 3}")
print(f"  {'True + True':<12}= {True + True}")

print("\nPrecision Gotcha:")
print(f"  {'0.1 + 0.2':<12}= {0.1 + 0.2} (not exactly 0.3!)")


print("\nDifference between == and is:")
str1 = "hello"
str2 = "world"
str3 = "".join(["he", "llo"])

print("str1 = 'hello', str2 = 'world', str3 = 'hello'")
print(f"  {'str1 == str2':<12}= {str1 == str2}")
print(f"  {'str1 is str2':<12}= {str1 is str2}")
print(f"  {'str1 == str3':<12}= {str1 == str3}")
print(f"  {'str1 is str3':<12}= {str1 is str3}")