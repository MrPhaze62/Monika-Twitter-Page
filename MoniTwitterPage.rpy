init -990 python in mas_submod_utils:
    Submod(
        author="MrPhaze",
        name="Twitter Button",
        description="Opens up moni twiiter page v2.",
        version="0.0.1",
        dependencies={},
        settings_pane=None,
        version_updates={}
    )
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_opentwitter",
            category=['monika'],
            prompt="Monika Twitter Page",
            action=EV_ACT_PUSH,
            random=False,
            pool=True,
            unlocked=True
        )
    )


init python:
    import webbrowser

label monika_opentwitter:
    m 1eud "Want me to open my Twitter page?"
    m 4wub "Let me open it for you!"
    jump Moni_Twitsite
    
    return

label Moni_Twitsite:
    $ webbrowser.open("https://twitter.com/lilmonix3?lang=en")
    m 2hub "There we go!"
    return