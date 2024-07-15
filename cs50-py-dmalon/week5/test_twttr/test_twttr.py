from twttr import shorten

def test_strip_vowels():
    assert shorten("apple is falling") == "ppl s fllng"
    assert shorten("Its a beautiful Life!!!") == "ts  btfl Lf!!!"
    assert shorten("Boeing 747 travels 10000 miles without refueling") == "Bng 747 trvls 10000 mls wtht rflng"
    assert shorten("123345 7878789789") == "123345 7878789789"