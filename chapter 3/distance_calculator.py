dot1 = tuple(map(int, input("점1: ").replace('(','').replace(')','').split(',')))
dot2 = tuple(map(int, input("점2: ").replace('(','').replace(')','').split(',')))

print(f"두 점 사이의 거리: {((dot2[0] - dot1[0])**2 + (dot2[1] - dot1[1])**2)**0.5:.1f}")