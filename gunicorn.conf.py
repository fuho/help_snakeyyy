from dynoscale.hooks.gunicorn import pre_request as dynoscale_hook


def pre_request(worker, req):
    # https://dynoscale.net/documentation/getting-started-python
    dynoscale_hook(worker, req)
