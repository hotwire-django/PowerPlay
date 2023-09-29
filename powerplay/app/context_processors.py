def turbo(request):
    user_agent = request.META.get("HTTP_USER_AGENT")
    if user_agent:
        return {
            "turbo_native": "Turbo Native" in user_agent,
            "turbo_ios": "Turbo Native iOS" in user_agent,
            "turbo_android": "Turbo Native Android" in user_agent,
        }
