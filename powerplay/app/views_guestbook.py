from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import StreamingHttpResponse
from django.template.loader import render_to_string
from app.forms import GuestbookForm

import json
from uuid import uuid4

import redis

r = redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)
p = r.pubsub()


def fetch_guest_list():
    guestlist = []
    for k, v in r.hgetall("guest1").items():
        name_comment = v.split("\n", 1)
        name = name_comment[0]
        comment = ""
        if len(name_comment) == 2:
            comment = name_comment[1]
        guestlist.append({"uuid": k, "name": name, "comment": comment})
    return guestlist


def save_guest_entry(form_data):
    r.hset("guest1", form_data["uuid"], f'{form_data["name"]}\n{form_data["comment"]}')
    r.publish("guest_stream", json.dumps(form_data))


def fetch_guest_count():
    return r.hlen("guest1")


def guestbook_list(request):
    # Create and set a unique id to represent this computer.
    request.session.setdefault("uuid", str(uuid4()))

    if request.method == "POST":
        form = GuestbookForm(request.POST)
        if form.is_valid():
            save_guest_entry(form.cleaned_data)

            # Method 1) redirect/reload page
            # Simplest & Slowest.
            messages.success(request, "Your changes have been saved.")
            return redirect("guestbook")

            # Method 2) return Frame
            # Limited to a box of changes.
            # Add data-turbo-frame="guestbook_frame" to the form element
            # guestlist = fetch_guest_list()
            # return render(request, "partials/guestbook_frame.html", {
            #     "guestlist": guestlist,
            #     "guest_count": len(guestlist),
            # })

            # Method 3) return Stream
            # return render(request, "streams/guestbook_entry.html", {
            #     "entry": form.cleaned_data,
            #     "guest_count": fetch_guest_count(),
            # }, content_type="text/vnd.turbo-stream.html")
    else:
        form = GuestbookForm(initial={"uuid": request.session["uuid"]})

    guestlist = fetch_guest_list()

    return render(
        request,
        "guestbook.html",
        {"form": form, "guestlist": guestlist, "guest_count": len(guestlist)},
        status=(422 if form.errors else 200),
    )


def guestbook_remove_entry(request, pk):
    r.hdel("guest1", str(pk))
    r.publish("guest_stream_remove", str(pk))
    return render(
        request,
        "streams/guestbook_entry_remove.html",
        {
            "uuid": pk,
            "guest_count": fetch_guest_count(),
        },
        content_type="text/vnd.turbo-stream.html",
    )


def event_stream():
    pubsub = r.pubsub()  # Each thread must have its own pubsub connection
    pubsub.subscribe("guest_stream", "guest_stream_remove")
    i = 0
    for message in pubsub.listen():
        print("msg", message)
        if message["type"] != "message":
            continue
        resp = None
        if message["channel"] == "guest_stream":
            entry = json.loads(message["data"])
            resp = render_to_string("streams/guestbook_entry.html", {"entry": entry})
        elif message["channel"] == "guest_stream_remove":
            resp = render_to_string(
                "streams/guestbook_entry_remove.html", {"uuid": message["data"]}
            )

        if resp:
            resp += render_to_string(
                "streams/guestbook_entry_counter.html",
                {"guest_count": fetch_guest_count()},
            )
            resp = resp.replace("\n", "")
            yield f"id:{i}\ndata: {resp}\n\n"
            i += 1


def guestbook_stream(request):
    return StreamingHttpResponse(event_stream(), content_type="text/event-stream")
