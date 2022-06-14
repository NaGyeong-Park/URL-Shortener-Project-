from django.conf import settings
from random import choice
from string import ascii_letters, digits

# settings 모듈에서 값을 가져온다
SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 7)

AVAIABLE_CHARS = ascii_letters + digits

# 랜덤 코드 만들기
def create_random_code(chars=AVAIABLE_CHARS):
    # 정해진 사이즈(7)만큼 랜덤 문자열을 만든다.
    return "".join(
        [choice(chars) for _ in range(SIZE)]
    )

# 줄인 url 만들기
def create_shortened_url(model_instance):
    random_code = create_random_code()
    # model class 가져오기
    model_class = model_instance.__class__

    # 이미 있는 URL이라면 다시 랜덤 코드 만들기
    if model_class.objects.filter(short_url=random_code).exists():
        return create_shortened_url(model_instance)
    
    return random_code