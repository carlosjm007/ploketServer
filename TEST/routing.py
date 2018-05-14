from channels import route
from TEST.consumers import ws_connect, ws_receive, ws_disconnect
# There's no path matching on these routes; we just rely on the matching
# from the top-level routing. We _could_ path match here if we wanted.
websocket_routing = [
    # Called when WebSockets connect
    route("websocket.connect", ws_connect, path=r'^/live/(?P<sala>[^/]+)/(?P<id>[^/]+)/$'),

    # Called when WebSockets get sent a data frame
    route("websocket.receive", ws_receive, path=r'^/live/(?P<sala>[^/]+)/(?P<id>[^/]+)/$'),

    # Called when WebSockets disconnect
    route("websocket.disconnect", ws_disconnect, path=r'^/live/(?P<sala>[^/]+)/(?P<id>[^/]+)/$'),
]

custom_routing = [
    # Handling different chat commands (websocket.receive is decoded and put
    # onto this channel) - routed on the "command" attribute of the decoded
    # message.
]