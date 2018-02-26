from . import settings

def app_info(req):
    return dict(
        build=settings.BUILD,
    )