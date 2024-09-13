import threading
from django.shortcuts import render
from .models import MyModel

def test_signal_view(request):
    # Get current thread ID in the view (caller)
    caller_thread = threading.get_ident()
    print(f"Caller thread ID: {caller_thread}")

    # Creating an instance of MyModel will trigger the post_save signal
    my_instance = MyModel.objects.create(name='Test Signal')

    return render(request, 'test.html', {})
