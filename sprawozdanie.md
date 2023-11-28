# Laboratorium 5
## Petrashevich Ulyana

### Konfiguracja repozytorium
Na platformie Azure DevOps, w ustawieniach, tworzę nowy Personal Acces Token z uprawnieniami do zarządzania Work Items.
 ![azure1](https://github.com/PetrashU/PyPlines/assets/102193722/6ed15b6e-32f9-4554-a411-bfb6de7c6365)
![azure2](https://github.com/PetrashU/PyPlines/assets/102193722/b18b91fe-a875-4b7e-8e85-6a335cfc8bbb)

Token, jako też parametry bazy danych, dodaję do sekretów repozytorium na GitHub.
 ![git1](https://github.com/PetrashU/PyPlines/assets/102193722/dbc4ada0-0a75-439c-b571-8aec791fccb1)
![git2](https://github.com/PetrashU/PyPlines/assets/102193722/494d841e-de22-4156-ae1c-eb4536294fb7)
![git3](https://github.com/PetrashU/PyPlines/assets/102193722/45c02186-ce09-4439-8353-95c5c83fd5b5)

W projekcie dodałam zabezpieczenie przed scaleniem bez pull requestu.
 ![git4](https://github.com/PetrashU/PyPlines/assets/102193722/c7c4d017-e2e0-418f-b907-1bcb1dc42123)

### Testy
Przypomnienie – tak wyglądała moja aplikacja webowa MVC.
 ![app](https://github.com/PetrashU/PyPlines/assets/102193722/e98c9bcb-aa2c-4f85-a956-3767d5f13ba6)

W tym projekcie do plików zostały dodane:
*	Plik requirements.txt – zawiera wszystkie zainstalowane na maszynie pakiety python, tworzony poprzez komendę „pip freeze > requirements.txt”
*	Tests/test.py
Plik testowy zawiera instalację drivera za pomocą ChromeDriveManagera i podłączenie się do strony.
 ![test1](https://github.com/PetrashU/PyPlines/assets/102193722/6ad87680-19df-4630-837d-385130f2ea51)

Dalej zaimplementowane metody sprawdzające poprawne działanie. Znajdują odpowiednie pola/przyciski, wypełniają danymi, inicjują działanie i sprawdzają pojawienie się/usunięcie danych ze strony.
Dla komfortu obejrzenia testów dodałam też czekanie kilka sekund po wypełnieniu pól i naciśnięciach przycisków.
W testu na usunięcie rekordu pierwszy assert jest niepoprawny – musi być ‘not in’ zamiast ‘in’. Zrobiłam to z myślą o sprawdzaniu dodania bugu na platformę Azure. 
![test2](https://github.com/PetrashU/PyPlines/assets/102193722/91ee1e2e-6eaa-4658-8033-1db6128fc139)
![test3](https://github.com/PetrashU/PyPlines/assets/102193722/b1172e44-5147-4a06-8463-3b84dfe9d862)

### Action
Pipeline uruchamia się przy pull requestach o scaleniu z gałęzią main. Zaczyna z konfiguracji job i inicjalizacji kontenerów, w tym mysql. Potem konfiguruje srodowisko Python, instaluje wszystkie potrzebne pakiety z pliku requirement.txt. 
 ![action1](https://github.com/PetrashU/PyPlines/assets/102193722/2c34fc0c-2829-4768-9f97-3fdf359c1b76)

Dalej do pliku, z którego program parametry łączenia z bazą, wstawiam potrzebne dane. Uruchamiam aplikację i kilka sekund czekam, aż się załaduje. Następnie wywółuję testy, których stdout jako i stderr będzie zapisany do pliku error.txt. Jeżeli wystąpi błąd, w pliku error będzie to oznaczone dodatkową linijką „Failed”. Po czym inicjowany jest process dodania bug’a do Azure DevOps. Najpierw konfiguruję, w jakiej organizacji i w jakim projekcie pracuję. Potem loguję się za pomocą Tokenu i ostatecznie dodaje nowy work-item typu Bug.  
![action2](https://github.com/PetrashU/PyPlines/assets/102193722/3ba96fa4-f471-4fa8-86cf-7cf36e0a5b5b)
