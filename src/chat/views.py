from django.shortcuts import render
from django.http import HttpResponse
from .ml_models import embedding_model

def index(request):
    embedded_text = embedding_model.encode(["Hi! I'm John"])
    print(embedded_text)

    context = {"message_history": [{"role": "user", "message": "hi"},{"role": "assistant", "message": "hello"},{"role":"user", "message":"tell me more"}]}
    # context = {}
    return render(request, "chat/index.html", context)

