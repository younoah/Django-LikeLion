# Decorators

> 참고 : https://ssungkang.tistory.com/entry/python-%EC%9E%A5%EC%8B%9D%EC%9E%90-%EB%8D%B0%EC%BD%94%EB%A0%88%EC%9D%B4%ED%84%B0decorator-%EB%A5%BC-%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90

**함수를 Wrapping 하는 함수**

```python
from django.contrib.auth.decorators import login_required

@login_required # 장식자
def test_view(request):
    return render(request, 'test.html')
```

> 외부에서 들어올 때는 login_required가 감싸고 있는 것처럼 보이게 됩니다. 로직이 맞을 때, 내부의 test_view를 호출해서 사용할 수 있게 됩니다.

