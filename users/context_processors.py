def best_users(req):
    return dict(best_members=[
        'Kachalov', 'Buglight', 'Anonymous'
    ])


def current_user(req):
    return dict(
        current_user=dict(
            login='Kachalov',
            id=1,
        ),
    )