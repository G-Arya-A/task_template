"""Örnek test dosyası."""


def test_example():
    """Örnek test - başarı durumu."""
    assert 1 + 1 == 2


def test_string_operations():
    """String işlemleri testi."""
    assert "hello".upper() == "HELLO"
    assert len("test") == 4
