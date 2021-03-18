import hcskr

# hcskr.selfcheck("이름","생년월일","지역명","학교명","학교구분","비밀번호")

data = hcskr.selfcheck("한민석","030428","서울","둔촌고","고등학교","7530")
print(data['message']) //성공적으로 완료됬음을 표시
