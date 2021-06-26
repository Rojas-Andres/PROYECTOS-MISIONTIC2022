from cliente import cliente
import inspect

print(dir(cliente))
src = inspect.getsource(cliente)
print(src)