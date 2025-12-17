with open("input/day12.txt", "r") as f:
    boxes = f.read()
    
boxes = boxes.split("\n\n")

instances = boxes[6].strip().split("\n")
instances = [instance.strip().split(":") for instance in instances]
instances = [(i[0].split("x"), i[1].strip().split(" ")) for i in instances]
instances = [((int(a[0]), int(a[1])), list(map(int, b))) for (a, b) in instances]

sizes = [5, 7, 7, 6, 7, 7]

def too_big(instance) -> bool:
    ((x, y), amounts) = instance
    total_area = x * y
    total_needed = 0
    for i, amount in enumerate(amounts):
        total_needed += sizes[i] * amount
    return total_needed > total_area
 
def certainly_fits(instance) -> bool:
    ((x, y), amounts) = instance
    horizontal_shapes = x // 3
    vertical_shapes = y // 3
    total_shapes_easy = horizontal_shapes * vertical_shapes
    total_shapes_necessary = sum(amounts)
    return total_shapes_necessary <= total_shapes_easy

too_bigs = 0
easy_fits = 0
for i, instance in enumerate(instances):
    if too_big(instance):
        too_bigs += 1
    if certainly_fits(instance):
        easy_fits += 1

print(too_bigs, easy_fits, len(instances))