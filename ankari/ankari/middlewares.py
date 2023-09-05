import time

class TimerMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwds):
        start_time = time.monotonic()
        print(request)
        response = self.get_response(request)
        # response.content = 'I am gey!' Изменить контент страницы
        end_time = time.monotonic()
        print('Time took: ', end_time - start_time)
        return response


class TestMiddleware():
    def __init__(self, get_response: callable):
        # get_response - обычная функция
        # callable - аннотация в Python, говорящая, что подрузамевает что будет функция в запросе
        self.get_response = get_response
    
    def __call__(self, request, *args, **kwds):
        # До ответа
        print('Before response')
        response = self.get_response(request, *args, **kwds) # CALLABLE VIEW
        # После ответа
        print('After response')
        return response
    
    

