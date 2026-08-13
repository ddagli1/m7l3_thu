import string
from password.new_password import generate_password


def test_password_characters():
    """Şifre oluşturulurken yalnızca geçerli karakterlerin kullanıldığını test eder"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)

    for char in password:
        assert char in valid_characters

def test_password_length():
    password = generate_password(20)
    assert len(password) == 20
def test_passwords_are_different():
    password1 = generate_password(20)
    password2 = generate_password(20)
    assert password1 != password2
"""
Aşağıda önerilenlerden birini kullanarak başka bir test yazın. Alternatif olarak, kendi testinizi de oluşturabilirsiniz!
Daha fazla test yazabilirseniz harika olur!

1. Şifrenin uzunluğunun belirtilen uzunlukla eşleşip eşleşmediğini test edin  
2. Arka arkaya oluşturulan iki şifrenin farklı olup olmadığını test edin 
"""
