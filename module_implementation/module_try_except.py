try:
    import xyz
    import calc

except ImportError:
    print("module is not present")
print(calc.a)
print(calc.b)