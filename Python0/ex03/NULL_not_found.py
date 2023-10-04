def NULL_not_found(object: any) -> int:
    obj_type = type(object).__name__

    if obj_type == None:
        print(f"None : {type(object)}")
    elif obj_type == float("NaN"):
        print(f"nan : {type(object)}")
    elif obj_type == 0:
        print(f"0 : {type(object)}")
    elif obj_type == "\"":
        print(f"\" : {type(object)}")
    elif obj_type == False:
        print(f"False : {type(object)}")
    else:
        print("Type not found")
    return 1
