def NULL_not_found(object: any) -> int:
    obj_type = type(object).__name__

    if obj_type == 'NoneType':
        print(f"Nothing: {object} <class '{obj_type}'>")
    elif obj_type == 'float' and str(object) == 'nan':
        print(f"Cheese: {object} <class '{obj_type}'>")
    elif obj_type == 'int' and object == 0:
        print(f"Zero: {object} <class '{obj_type}'>")
    elif obj_type == 'str' and object == '':
        print(f"Empty: {object} <class '{obj_type}'>")
    elif obj_type == 'bool':
        print(f"Fake: {object} <class '{obj_type}'>")
    else:
        print("Type not Found")
    return 1
