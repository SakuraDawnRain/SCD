def display_info(state, progress, extensions, resources):
    print("******************************************")
    print(state.show())
    print("******************************************")
    print("模型训练进度 = {}%".format(str(progress)))
    print("******************************************")
    print("插件列表")
    for i in range(len(extensions)):
        print("- 【{}】".format(extensions[i].name))
    print("******************************************")
    print("资源列表")
    for i in resources.keys():
        print("{}: {}".format(resources[i], i))
    print("******************************************")