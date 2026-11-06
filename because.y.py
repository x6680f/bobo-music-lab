
# 简易仓库管理程序

# 仓库数据，用字典存储
warehouse = {}


def add_goods():
    """添加商品"""
    name = input("请输入商品名称：")
    if name in warehouse:
        print("该商品已经存在！")
        return
    try:
        num = int(input("请输入商品库存数量："))
        price = float(input("请输入商品单价："))
        warehouse[name] = {"stock": num, "price": price}
        print(f"✅ 商品【{name}】添加成功！")
    except ValueError:
        print("❌ 输入的数量/单价必须是数字！")


def search_goods():
    """查询商品"""
    name = input("输入要查询的商品名：")
    if name in warehouse:
        item = warehouse[name]
        print(f"\n📦商品：{name} | 库存：{item['stock']} | 单价：{item['price']:.2f}元")
    else:
        print("❌ 没有找到该商品")


def update_stock():
    """修改库存"""
    name = input("输入要修改的商品名称：")
    if name not in warehouse:
        print("❌ 商品不存在")
        return
    try:
        new_num = int(input("输入新的库存数量："))
        warehouse[name]["stock"] = new_num
        print(f"✅【{name}】库存更新完成，当前库存 {new_num}")
    except ValueError:
        print("❌ 数量必须填整数！")


def delete_goods():
    """删除商品"""
    name = input("输入要删除的商品名称：")
    if name in warehouse:
        del warehouse[name]
        print(f"✅ 已删除商品【{name}】")
    else:
        print("❌ 找不到该商品")


def show_all():
    """打印全部仓库商品"""
    if not warehouse:
        print("\n📭仓库目前空空如也！")
        return
    print("\n===== 📋仓库全部库存列表 =====")
    for k, v in warehouse.items():
        print(f"商品:{k} | 库存:{v['stock']} | 单价:{v['price']:.2f}")


def main():
    while True:
        print("\n========= 仓库管理系统 =========")
        print("1. 添加商品")
        print("2. 查询商品")
        print("3. 修改库存")
        print("4. 删除商品")
        print("5. 查看全部库存")
        print("0. 退出程序")
        choice = input("\n请输入功能序号：")
        if choice == "1":
            add_goods()
        elif choice == "2":
            search_goods()
        elif choice == "3":
            update_stock()
        elif choice == "4":
            delete_goods()
        elif choice == "5":
            show_all()
        elif choice == "0":
            print("程序退出！")
            break
        else:
            print("⚠️无效输入，请重新选择！")


if __name__ == "__main__":
    main()
