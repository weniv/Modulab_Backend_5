# SQLAlchemy 연습문제 정답지
# ========================================

# 문제 1번 정답
def solution_1():
    """김철수 사용자의 모든 주문 정보 출력"""
    user = session.query(User).filter(User.username == "김철수").first()
    
    if not user:
        print("김철수 사용자를 찾을 수 없습니다.")
        return
    
    print(f"사용자 이름: {user.username}")
    print(f"총 주문 수: {len(user.orders)}개")
    print("주문 상세:")
    
    for order in user.orders:
        print(f"  - 주문 ID: {order.id}")
        print(f"    주문 금액: {order.total_amount:,.0f}원")
        print(f"    주문 상태: {order.status}")
        print()

# 문제 2번 정답  
def solution_2():
    """각 사용자별 주문 통계"""
    users = session.query(User).all()
    
    print("👥 사용자별 주문 통계")
    print("=" * 50)
    
    for user in users:
        if user.orders:
            total_orders = len(user.orders)
            total_amount = sum(order.total_amount for order in user.orders)
            avg_amount = total_amount / total_orders
            
            print(f"🧑 {user.username}")
            print(f"  총 주문 횟수: {total_orders}회")
            print(f"  총 주문 금액: {total_amount:,.0f}원")
            print(f"  평균 주문 금액: {avg_amount:,.0f}원")
        else:
            print(f"🧑 {user.username}")
            print(f"  주문 없음")
        print()

# 문제 3번 정답
def solution_3():
    """전자제품 중 재고 30개 이상, 가격 순 정렬"""
    products = session.query(Product).filter(
        and_(Product.category == "전자제품", Product.stock >= 30)
    ).order_by(desc(Product.price)).all()
    
    print("💻 조건에 맞는 전자제품들")
    print("=" * 60)
    
    for product in products:
        print(f"📦 제품명: {product.name}")
        print(f"   가격: {product.price:,.0f}원")
        print(f"   재고: {product.stock}개")
        
        # 이 제품을 주문한 사용자들 찾기
        buyers = set()  # 중복 제거용
        for order_item in product.order_items:
            buyer_name = order_item.order.user.username
            buyers.add(buyer_name)
        
        if buyers:
            print(f"   구매자들: {list(buyers)}")
        else:
            print(f"   구매자: 없음")
        print()

# 문제 4번 정답
def solution_4():
    """카테고리별 통계"""
    # 모든 카테고리 가져오기
    category_groups = session.query(Product.category).distinct().all()
    
    print("📊 카테고리별 통계")
    print("=" * 60)
    
    for (category,) in category_groups:
        # 해당 카테고리의 모든 제품들
        products_in_category = session.query(Product).filter(
            Product.category == category
        ).all()
        
        # 카테고리 내 제품 수
        product_count = len(products_in_category)
        
        # 카테고리 내 평균 가격
        total_price = sum(p.price for p in products_in_category)
        avg_price = total_price / product_count if product_count > 0 else 0
        
        # 이 카테고리 제품들을 구매한 고유 사용자들
        unique_buyers = set()
        for product in products_in_category:
            for order_item in product.order_items:
                unique_buyers.add(order_item.order.user.username)
        
        print(f"📂 카테고리: {category}")
        print(f"   제품 수: {product_count}개")
        print(f"   평균 가격: {avg_price:,.0f}원")
        print(f"   구매 고객 수: {len(unique_buyers)}명")
        if unique_buyers:
            print(f"   구매 고객들: {list(unique_buyers)}")
        print()

# 문제 5번 정답
def solution_5():
    """VIP 고객 분석"""
    # VIP 후보자들 (활성 + 연봉 60000 이상)
    vip_candidates = session.query(User).filter(
        and_(User.is_active == True, User.salary >= 60000)
    ).all()
    
    vip_customers = []
    
    for user in vip_candidates:
        # 완료된 주문들만 필터링
        completed_orders = [order for order in user.orders if order.status == "completed"]
        
        if len(completed_orders) >= 1:  # 완료된 주문이 1개 이상
            # VIP 고객 정보 수집
            completed_order_count = len(completed_orders)
            total_completed_amount = sum(order.total_amount for order in completed_orders)
            max_single_order = max(order.total_amount for order in completed_orders)
            
            # 주문한 제품 카테고리들 (중복 제거)
            categories = set()
            for order in completed_orders:
                for order_item in order.order_items:
                    categories.add(order_item.product.category)
            
            vip_info = {
                'user': user,
                'completed_order_count': completed_order_count,
                'total_completed_amount': total_completed_amount,
                'max_single_order': max_single_order,
                'categories': list(categories)
            }
            vip_customers.append(vip_info)
    
    # 완료된 주문 총액 순으로 정렬 (내림차순)
    vip_customers.sort(key=lambda x: x['total_completed_amount'], reverse=True)
    
    print("👑 VIP 고객 분석 결과")
    print("=" * 70)
    
    if not vip_customers:
        print("VIP 조건을 만족하는 고객이 없습니다.")
        return
    
    for i, vip in enumerate(vip_customers, 1):
        user = vip['user']
        print(f"🏆 VIP 순위 {i}위")
        print(f"   고객명: {user.username}")
        print(f"   연봉: {user.salary:,.0f}원")
        print(f"   완료된 주문 수: {vip['completed_order_count']}개")
        print(f"   완료된 주문 총액: {vip['total_completed_amount']:,.0f}원")
        print(f"   가장 비싼 단일 주문: {vip['max_single_order']:,.0f}원")
        print(f"   주문한 카테고리들: {vip['categories']}")
        print()
    
    print(f"📈 총 VIP 고객 수: {len(vip_customers)}명")

# 모든 정답 실행 함수
def run_all_solutions():
    """모든 문제의 정답을 순서대로 실행"""
    print("🎯 문제 1번 정답:")
    solution_1()
    
    print("\n🎯 문제 2번 정답:")
    solution_2()
    
    print("\n🎯 문제 3번 정답:")
    solution_3()
    
    print("\n🎯 문제 4번 정답:")
    solution_4()
    
    print("\n🎯 문제 5번 정답:")
    solution_5()

# 정답 확인용 - 이 부분을 주석 해제하고 실행하세요
# run_all_solutions()
