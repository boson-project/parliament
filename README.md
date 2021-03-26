# Parliament

Parliament is a framework for invoking functions over HTTP. It
handles routing, liveness and readiness endpoints, and CloudEvent
extraction.

Function developers write functions that take a dictionary as the
single parameter. There is a `request` object in the dictionary
that is the Flask `request`object`. If the incoming request is a
POST of a CloudEvent, the event will be extracted and provided as a
`cloud_event` object in the dictionary.

[![Mothership Connection](parliament.jpg)](https://www.youtube.com/watch?v=gBWH3OWfT2Y)
