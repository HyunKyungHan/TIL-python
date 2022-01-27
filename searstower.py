#One morning, you go out and place a dollar bill on the sidewalk by the Sears tower in Chicago.
#Each day thereafter, you go out double the number of bills.
#How long does it take for the stack of bills to exceed the height of the tower?

bill_thickness = 0.11*0.001 #지폐 한 장의 두께를 미터로 변환
height_sears = 442 #시어스 타워의 높이를 미터로 표현
num_bills = 1 #지폐의 수를 1로 초기화
day = 1 #날짜를 1로 초기화

while num_bills * bill_thickness < height_sears:
    print(day, num_bills, num_bills * bill_thickness)
    day += 1
    num_bills = num_bills*2

print('Number of days: ', day)
print('Number of bills: ', num_bills)
print('Final height: ', num_bills * bill_thickness)
