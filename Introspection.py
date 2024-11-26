import inspect
from pprint import pprint


def introspection_info(obj):
    intro_dict = {}
    list_attr = []
    list_method = []


    # Тип объекта
    type_ = type(obj).__name__
    intro_dict['type'] = type_

    # Определяем что аттрибут(не вызывается), что метод(вызывается)
    for attr in dir(obj):
        if not callable(getattr(obj, attr)):
            list_attr.append(attr)
        else:
            list_method.append(attr)

    intro_dict['attribute'] = list_attr
    intro_dict['method'] = list_method
    intro_dict['module'] = __name__




    # for i in intro_dict:
    #     print(i, intro_dict[i])
    return intro_dict




number_info = introspection_info(42)
print(number_info)
print()
pprint(number_info)