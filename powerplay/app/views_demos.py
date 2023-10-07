from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import StreamingHttpResponse

from app.models import Game

import time


def game_list_slow(request):
    time.sleep(3)
    p = Paginator(Game.objects.all(), 7)
    page = p.page(1)
    return render(request, "game_list.html", {"page": page})


def scroll_frame(request, page=1):
    objects = range(1, 1000)
    p = Paginator(objects, 5)
    page = p.page(page)
    return render(request, "partials/scroll_frame.html", {"page": page})


def sse(request):
    def event_stream():
        i = 0
        while True:
            i += 1
            output = f"""
<turbo-stream action="append" target="messages">
  <template>
    <div id="message_{i}">
      This div will be appended to the element with the DOM ID "messages_{i}".
    </div>
  </template>
</turbo-stream>
""".replace("\n", "")  # fmt: skip
            print(output)
            yield f"data: {output}\n\n"
            time.sleep(2)

    return StreamingHttpResponse(event_stream(), content_type="text/event-stream")
