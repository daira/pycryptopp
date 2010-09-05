from pycryptopp import _import_my_names

_import_my_names(globals(), "sha256_")

del _import_my_names

def start_up_self_test():
    """
    This is a quick test intended to detect major errors such as the library being
    miscompiled and segfaulting or returning incorrect answers.  We've had problems
    of that kind many times, thus justifying running this self-test on import.
    This idea was suggested to me by the second edition of "Practical
    Cryptography" by Ferguson, Schneier, and Kohno.
    This test was copied from pycryptopp/test/test_sha256.py on 2010-09-04.

    This test takes up to 1.5 milliseconds on a VirtualBox instance on
    my Macbook Pro (fast 64-bit Intel dual-core).

    Test that updating a hasher with various sized inputs yields
    the expected answer. This is somewhat redundant with
    test_chunksize(), but that's okay. This one exercises some
    slightly different situations (such as finalizing a hash after
    different length inputs.) This one is recursive so that there
    is a single fixed result that we expect.
    """
    hx = SHA256()
    for i in range(0, 65):
        s = "a" * i
        hy = SHA256(s).digest()
        hx.update(hy)
    for i in range(0, 65):
        hx.update('b')
        hx.update('c'*64)
    if hx.hexdigest().lower() != '79cbfab60b81f06937f376d4ad9560a60e70cb11a9b658a93e53010d1da77090':
        raise Error("pycryptopp failed startup self-test. Please run pycryptopp unit tests.")

start_up_self_test()
