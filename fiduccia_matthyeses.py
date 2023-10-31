
def fm(n,adj):
    area_vector = []
    part = [True if i > n // 2 else False for i in range(n)]
    initial_cut_cost = 0
    vis_1 = [0] * n
    
    for i in range(n):
        for it in adj[i]:
            if vis_1[i] == 0 or vis_1[it] == 0:
                if part[i] != part[it]:
                    initial_cut_cost += 1
                    vis_1[i] = 1
                    vis_1[it] = 1
    
    final_cut_cost = 0
    mn = float("inf")

    for j in range(60):
        flag = 0
        for i in range(n):
            if i < n // 2:
                part[i] = not part[i]   

        fixed = [0] * n

        for _ in range(5):
            f = fixed.count(1)

            if f == n:
                break

            gain = [0] * n

            for i in range(n):
                a = 0
                b = 0

                for it in adj[i]:
                    if part[it] == part[i]:
                        a += 1
                    else:
                        b += 1

                gain[i] = a - b

            max_gain = float("-inf")
            fix_index = -1

            for i in range(n):
                if gain[i] > max_gain and fixed[i] == 0:
                    fix_index = i
                    max_gain = gain[i]

            if fix_index > -1:
                fixed[fix_index] = 1
                part[fix_index] = not part[fix_index]

            final_cut_cost = 0
            vis_2 = [0] * n

            for i in range(n):
                for it in adj[i]:
                    if vis_2[i] == 0 or vis_2[it] == 0:
                        if part[i] != part[it]:
                            final_cut_cost += 1
                            vis_2[i] = 1
                            vis_2[it] = 1

            mn = min(mn, final_cut_cost)

            if flag == 1:
                break
         
    print("Part A:-", [i for i in range(n) if not part[i]])
    print("Part B:-", [i for i in range(n) if part[i]])
    print(initial_cut_cost, mn)
