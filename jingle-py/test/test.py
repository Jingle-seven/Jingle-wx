

path="123456789"
path2="12"
print(path.replace("/",".").replace("\\",".").replace(":",""))
print(path[len(path2)-len(path):])
print(path[len(path2):])

if __name__=="__main__":
    print("end")