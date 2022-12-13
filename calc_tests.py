import calc

assert calc.calc("3 + 5") == 8, "failed test: answer should be 8"
assert calc.calc("0 + 5") == 5, "failed test: answer should be 5"
assert calc.calc("4 * 3") == 12, "failed test: answer should be 12"
assert calc.calc("80 * 2") == 160, "failed test: answer should be 160"
assert calc.calc("3 - 5") == -2, "failed test: answer should be -2"
assert calc.calc("55 - 27") == 28, "failed test: answer should be 28"
assert calc.calc("4 // 4") == 1, "failed test: answer should be 1"
assert calc.calc("5 // 1") == 5, "failed test: answer should be 5"
assert calc.calc("64 // 2") == 1, "failed test: answer should be 32"
print("all tests passed")
