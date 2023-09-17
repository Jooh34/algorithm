def solution(bridge_length, weight, truck_weights):
    b = [0] * bridge_length
    total_weight = 0
    t = 0

    while truck_weights:
        truck = truck_weights[0]
        # max weight
        if weight < total_weight+truck:
            while True:
                arrive = b.pop(0)
                b.append(0)
                t+=1
                if arrive != 0:
                    total_weight -= arrive
                    break

            if weight >= total_weight+truck:
                b.pop(-1)
                b.append(truck)
                total_weight += truck
                truck_weights.pop(0)
        
        else: # new truck
            total_weight -= b.pop(0)
            b.append(truck)
            total_weight += truck
            truck_weights.pop(0)
            t+=1
    
    while total_weight != 0:
        total_weight -= b.pop(0)
        b.append(0)
        t+=1

    return t


q1 = [2, 10, [7,4,5,5]]
print(solution(*q1))