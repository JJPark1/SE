def solution(max_weight, specs, names):
    specs = dict(specs)
    truck = 1 # 필요한 트럭 수
    weight = 0 # 상품의 무게
    for i in names:
        weight += int(specs.get(i))
        if weight > max_weight:
            truck += 1
            weight = int(specs.get(i))
    return truck

