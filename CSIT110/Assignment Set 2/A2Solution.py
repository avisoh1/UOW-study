name = 'Solution'
student_num = '12343545'  # Student number 
subject_code = 'SCIT110'  # SCIT110 or SP420

def map_to_dict(list1: list, list2: list) -> dict:
    new_dict = {}
    for i in range(0, len(list1)):
        new_dict[list1[i]] = list2[i]
    return new_dict


def report_cases(N: int = 0, disease: str = "heat stroke"):
    print(f"There are {N} {disease} case(s) today.")


def get_subscription():
    items = {
        "6 Apples": 5.4,
        "Mixed Vegetables Pack 1kg": 9.32,
        "Yakult 5 in a pack": 3.2,
        "Mixed nuts 500g": 16.98,
        "Milk Powder 200g": 9.47,
        "Roasted Chicken Breast 1kg": 8.56
        }

    def format_money(price: float):
        return f"${price:.2f}"
    print("Food items available for subscription (price/week)")
    for item in items:
        print(f"{item:<41}{format_money(items[item]):>9}")
    print()
    selection = []
    for item in items:
        q = "\""
        user_input = input(f"Add {q}{item}{q} to subscription? (Y/N): ")
        if user_input.lower() == "y":
            selection.append(item)

    print()
    print("Your selection: ")
    total_cost = 0
    if len(selection) == 0:
        print(" - None")
    else:
        for item in selection:
            print(f" - {item} ({format_money(items[item])})")
            total_cost += items[item]
    print()
    print(f"Total cost {format_money(total_cost)}")


def generate_qns_from_list(lst: list):
    math_qns = []
    for ele in lst:
        if len(ele) > 2:
            op = ele[0]
            qns = str(ele[1])
            ans = ele[1]
            for idx in range(2, len(ele)):
                if op == "+":
                    qns += " + " + str(ele[idx])
                    ans += ele[idx]
                elif op == "-":
                    qns += " - " + str(ele[idx])
                    ans -= ele[idx]
                elif op == "x":
                    qns += " x " + str(ele[idx])
                    ans *= ele[idx]
                else:
                    qns += " / " + str(ele[idx])
                    ans /= ele[idx]
            math_qns.append({"qns": qns, "ans": ans})
    return math_qns


class BackPack(object):
    """docstring for BackPack"""
    style = "basic"

    def __init__(self, account_id: str):
        self.account_id = account_id
        self.inventory = {}

    def add_item_to_bag(self, item_name: str, quantity: int):
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity

    def remove_item_from_bag(self, item_name: str, quantity: int) -> None:
        if self.inventory[item_name] == quantity:
            del self.inventory[item_name]
        else:
            self.inventory[item_name] -= quantity

    def empty_bag(self) -> None:
        self.inventory.clear()

    def count_items(self) -> int:
        count = 0
        for quantity in self.inventory.values():
            count += quantity
        return count


def main():
    pass
    print(map_to_dict(
        ["one", "two", "three"],
        [1, 2, 3]) == {"one": 1, "two": 2, "three": 3})
    get_subscription()
    input_list = [
        ["+", 1, 3, 3],
        ["-", 2, 5, -1],
        ["x", 3, 2],
        ["/", 12, 3, 2],
        ["x", 0, 23],
        ["+", 1, 2, 3, 4]]
    print(
        generate_qns_from_list(input_list) == [
            {"qns": "1 + 3 + 3", "ans": 7},
            {"qns": "2 - 5 - -1", "ans": -2},
            {"qns": "3 x 2", "ans": 6},
            {"qns": "12 / 3 / 2", "ans": 2},
            {"qns": "0 x 23", "ans": 0},
            {"qns": "1 + 2 + 3 + 4", "ans": 10}])
    bag = BackPack("394eds7A")
    bag.add_item_to_bag("dagger", 1)
    bag.add_item_to_bag("wooden sword", 2)
    bag.add_item_to_bag("red potion", 3)
    bag.add_item_to_bag("red potion", 2)
    print(bag.inventory == {"dagger": 1, "wooden sword": 2, "red potion": 5})
    bag.remove_item_from_bag("wooden sword", 1)
    bag.remove_item_from_bag("red potion", 5)
    print(bag.inventory == {"dagger": 1, "wooden sword": 1})
    print(bag.count_items() == 2)
    bag.empty_bag()
    print(bag.count_items() == 0)


if __name__ == '__main__':
    main()
