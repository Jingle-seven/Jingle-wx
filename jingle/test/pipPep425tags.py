import pip
print(pip.pep425tags.get_supported())
print(pip.__version__)
# import pip._internal
# print(pip._internal.pep425tags.get_supported())

# 无论如何都会提示AttributeError: module 'pip' has no attribute 'pep425tags'