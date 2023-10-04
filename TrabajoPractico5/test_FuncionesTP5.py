import pytest
from FuncionesTP5 import validate_dni
from FuncionesTP5 import last_word
from FuncionesTP5 import ID_club
from FuncionesTP5 import is_multiple
from FuncionesTP5 import temperature
from FuncionesTP5 import text_function
from FuncionesTP5 import get_max_min
from FuncionesTP5 import area_perimeter
from FuncionesTP5 import login
from FuncionesTP5 import phrase_dict

@pytest.mark.parametrize("input,res", [
(38756526, True),
(1234567, True),
(123456789, False),
(123456, False),
(38756525, True),
(3875652, True)
])

def test_validate_dni(input,res):
    assert validate_dni(input) == res


@pytest.mark.parametrize("input,res", [
("hello world", 5),
("python is amazing", 7),
("   multiple   spaces   ", 6),
("", 0),
("12345 abcde", 5),
("12345", 5),
("     ", 0)
])

def test_last_word(input,res):
    assert last_word(input) == res

@pytest.mark.parametrize("name,last_name,DNI,result", [
("John", "Doe", 123456789, "John3123"),
("Alice Bob", "Smith", 987654321, "Alice5987"),
("Jane", "Doe", 987, "Jane3987"),
("Bob", "", 456789012, "Bob0456"),
("Charlie Delta", "Brown", 111, "Charlie5111"),
("Eva", "Green", 123, "Eva5123"),
("", "Taylor", 999, "6999")
])

def test_ID_club(name,last_name,DNI,result):
    assert ID_club(name,last_name,DNI) == result

@pytest.mark.parametrize("number, number2, result", [
    (10, 2, True),   
    (15, 3, True),   
    (7, 2, False),   
    (25, 5, True),   
    (100, 7, False),  
    (0, 10, True),   
    (20, 0, False)  
])

def test_is_multiple(number, number2, result):
    assert is_multiple(number,number2) == result

@pytest.mark.parametrize("temp_max, temp_min, result", [
    (30, 10, 20),   
    (-5, -15, -10),  
    (0, 0, 0),       
    (20, -20, 0),    
    (25.5, 15.5, 20.5),  
    (100, -50, 25) 
])

def test_temperature(temp_max, temp_min, result):
    assert temperature(temp_max,temp_min) == result

@pytest.mark.parametrize("input_text,result", [
    ("hello world!", "h e l l o  w o r l d !"),  
    ("12345", "1 2 3 4 5 "),  
    ("", ""),  
    ("abc123", "a b c 1 2 3 "),  
    ("   ", "   "),  
    ("!@#$%", "!@#$%")  
])

def test_text_function(input_text, result):
    assert text_function(input_text) == result

@pytest.mark.parametrize("numbers, result", [
    ([1, 2, 3, 4, 5], (5, 1)),         
    ([-5, -3, 0, 2, 4], (4, -5)),      
    ([10, 10, 10, 10], (10, 10)),     
    ([0], (0, 0)),                    
    ([100, 0, -50], (100, -50)),       
    ([3.5, 1.1, 2.2], (3.5, 1.1)),     
    ([], (None, None))                
])

def test_get_max_min(numbers, result):
    assert get_max_min(numbers) == result

@pytest.mark.parametrize("radio, result", [
    (1, "El area de la circunferencia es: 3.141592653589793 y el perimetro: 6.283185307179586"),  
    (2.5, "El area de la circunferencia es: 19.634954084936208 y el perimetro: 15.707963267948966"),  
    (0, "El area de la circunferencia es: 0.0 y el perimetro: 0.0"),  
    (-3, "El area de la circunferencia es: 28.274333882308138 y el perimetro: -18.84955592153876")  
])

def test_area_perimeter(radio, result):
    assert area_perimeter(radio) == result

@pytest.mark.parametrize("user, password, result", [
    ("usuario1", "asdasd", True),  
    ("usuario1", "incorrect", False),  
    ("otro_usuario", "asdasd", False),  
    ("otro_usuario", "incorrect", False)  
])    

def test_login(user, password,result):
    assert login(user, password) == result

@pytest.mark.parametrize("phrase, result", [
    ("This is a test", {'This': 4, 'is': 2, 'a': 1, 'test': 4}),  
    ("A simple phrase", {'A': 1, 'simple': 6, 'phrase': 6}),
    ("", {}),
    ("SingleWord", {'SingleWord': 10}), 
    ("    Multiple    Spaces    ", {'Multiple': 8, 'Spaces': 6}),  
    ("12345 abcde", {'12345': 5, 'abcde': 5}),  
])

def test_phrase_dict(phrase,result):
    assert phrase_dict(phrase) == result
