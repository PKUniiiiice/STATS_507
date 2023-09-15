import timeout_decorator
def wrap_test(test_fn, s=10):
    timeout_decorator.timeout(s, use_signals=False)(test_fn)()