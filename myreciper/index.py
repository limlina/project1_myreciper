# 오픈소스기초프로젝트 - 12조 룰루랄라파이썬

from recipe_list import *

mylist = []

def main():
    while True:
        print("===========================")
        print("My Reciper")
        print("===========================")
        print("1. 소개")
        print("2. 재료 목록")
        print("3. 레시피 추천")
        print("0. 종료")
        print("===========================")
        menu = int(input("선택 : "))

        if menu == 1:
            introduce()
        elif menu == 2:
            ingredient_list()
        elif menu == 3:
            recipe_recommend()
        elif menu == 0:
            exit()
        else:
            return main()

def introduce():
    print(" * 프로그램명 : My Reciper ")
    print(" * 12조 룰루랄라 파이썬 ")
    print(" * 냉장고에 남아있는 재료들을 이용하여 만들 수 있는 레시피를 추천해주는 프로그램 ")
    print("\n")

def ingredient_list():
    print("\n")
    print("===========================")
    print("재료목록")
    print("===========================")
    print("1. 재료 입력")
    print("2. 재료 삭제")
    print("3. 재료 목록 초기화")
    print("4. 재료 목록 보기")
    print("0. 재료 목록 종료")
    print("===========================")
    menu2 = int(input("선택 : "))

    if menu2 == 1:
        print("**---------------------------------------------------------**")
        print("한개씩 입력하세요. 0 입력시 종료")
        print("**---------------------------------------------------------**")
        while True:
            ingredients = input("추가할 재료를 입력하세요. : ")

            if ingredients == "0":
                print(" %s " % mylist)
                break

            mylist.append(ingredients)
            print(" %s " % mylist)

    elif menu2 == 2:
        print("\n")
        print("**---------------------------------------------------------**")
        print("한개씩 입력하세요. 0 입력시 종료")
        print("**---------------------------------------------------------**")
        while True:
            ingredients2 = input("삭제할 재료를 입력하세요 : ")

            if ingredients2 == "0":
                print(" %s " % mylist)
                break

            elif ingredients2 in mylist:
                mylist.remove(ingredients2)
                print(" %s " % mylist)

            elif ingredients2 not in mylist:
                print(" %s " % mylist)
                print("입력하신 재료는 재료목록에 없는 재료입니다.")

    elif menu2 == 3:
        while True:
            mylist.clear()
            print("-> 재료목록이 초기화 되었습니다.")
            print(" %s " % mylist)
            break

    elif menu2 == 4:
         print(" %s " % mylist)

    elif menu2 == 0:
        main()

    else:
        return ingredient_list()

def recipe_recommend():
    while True:
        print("1. 레피시 검색")
        print("2. 종료")
        choice = input(" 선택 >>  ")  # 선택한 메뉴 실행
        print()

        if choice == "1":  # '1. 레시피 검색'의 경우
            while True:
                recipe_igd = input("사용할 재료를 입력해주세요(쉼표로 구분) : ")  # 당근, 양파, 대파, 밥 처럼 쉼표로 구분하여 입력
                recipe_igd = recipe_igd.split(",")  # 문자열을 쉼표 단위로 나눠 리스트로 저장
                for idx, r in enumerate(recipe_igd):
                    recipe_igd[idx] = r.strip()  # 각 단어의 양쪽 공백 제거 >> " 당근 "이면 "당근"으로

                if len(recipe_igd) < 3 or len(recipe_igd) > 10:  # 입력된 재료가 3개미만이거나 10개 초과면 오류후 재입력
                    print("재료가 너무 적거나 많습니다.")
                else:
                    break
            print()

            while True:
                print("    1. 등록한 재료만 이용")
                print("    2. 추가 재료까지 이용")

                search_type = input("     선택 >>  ")  # 원하는 메뉴 선택
                print()

                if search_type == "1" or search_type == "2":  # 1번이나 2번이면 선택완료
                    break
                else:
                    print("잘못된 선택입니다.")  # 다른번호면 재선택

            if search_type == "1":  # 등록한 재료만 이용
                recipe_title = []  # 레시피 제목들 저장 리스트
                recipe_rate = []  # 재료 일치율 저장 리스트

                for k in recipe:  # 저장된 모든 레시피 탐색
                    count = 0
                    for i in recipe[k]["재료"]:
                        if i in recipe_igd:  # 저장된 재료가 입력한 재료에 있으면 count 1 증가
                            count = count + 1

                    cmp_rate = count / len(recipe[k]["재료"])  # count를 현 레시피의 재료 개수로 나누어서 비율 계산

                    if cmp_rate > 0.85:  # 0.85 이상의 일치율을 가진 레시피만 저장
                        recipe_rate.append(cmp_rate)
                        recipe_title.append(k)

                    for i in range(len(recipe_rate) - 1):  # 정렬알고리즘(버블 소트)으로 정렬  (정확도순)
                        for j in range(len(recipe_rate) - i):
                            if j == 0:
                                continue
                            if recipe_rate[j - 1] < recipe_rate[j]:
                                recipe_rate[j - 1], recipe_rate[j] = recipe_rate[j], recipe_rate[j - 1]
                                recipe_title[j - 1], recipe_title[j] = recipe_title[j], recipe_title[j - 1]

                for r in recipe_title:  # 저장된 내용 출력
                    print(r)

            elif search_type == "2":  # 추가 재료까지 이용
                recipe_title = []  # 레시피 제목들 저장 리스트
                recipe_rate = []  # 재료 일치율 저장 리스트

                for k in recipe:  # 저장된 모든 레시피 탐색
                    count = 0
                    for i in recipe_igd:
                        if i in recipe[k]["재료"]:  # 입력한 재료가 저장된 재료에 있으면 count 1 증가
                            count = count + 1

                    cmp_rate = count / len(recipe[k]["재료"])  # count를 현 레시피의 재료 개수로 나누어서 비율 계산

                    if cmp_rate > 0.15:  # 0.15 이상의 일치율을 가진 레시피만 저장
                        recipe_rate.append(cmp_rate)
                        recipe_title.append(k)

                    for i in range(len(recipe_rate) - 1):  # 정렬알고리즘(버블 소트)으로 정렬  (정확도순)
                        for j in range(len(recipe_rate) - i):
                            if j == 0:
                                continue
                            if recipe_rate[j - 1] < recipe_rate[j]:
                                recipe_rate[j - 1], recipe_rate[j] = recipe_rate[j], recipe_rate[j - 1]
                                recipe_title[j - 1], recipe_title[j] = recipe_title[j], recipe_title[j - 1]

                for r in recipe_title:
                    print(r, "  ", "필요한 추가 재료 : ", end='')
                    for m in recipe[r]["재료"]:
                        if m not in recipe_igd:
                            print(m, " ", end='')
                    print()

            print()

            recipe_k = input("레시피를 확인하실 메뉴를 입력하세요 : ")  # 레시피 제목 입력해서 레시피 출력
            for r in recipe[recipe_k]["레시피"]:
                print(r)

            print()
        elif choice == "2":  # '2. 종료'의 경우
            break
        else:
            print("잘못된 선택입니다.")
            print()

main()